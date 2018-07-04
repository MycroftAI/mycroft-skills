from requests import get, post
from fuzzywuzzy import fuzz
import json

__author__ = 'btotharye'

# Timeout time for HA requests
TIMEOUT = 10


class HomeAssistantClient(object):
    def __init__(self, host, password, portnum, ssl=False, verify=True):
        self.ssl = ssl
        self.verify = verify
        if portnum is None or portnum == 0:
            self.url = "https://%s" % host
        if self.ssl:
            self.url = "https://%s:%d" % (host, portnum)
        else:
            self.url = "http://%s:%d" % (host, portnum)
        self.headers = {
            'x-ha-access': password,
            'Content-Type': 'application/json'
        }

    def _get_state(self):
        if self.ssl:
            req = get("%s/api/states" %
                      self.url, headers=self.headers,
                      verify=self.verify, timeout=TIMEOUT)
        else:
            req = get("%s/api/states" % self.url, headers=self.headers,
                      timeout=TIMEOUT)

        if req.status_code == 200:
            return req.json()
        else:
            pass

    def find_entity(self, entity, types):
        json_data = self._get_state()
        # require a score above 50%
        best_score = 50
        best_entity = None
        if json_data:
            for state in json_data:
                try:
                    if state['entity_id'].split(".")[0] in types:
                        # something like temperature outside
                        # should score on "outside temperature sensor"
                        # and repetitions should not count on my behalf
                        score = fuzz.token_sort_ratio(
                            entity,
                            state['attributes']['friendly_name'].lower())
                        if score > best_score:
                            best_score = score
                            best_entity = {
                                "id": state['entity_id'],
                                "dev_name": state['attributes']
                                ['friendly_name'],
                                "state": state['state'],
                                "best_score": best_score}
                        score = fuzz.token_sort_ratio(
                            entity,
                            state['entity_id'].lower())
                        if score > best_score:
                            best_score = score
                            best_entity = {
                                "id": state['entity_id'],
                                "dev_name": state['attributes']
                                ['friendly_name'],
                                "state": state['state'],
                                "best_score": best_score}
                except KeyError:
                    pass
            return best_entity
    #
    # checking the entity attributes to be used in the response dialog.
    #

    def find_entity_attr(self, entity):
        json_data = self._get_state()

        if json_data:
            for attr in json_data:
                if attr['entity_id'] == entity:
                    entity_attrs = attr['attributes']
                    try:
                        if attr['entity_id'].startswith('light.'):
                            # Not all lamps do have a color
                            unit_measur = entity_attrs['brightness']
                        else:
                            unit_measur = entity_attrs['unit_of_measurement']
                    except KeyError:
                        unit_measur = None
                    # IDEA: return the color if available
                    # TODO: change to return the whole attr dictionary =>
                    # free use within handle methods
                    sensor_name = entity_attrs['friendly_name']
                    sensor_state = attr['state']
                    entity_attr = {
                        "unit_measure": unit_measur,
                        "name": sensor_name,
                        "state": sensor_state
                    }
                    return entity_attr
        return None

    def execute_service(self, domain, service, data):
        if self.ssl:
            r = post("%s/api/services/%s/%s" % (self.url, domain, service),
                     headers=self.headers, data=json.dumps(data),
                     verify=self.verify, timeout=TIMEOUT)
            return r
        else:
            r = post("%s/api/services/%s/%s" % (self.url, domain, service),
                     headers=self.headers, data=json.dumps(data), timeout=TIMEOUT)
            return r

    def find_component(self, component):
        """Check if a component is loaded at the HA-Server"""
        if self.ssl:
            req = get("%s/api/components" %
                      self.url, headers=self.headers, verify=self.verify,
                      timeout=TIMEOUT)
        else:
            req = get("%s/api/components" % self.url, headers=self.headers,
                      timeout=TIMEOUT)

        if req.status_code == 200:
            return component in req.json()

    def engage_conversation(self, utterance):
        """Engage the conversation component at the Home Assistant server
        Attributes:
            utterance    raw text message to be processed
        Return:
            Dict answer by Home Assistant server
            { 'speech': textual answer,
              'extra_data': ...}
        """
        data = {
            "text": utterance
        }
        if self.ssl:
            return post("%s/api/conversation/process" % (self.url),
                        headers=self.headers,
                        data=json.dumps(data),
                        verify=self.verify,
                        timeout=TIMEOUT
                        ).json()['speech']['plain']
        else:
            return post("%s/api/conversation/process" % (self.url),
                        headers=self.headers,
                        data=json.dumps(data),
                        timeout=TIMEOUT).json()['speech']['plain']
