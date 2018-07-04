from unittest import TestCase
import sys
sys.path.append('../')
for p in sys.path:
    print(p)
from ha_client import HomeAssistantClient
import unittest
from unittest import mock


kitchen_light = {'state': 'off', 'id': '1', 'dev_name': 'kitchen'}

json_data = {'attributes': {'friendly_name': 'Kitchen Lights',
                'max_mireds': 500,
                'min_mireds': 153,
                'supported_features': 151},
 'entity_id': 'light.kitchen_lights',
 'state': 'off'}

attr_resp = {
            "id": '1',
            "dev_name": {'attributes': {'friendly_name': 'Kitchen Lights', 'max_mireds': 500, 'min_mireds': 153, 'supported_features': 151}, 'entity_id': 'light.kitchen_lights', 'state': 'off'}}

headers = {
    'x-ha-access': 'password',
    'Content-Type': 'application/json'
}


class TestHaClient(TestCase):

    def test_mock_ssl(self):
        with mock.patch('requests.get') as mock_request:
            portnum = 8123
            ssl = True
            url = 'https://192.168.0.1:8123'

            mock_request.return_value.status_code = 200
            self.assertTrue(url, 'https://192.168.0.1:8123')
            self.assertTrue(portnum, 8123)
            self.assertTrue(ssl, True)
            self.assertTrue(mock_request.return_value.status_code, 200)

    def test_mock_ssl_no_port(self):
        with mock.patch('requests.get') as mock_request:
            portnum = None
            ssl = True
            url = 'https://192.168.0.1'

            mock_request.return_value.status_code = 200
            self.assertTrue(url, 'https://192.168.0.1')
            self.assertEqual(portnum, None)
            self.assertTrue(ssl, True)
            self.assertTrue(mock_request.return_value.status_code, 200)

    def test_broke_entity(self):
        portnum = 8123
        ssl = False
        ha = HomeAssistantClient(host='167.99.144.205', password='password', portnum=portnum, ssl=ssl)
        self.assertRaises(TypeError, ha)

    def test_light_nossl(self):
        portnum = 8123
        ssl = False
        ha = HomeAssistantClient(host='167.99.144.205', password='password', portnum=portnum, ssl=ssl)
        component = ha.find_component('light')
        entity = (ha.find_entity('kitchen', 'light'))
        if entity['best_score'] >= 50:
            print(entity['best_score'])
            print(entity)
            self.assertTrue(True)
        light_attr = ha.find_entity_attr(entity['id'])

        self.assertEqual(component, True)
        self.assertEqual(light_attr['name'], 'Kitchen Lights')
        self.assertEqual(entity['dev_name'], 'Kitchen Lights')
        self.assertEqual(ha.ssl, False)
        self.assertEqual(portnum, 8123)
        convo = ha.engage_conversation('turn off kitchen light')
        self.assertEqual(convo, {'extra_data': None, 'speech': 'Turned Kitchen Lights off'})
        ha_data = {'entity_id': entity['id']}
        if light_attr['state'] == 'on':
            r = ha.execute_service("homeassistant", "turn_off",
                                   ha_data)
            if r.status_code == 200:
                entity = ha.find_entity(light_attr['name'], 'light')
                if entity['state'] == 'off':
                    self.assertTrue(True)
                    self.assertEqual(entity,
                                     {'id': 'light.kitchen_lights', 'dev_name': 'Kitchen Lights', 'state': 'off',
                                      'best_score': 100})
                    self.assertEqual(light_attr['unit_measure'], 53)
                if entity['best_score'] >= 50:
                    self.assertTrue(True)
        else:
            r = ha.execute_service("homeassistant", "turn_on",
                                   ha_data)
            if r.status_code == 200:
                if entity['state'] == 'on':
                    self.assertTrue(True)
                    self.assertEqual(light_attr['state'], 'on')
                    self.assertEqual(entity,
                                     {'id': 'light.kitchen_lights', 'dev_name': 'Kitchen Lights', 'state': 'on',
                                      'best_score': 100})
                    self.assertEqual(light_attr['unit_measure'], 53)




    @mock.patch('ha_client.HomeAssistantClient.find_entity')
    def test_toggle_lights(self, mock_get):
        ha = HomeAssistantClient(host='192.168.0.1', password='password', portnum=8123, ssl=True)
        ha.find_entity = mock.MagicMock()
        entity = ha.find_entity(kitchen_light['dev_name'], 'light')
        mock_get.entity = {
                "id": '1',
                "dev_name": {'attributes': {'friendly_name': 'Kitchen Lights', 'max_mireds': 500, 'min_mireds': 153, 'supported_features': 151}, 'entity_id': 'light.kitchen_lights', 'state': 'off'}}
        self.assertEqual(mock_get.entity, attr_resp)
        ha_data = {'entity_id': entity['id']}
        state = entity['state']
        if state == 'on':
            ha.execute_service = mock.MagicMock()
            r = ha.execute_service("homeassistant", "turn_off",
                                   ha_data)
            if r.status_code == 200:
                entity = ha.find_entity(kitchen_light['dev_name'], 'light')
                if entity['state'] == 'off':
                    self.assertTrue(True)
                if entity['best_score'] >= 50:
                    self.assertTrue(True)

        else:
            ha.execute_service = mock.MagicMock()
            r = ha.execute_service("homeassistant", "turn_on",
                                   ha_data)
            if r.status_code == 200:
                if entity['state'] == 'on':
                    self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()



