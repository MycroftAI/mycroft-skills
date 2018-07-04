from adapt.intent import IntentBuilder
from mycroft.skills.core import FallbackSkill
from mycroft.util.log import getLogger
from mycroft import MycroftSkill, intent_file_handler
from os.path import dirname, join
from requests.exceptions import ConnectionError

from .ha_client import HomeAssistantClient

__author__ = 'robconnolly, btotharye, nielstron'
LOGGER = getLogger(__name__)

# Timeout time for HA requests
TIMEOUT = 10


class HomeAssistantSkill(FallbackSkill):

    def __init__(self):
        MycroftSkill.__init__(self)
        super(HomeAssistantSkill, self).__init__(name="HomeAssistantSkill")
        self.ha = None
        self.enable_fallback = False

    def _setup(self, force=False):
        if self.settings is not None and (force or self.ha is None):
            portnumber = self.settings.get('portnum')
            try:
                portnumber = int(portnumber)
            except TypeError:
                portnumber = 8123
            except ValueError:
                # String might be some rubbish (like '')
                portnumber = 0
            self.ha = HomeAssistantClient(
                self.settings.get('host'),
                self.settings.get('password'),
                portnumber,
                self.settings.get('ssl') == 'true',
                self.settings.get('verify') == 'true'
            )
            if self.ha:
                # Check if conversation component is loaded at HA-server
                # and activate fallback accordingly (ha-server/api/components)
                # TODO: enable other tools like dialogflow
                if (self.ha.find_component('conversation') and
                        self.settings.get('enable_fallback') == 'true'):
                    self.enable_fallback = True

    def _force_setup(self):
        LOGGER.debug('Creating a new HomeAssistant-Client')
        self._setup(True)

    def initialize(self):
        self.language = self.config_core.get('lang')
        self.load_vocab_files(join(dirname(__file__), 'vocab', self.lang))
        self.load_regex_files(join(dirname(__file__), 'regex', self.lang))
        self.__build_switch_intent()
        self.__build_light_adjust_intent()
        self.__build_automation_intent()
        self.__build_sensor_intent()
        self.__build_tracker_intent()
        self.register_intent_file('set.climate.intent', self.handle_set_thermostat_intent)
        self.register_intent_file('set.light.brightness.intent', self.handle_light_set_intent)
        # Needs higher priority than general fallback skills
        self.register_fallback(self.handle_fallback, 2)
        # Check and then monitor for credential changes
        self.settings.set_changed_callback(self.on_websettings_changed)

    def on_websettings_changed(self):
        # Only attempt to load if the host is set
        if self.settings.get('host', None):
            try:
                self._setup()
            except Exception:
                pass

    def __build_switch_intent(self):
        intent = IntentBuilder("switchIntent").require("SwitchActionKeyword") \
            .require("Action").require("Entity").build()
        self.register_intent(intent, self.handle_switch_intent)


    def __build_light_adjust_intent(self):
        intent = IntentBuilder("LightAdjBrightnessIntent") \
            .optionally("LightsKeyword") \
            .one_of("IncreaseVerb", "DecreaseVerb", "LightBrightenVerb",
                    "LightDimVerb") \
            .require("Entity").optionally("BrightnessValue").build()
        self.register_intent(intent, self.handle_light_adjust_intent)

    def __build_automation_intent(self):
        intent = IntentBuilder("AutomationIntent").require(
            "AutomationActionKeyword").require("Entity").build()
        self.register_intent(intent, self.handle_automation_intent)

    def __build_sensor_intent(self):
        intent = IntentBuilder("SensorIntent").require(
            "SensorStatusKeyword").require("Entity").build()
        # TODO - Sensors - Locks, Temperature, etc
        self.register_intent(intent, self.handle_sensor_intent)

    def __build_tracker_intent(self):
        intent = IntentBuilder("TrackerIntent").require(
            "DeviceTrackerKeyword").require("Entity").build()
        # TODO - Identity location, proximity
        self.register_intent(intent, self.handle_tracker_intent)


    def handle_switch_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        LOGGER.debug("Starting Switch Intent")
        entity = message.data["Entity"]
        action = message.data["Action"]
        LOGGER.debug("Entity: %s" % entity)
        LOGGER.debug("Action: %s" % action)
        # TODO if entity is 'all', 'any' or 'every' turn on
        # every single entity not the whole group
        try:
            ha_entity = self.ha.find_entity(
                entity, ['group', 'light', 'fan', 'switch', 'scene',
                         'input_boolean', 'climate'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return
        LOGGER.debug("Entity State: %s" % ha_entity['state'])
        ha_data = {'entity_id': ha_entity['id']}

        # IDEA: set context for 'turn it off' again or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        if self.language == 'de':
            if action == 'ein':
                action = 'on'
            elif action == 'aus':
                action = 'off'
        if ha_entity['state'] == action:
            LOGGER.debug("Entity in requested state")
            self.speak_dialog('homeassistant.device.already', data={
                "dev_name": ha_entity['dev_name'], 'action': action})
        elif action == "toggle":
            self.ha.execute_service("homeassistant", "toggle",
                                    ha_data)
            if(ha_entity['state'] == 'off'):
                action = 'on'
            else:
                action = 'off'
            self.speak_dialog('homeassistant.device.%s' % action,
                              data=ha_entity)
        elif action in ["on", "off"]:
            self.speak_dialog('homeassistant.device.%s' % action,
                              data=ha_entity)
            self.ha.execute_service("homeassistant", "turn_%s" % action,
                                    ha_data)
        else:
            self.speak_dialog('homeassistant.error.sorry')
            return

    @intent_file_handler('set.light.brightness.intent')
    def handle_light_set_intent(self, message):
        self._setup()
        if(self.ha is None):
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["entity"]
        try:
            brightness_req = float(message.data["brightnessvalue"])
            if brightness_req > 100 or brightness_req < 0:
                self.speak_dialog('homeassistant.brightness.badreq')
        except KeyError:
            brightness_req = 10.0
        brightness_value = int(brightness_req / 100 * 255)
        brightness_percentage = int(brightness_req)
        LOGGER.debug("Entity: %s" % entity)
        LOGGER.debug("Brightness Value: %s" % brightness_value)
        LOGGER.debug("Brightness Percent: %s" % brightness_percentage)
        try:
            ha_entity = self.ha.find_entity(
                entity, ['group', 'light'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return
        ha_data = {'entity_id': ha_entity['id']}

        # IDEA: set context for 'turn it off again' or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        ha_data['brightness'] = brightness_value
        ha_data['dev_name'] = ha_entity['dev_name']
        self.ha.execute_service("homeassistant", "turn_on", ha_data)
        self.speak_dialog('homeassistant.brightness.dimmed',
                          data=ha_data)

        return

    def handle_light_adjust_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["Entity"]
        try:
            brightness_req = float(message.data["BrightnessValue"])
            if brightness_req > 100 or brightness_req < 0:
                self.speak_dialog('homeassistant.brightness.badreq')
        except KeyError:
            brightness_req = 10.0
        brightness_value = int(brightness_req / 100 * 255)
        # brightness_percentage = int(brightness_req) # debating use
        LOGGER.debug("Entity: %s" % entity)
        LOGGER.debug("Brightness Value: %s" % brightness_value)
        try:
            ha_entity = self.ha.find_entity(
                entity, ['group', 'light'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return
        ha_data = {'entity_id': ha_entity['id']}
        # IDEA: set context for 'turn it off again' or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        # if self.language == 'de':
        #    if action == 'runter' or action == 'dunkler':
        #        action = 'dim'
        #    elif action == 'heller' or action == 'hell':
        #        action = 'brighten'
        if "DecreaseVerb" in message.data or \
                "LightDimVerb" in message.data:
            if ha_entity['state'] == "off":
                self.speak_dialog('homeassistant.brightness.cantdim.off',
                                  data=ha_entity)
            else:
                light_attrs = self.ha.find_entity_attr(ha_entity['id'])
                if light_attrs['unit_measure'] is None:
                    print(ha_entity)
                    self.speak_dialog(
                        'homeassistant.brightness.cantdim.dimmable',
                        data=ha_entity)
                else:
                    ha_data['brightness'] = light_attrs['unit_measure']
                    if ha_data['brightness'] < brightness_value:
                        ha_data['brightness'] = 10
                    else:
                        ha_data['brightness'] -= brightness_value
                    self.ha.execute_service("homeassistant",
                                            "turn_on",
                                            ha_data)
                    ha_data['dev_name'] = ha_entity['dev_name']
                    self.speak_dialog('homeassistant.brightness.decreased',
                                      data=ha_data)
        elif "IncreaseVerb" in message.data or \
                "LightBrightenVerb" in message.data:
            if ha_entity['state'] == "off":
                self.speak_dialog(
                    'homeassistant.brightness.cantdim.off',
                    data=ha_entity)
            else:
                light_attrs = self.ha.find_entity_attr(ha_entity['id'])
                if light_attrs['unit_measure'] is None:
                    self.speak_dialog(
                        'homeassistant.brightness.cantdim.dimmable',
                        data=ha_entity)
                else:
                    ha_data['brightness'] = light_attrs['unit_measure']
                    if ha_data['brightness'] > brightness_value:
                        ha_data['brightness'] = 255
                    else:
                        ha_data['brightness'] += brightness_value
                    self.ha.execute_service("homeassistant",
                                            "turn_on",
                                            ha_data)
                    ha_data['dev_name'] = ha_entity['dev_name']
                    self.speak_dialog('homeassistant.brightness.increased',
                                      data=ha_data)
        else:
            self.speak_dialog('homeassistant.error.sorry')
            return

    def handle_automation_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["Entity"]
        LOGGER.debug("Entity: %s" % entity)
        # also handle scene and script requests
        try:
            ha_entity = self.ha.find_entity(
                entity, ['automation', 'scene', 'script'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        ha_data = {'entity_id': ha_entity['id']}
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return

        # IDEA: set context for 'turn it off again' or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        LOGGER.debug("Triggered automation/scene/script: {}".format(ha_data))
        if "automation" in ha_entity['id']:
            self.ha.execute_service('automation', 'trigger', ha_data)
            self.speak_dialog('homeassistant.automation.trigger',
                              data={"dev_name": ha_entity['dev_name']})
        elif "script" in ha_entity['id']:
            self.speak_dialog('homeassistant.automation.trigger',
                              data={"dev_name": ha_entity['dev_name']})
            self.ha.execute_service("homeassistant", "turn_on",
                                    data=ha_data)
        elif "scene" in ha_entity['id']:
            self.speak_dialog('homeassistant.device.on',
                              data=ha_entity)
            self.ha.execute_service("homeassistant", "turn_on",
                                    data=ha_data)

    def handle_sensor_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["Entity"]
        LOGGER.debug("Entity: %s" % entity)
        try:
            ha_entity = self.ha.find_entity(entity, ['sensor'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return

        entity = ha_entity['id']

        # IDEA: set context for 'read it out again' or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        unit_measurement = self.ha.find_entity_attr(entity)
        if unit_measurement['state'] is not None:
            sensor_unit = unit_measurement['unit_measure']
        else:
            sensor_unit = ''

        sensor_name = unit_measurement['name']
        sensor_state = unit_measurement['state']
        # extract unit for correct pronounciation
        # this is fully optional
        try:
            from quantulum import parser
            quantulumImport = True
        except ImportError:
            quantulumImport = False

        if quantulumImport and unit_measurement != '':
            quantity = parser.parse((u'{} is {} {}'.format(
                sensor_name, sensor_state, sensor_unit)))
            if len(quantity) > 0:
                quantity = quantity[0]
                if (quantity.unit.name != "dimensionless" and
                        quantity.uncertainty <= 0.5):
                    sensor_unit = quantity.unit.name
                    sensor_state = quantity.value

        self.speak_dialog('homeassistant.sensor', data={
            "dev_name": sensor_name,
            "value": sensor_state,
            "unit": sensor_unit})
        # IDEA: Add some context if the person wants to look the unit up
        # Maybe also change to name
        # if one wants to look up "outside temperature"
        # self.set_context("SubjectOfInterest", sensor_unit)

    # In progress, still testing.
    # Device location works.
    # Proximity might be an issue
    # - overlapping command for directions modules
    # - (e.g. "How far is x from y?")
    def handle_tracker_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["Entity"]
        LOGGER.debug("Entity: %s" % entity)
        try:
            ha_entity = self.ha.find_entity(entity, ['device_tracker'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return

        # IDEA: set context for 'locate it again' or similar
        # self.set_context('Entity', ha_entity['dev_name'])

        entity = ha_entity['id']
        dev_name = ha_entity['dev_name']
        dev_location = ha_entity['state']
        self.speak_dialog('homeassistant.tracker.found',
                          data={'dev_name': dev_name,
                                'location': dev_location})

    @intent_file_handler('set.climate.intent')
    def handle_set_thermostat_intent(self, message):
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return
        entity = message.data["entity"]
        LOGGER.debug("Entity: %s" % entity)
        LOGGER.debug("This is the message data: %s" % message.data)
        temperature = message.data["temp"]
        LOGGER.debug("Temperature: %s" % temperature)
        try:
            ha_entity = self.ha.find_entity(entity, ['climate'])
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return
        if ha_entity is None:
            self.speak_dialog('homeassistant.device.unknown', data={
                              "dev_name": entity})
            return

        climate_data = {'entity_id': ha_entity['id'], 'temperature': temperature}
        climate_attr = self.ha.find_entity_attr(ha_entity['id'])
        r = self.ha.execute_service("climate", "set_temperature", data=climate_data)
        self.speak_dialog('homeassistant.set.thermostat', data={
                          "dev_name": climate_attr['name'],
                          "value": temperature,
                          "unit": climate_attr['unit_measure']})


    def handle_fallback(self, message):
        if not self.enable_fallback:
            return False
        self._setup()
        if self.ha is None:
            self.speak_dialog('homeassistant.error.setup')
            return False
        # pass message to HA-server
        try:
            response = self.ha.engage_conversation(
                message.data.get('utterance'))
        except ConnectionError:
            self.speak_dialog('homeassistant.error.offline')
            return False
        # default non-parsing answer: "Sorry, I didn't understand that"
        answer = response.get('speech')
        if not answer or answer == "Sorry, I didn't understand that":
            return False

        asked_question = False
        # TODO: maybe enable conversation here if server asks sth like
        # "In which room?" => answer should be directly passed to this skill
        if answer.endswith("?"):
            asked_question = True
        self.speak(answer, expect_response=asked_question)
        return True

    def shutdown(self):
        self.remove_fallback(self.handle_fallback)
        super(HomeAssistantSkill, self).shutdown()

    def stop(self):
        pass


def create_skill():
    return HomeAssistantSkill()
