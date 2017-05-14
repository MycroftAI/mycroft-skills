from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from os.path import dirname, join
from requests import get, post
from fuzzywuzzy import fuzz
import json

__author__ = 'robconnolly, btotharye'
LOGGER = getLogger(__name__)


class HomeAssistantClient(object):
    def __init__(self, host, password, port=8123, ssl=False):
        self.ssl = ssl
        if self.ssl:
            port=443
            self.url = "https://%s:%d" % (host, port)
        else:
            self.url = "http://%s:%d" % (host, port)
        self.headers = {
            'x-ha-access': password,
            'Content-Type': 'application/json'
        }

    def find_entity(self, entity, types):
        if self.ssl:
            req = get("%s/api/states" % self.url, headers=self.headers, verify=True)
        else:
            req = get("%s/api/states" % self.url, headers=self.headers)

        if req.status_code == 200:
            best_score = 0
            best_entity = None
            for state in req.json():
                try:
                    if state['entity_id'].split(".")[0] in types:
                        LOGGER.debug("Entity Data: %s" % state)
                        score = fuzz.ratio(entity, state['attributes']['friendly_name'].lower())
                        if score > best_score:
                            best_score = score
                            best_entity = { "id": state['entity_id'],
                                            "dev_name": state['attributes']['friendly_name'],
                                            "state": state['state'] }
                except KeyError:
                    pass
            return best_entity
    #
    # checking the entity attributes to be used in the response dialog.
    #
    def find_entity_attr(self, entity):
        if self.ssl:
            req = get("%s/api/states" % self.url, headers=self.headers, verify=True)
        else:
            req = get("%s/api/states" % self.url, headers=self.headers)

        if req.status_code == 200:
            for attr in req.json():
                if attr['entity_id'] == entity:
                    try:
                        unit_measurement = attr['attributes']['unit_of_measurement']
                        sensor_name = attr['attributes']['friendly_name']
                        sensor_state = attr['state']
                        return unit_measurement, sensor_name, sensor_state
                    except:
                        unit_measurement = 'null'
                        sensor_name = attr['attributes']['friendly_name']
                        sensor_state = attr['state']
                        return unit_measurement, sensor_name, sensor_state

        return None

    def execute_service(self, domain, service, data):
        if self.ssl:
            post("%s/api/services/%s/%s" % (self.url, domain, service), headers=self.headers, data=json.dumps(data), verify=True)
        else:
            post("%s/api/services/%s/%s" % (self.url, domain, service), headers=self.headers, data=json.dumps(data))

# TODO - Localization
class HomeAssistantSkill(MycroftSkill):
    def __init__(self):
        super(HomeAssistantSkill, self).__init__(name="HomeAssistantSkill")
        self.ha = HomeAssistantClient(self.config.get('host'),
            self.config.get('password'), ssl=self.config.get('ssl', False))

    def initialize(self):
        self.load_vocab_files(join(dirname(__file__), 'vocab', self.lang))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))
        self.__build_lighting_intent()
        self.__build_sensor_intent()

    def __build_lighting_intent(self):
        intent = IntentBuilder("LightingIntent").require("LightActionKeyword").require("Action").require("Entity").build()
        # TODO - Locks, Temperature, Identity location
        self.register_intent(intent, self.handle_lighting_intent)

    def __build_sensor_intent(self):
        intent = IntentBuilder("SensorIntent").require("SensorStatusKeyword").require("Entity").build()
        # TODO - Locks, Temperature, Identity location
        self.register_intent(intent, self.handle_sensor_intent)

    def handle_lighting_intent(self, message):
        entity = message.data["Entity"]
        action = message.data["Action"]
        LOGGER.debug("Entity: %s" % entity)
        LOGGER.debug("Action: %s" % action)
        ha_entity = self.ha.find_entity(entity, ['group','light', 'switch', 'scene', 'input_boolean'])
        if ha_entity is None:
            #self.speak("Sorry, I can't find the Home Assistant entity %s" % entity)
            self.speak_dialog('homeassistant.device.unknown', data={"dev_name": ha_entity['dev_name']})
            return
        ha_data = {'entity_id': ha_entity['id']}

        if action == "on":
            if ha_entity['state'] == action:
                self.speak_dialog('homeassistant.device.already',\
                        data={ "dev_name": ha_entity['dev_name'], 'action': action })
            else:
                self.speak_dialog('homeassistant.device.on', data=ha_entity)
                self.ha.execute_service("homeassistant", "turn_on", ha_data)
        elif action == "off":
            if ha_entity['state'] == action:
                self.speak_dialog('homeassistant.device.already',\
                        data={"dev_name": ha_entity['dev_name'], 'action': action })
            else:
                self.speak_dialog('homeassistant.device.off', data=ha_entity)
                self.ha.execute_service("homeassistant", "turn_off", ha_data)
        elif action == "dim":
            if ha_entity['state'] == "off":
                self.speak_dialog('homeassistant.device.off', data={"dev_name": ha_entity['dev_name']})
                self.speak("Can not dim %s. It is off." % ha_entity['dev_name'])
            else:
                #self.speak_dialog('homeassistant.device.off', data=ha_entity)
                self.speak("Dimmed the %s" % ha_entity['dev_name'])
                #self.ha.execute_service("homeassistant", "turn_off", ha_data)
        elif action == "brighten":
            if ha_entity['state'] == "off":
                self.speak_dialog('homeassistant.device.off', data={"dev_name": ha_entity['dev_name']})
                self.speak("Can not brighten %s. It is off." % ha_entity['dev_name'])
            else:
                #self.speak_dialog('homeassistant.device.off', data=ha_entity)
                self.speak("Increased brightness of %s" % ha_entity['dev_name'])
                #self.ha.execute_service("homeassistant", "turn_off", ha_data)
        else:
            ##self.speak("I don't know what you want me to do.")
            self.speak_dialog('homeassistant.error.sorry')
    #
    # In progress, still testing.
    #
    def handle_sensor_intent(self, message):
        entity = message.data["Entity"]
        LOGGER.debug("Entity: %s" % entity)
        ha_entity = self.ha.find_entity(entity, ['sensor', 'device_tracker'])
        if ha_entity is None:
            #self.speak("Sorry, I can't find the Home Assistant entity %s" % entity)
            self.speak_dialog('homeassistant.device.unknown', data={"dev_name": ha_entity['dev_name']})
            return
        ha_data = ha_entity
        entity = ha_entity['id']
        unit_measurement = self.ha.find_entity_attr(entity)
        if unit_measurement[0] != 'null':
            sensor_unit = unit_measurement[0]
            sensor_name = unit_measurement[1]
            sensor_state = unit_measurement[2]
            self.speak(('Currently {} is {} {}'.format(sensor_name, sensor_state, sensor_unit)))
        else:
            sensor_name = unit_measurement[1]
            sensor_state = unit_measurement[2]
            self.speak('Currently {} is {}'.format(sensor_name, sensor_state))


    def stop(self):
        pass


def create_skill():
    return HomeAssistantSkill()
