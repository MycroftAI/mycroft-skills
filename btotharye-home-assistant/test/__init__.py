from test.integrationtests.skills.skill_tester import SkillTest

import mock

kitchen_light_off = {'state': 'off', 'id': '1', 'dev_name': 'kitchen light'}
kitchen_light_on = {'state': 'on', 'id': '1', 'dev_name': 'kitchen light'}
thermostat_on = {'state': 'on', 'id': '3', 'dev_name': 'living room thermostat'}
thermostat_off = {'state': 'off', 'id': '3', 'dev_name': 'living room thermostat'}
kitchen_light_attr = {
            "id": '1',
            "dev_name": {'attributes':
                             {'friendly_name': 'Kitchen Lights', 'max_mireds': 500, 'min_mireds': 153, 'supported_features': 151},
                         'entity_id': 'light.kitchen_lights', 'state': 'off'}, 'unit_measure': 10}

temp_entity = {'state': '', 'id': '2', 'dev_name': 'hallway thermostat'}
temp_entity_attr =  {
                        "unit_measure": '°F',
                        "name": 'hallway thermostat',
                        "state": '75'
                    }

def test_runner(skill, example, emitter, loader):
    s = [s for s in loader.skills if s and s.root_dir == skill]

    if example.endswith('001.TurnOnLight.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = kitchen_light_off
        s[0].ha.find_entity_attr.return_value = kitchen_light_attr

    if example.endswith('003.TurnOffLight.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = kitchen_light_on
        s[0].ha.find_entity_attr.return_value = kitchen_light_attr

    if example.endswith('002.DimLight.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = kitchen_light_on
        s[0].ha.find_entity_attr.return_value = kitchen_light_attr

    if example.endswith('006.SetLightBright.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = kitchen_light_on
        s[0].ha.find_entity_attr.return_value = kitchen_light_attr

    if example.endswith('005.CurrentSensorValue.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = temp_entity
        s[0].ha.find_entity_attr.return_value = temp_entity_attr

    if example.endswith('007.TurnOffThermostat.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = thermostat_on

    if example.endswith('008.SetThermostatTemp.intent.json'):
        s[0].ha = mock.MagicMock()
        s[0].ha.find_entity.return_value = temp_entity
        s[0].ha.find_entity_attr.return_value = temp_entity_attr

    return SkillTest(skill, example, emitter).run(loader)
