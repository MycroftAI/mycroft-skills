"""
    homeseer-mycroft: Skill for Mycroft allowing HomeSeer hub connectivity
    Copyright (C) 2018 Sawyer McLane

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from collections import namedtuple
from fuzzywuzzy import fuzz, process

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.parse import extract_number

from .homeseer_interface.HomeseerInterface import HomeseerInterface, HomeSeerCommandException

# from .homeseer_interface.HomeseerInterfaceSpoof import HomeseerInterfaceSpoof as HomeseerInterface, \
#     HomeSeerCommandException


Device = namedtuple('Device', 'ref name location location2')
Event = namedtuple('Event', 'group name id')


class HomeSeerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor

    def __init__(self):
        super(HomeSeerSkill, self).__init__(name="HomeSeerSkill")

        self.hs = HomeseerInterface(self.config.get('url'), self.config.get('username'), self.config.get('password'))
        self.device_list = []
        self.event_list = []

    def initialize(self):
        supported_languages = ["en-us"]

        if self.lang not in supported_languages:
            self.log.warning("Unsupported language ({}) for {}, shutting down skill".format(self.lang, self.name))
            self.shutdown()

        # Get HomeSeer devices from status query
        try:
            for d in self.hs.get_status()["Devices"]:
                self.device_list.append(Device(str(d["ref"]), d["name"], d["location"], d["location2"]))
            for e in self.hs.get_events():
                self.event_list.append(Event(e["Group"], e["Name"], str(e["id"])))
        except HomeSeerCommandException:
            self.log.warning("Unable to connect to HomeSeer. Shutting down.")
            self.shutdown()

    @property
    def device_refs(self):
        return [d.ref for d in self.device_list]

    @property
    def device_names(self):
        return [d.name for d in self.device_list]

    @property
    def device_locations(self):
        return [d.location for d in self.device_list]

    @property
    def device_location2s(self):
        return [d.location2 for d in self.device_list]

    @property
    def device_details(self):
        return [self.get_detail(device) for device in self.device_list]

    @staticmethod
    def get_detail(device: Device):
        return " ".join([device.location2, device.location, device.name])

    def get_device_by_attributes(self, detail: str) -> Device:
        best_score = 0
        score = 0
        best_device = None

        for device in self.device_list:
            device_detail = self.get_detail(device)
            score = fuzz.ratio(detail, device_detail)
            if score > best_score:
                best_score = score
                best_device = device

        return best_device

    def get_event_by_attributes(self, detail: str):
        best_score = 0
        score = 0
        best_event = None

        for event in self.event_list:
            event_detail = event.name
            score = fuzz.ratio(detail, event_detail)
            if score > best_score:
                best_score = score
                best_event = event

        return best_event

    def get_devices_by_attributes(self, detail: str) -> [Device]:
        """ Get a list of devices by returning all that have the same score as the best Device. """
        ranklist = process.extract(detail, self.device_details)
        best_score = ranklist[0][1]
        return [device for device in self.device_list if fuzz.WRatio(detail, self.get_detail(device)) == best_score]

    @intent_handler(IntentBuilder("").require("StatusDetail"))
    def handle_get_status_intent(self, message):
        detail = message.data["StatusDetail"]
        device = self.get_device_by_attributes(detail)
        try:
            status_json = self.hs.get_status(device.ref, device.location, device.location2)
            status_string = status_json["Devices"][0]["status"]

            self.speak_dialog('DeviceStatus', {'name': device.name,
                                               'value': status_string})
        except HomeSeerCommandException as e:
            self.speak_dialog('Error', {'exception': str(e)})

    @intent_handler(IntentBuilder("").require("ToggleSetting").require("ToggleSingleDetail"))
    def handle_turn_setting_intent(self, message):
        detail = message.data["ToggleSingleDetail"]
        setting = message.data["ToggleSetting"]
        self.log.info("Setting details {} to {}".format(detail, setting))
        device = self.get_device_by_attributes(detail)
        self.speak_dialog('ToggleSingle', {'setting': setting,
                                           'name': device.name})
        try:
            self.hs.control_by_label(device.ref, setting)
        except HomeSeerCommandException as e:
            self.speak_dialog('Error', {'exception': str(e)})

    @intent_handler(IntentBuilder("").require("AllKeyword").require("ToggleSetting").require("ToggleSingleDetail"))
    def handle_turn_setting_all_intent(self, message):
        detail = message.data["ToggleSingleDetail"]
        setting = message.data["ToggleSetting"]
        self.log.info("Setting ALL details {} to {}".format(detail, setting))
        self.speak_dialog('ToggleAll', {'setting': setting,
                                        'name': detail})
        devices = self.get_devices_by_attributes(detail)
        for d in devices:
            try:
                self.hs.control_by_label(d.ref, setting)
            except HomeSeerCommandException as e:
                self.speak_dialog('Error', {'exception': str(e)})
                break

    @intent_handler(IntentBuilder("").require("LockSetting").require("LockDetail"))
    def handle_lock_setting_intent(self, message):
        detail = message.data["LockDetail"]
        setting = message.data["LockSetting"]
        device = self.get_device_by_attributes(detail)
        self.log.info("{}ing {}...".format(setting, detail))
        self.speak_dialog('Lock', {'setting': setting,
                                   'name': device.name})
        try:
            self.hs.control_by_label(device.ref, setting + "ed")
        except HomeSeerCommandException as e:
            self.speak_dialog('Error', {'exception': str(e)})

    @intent_handler(IntentBuilder("").require("SetDetail"))
    def handle_set_percentage_intent(self, message):
        detail = message.data["SetDetail"]
        # Adapt is dumb with `%` characters, so we have to dead-reckon the location of the percentage
        index = message.data["utterance"].rfind("to")
        percent = str(int(extract_number(message.data["utterance"][index:].translate({ord('%'): None}),
                                         short_scale=False)))  # Remove % symbol that STT probably put there.
        device = self.get_device_by_attributes(detail)
        self.log.info("Setting {} to {}%".format(device.name, percent))
        self.speak_dialog('SetPercent', {'percent': percent,
                                         'name': device.name})
        try:
            self.hs.control_by_value(device.ref, int(percent))
        except HomeSeerCommandException as e:
            self.speak_dialog('Error', {'exception': str(e)})

    @intent_handler(IntentBuilder("").require("AllKeyword").require("SetDetail"))
    def handle_set_percentage_all_intent(self, message):
        detail = message.data["SetDetail"]
        index = message.data["utterance"].rfind("to")
        percent = str(int(extract_number(message.data["utterance"][index:].translate({ord('%'): None}),
                                         short_scale=False)))
        devices = self.get_devices_by_attributes(detail)
        self.log.info("Setting {} to {}%".format(detail, percent))
        self.speak_dialog('SetPercentAll', {'percent': percent,
                                            'name': detail})
        for d in devices:
            try:
                self.hs.control_by_value(d.ref, int(percent))
            except HomeSeerCommandException as e:
                self.speak_dialog('Error', {'exception': str(e)})
                break

    @intent_handler(IntentBuilder("").require("EventDetail"))
    def handle_run_event_intent(self, message):
        detail = message.data["EventDetail"]
        event = self.get_event_by_attributes(detail)
        self.log.info("Running event {}".format(event.name))
        self.speak_dialog('RunEvent', {'event': event.name})
        try:
            self.hs.run_event_by_event_id(event.id)
        except HomeSeerCommandException as e:
            self.speak_dialog('Error', {'exception': str(e)})


def create_skill():
    return HomeSeerSkill()
