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

from .HomeseerInterface import HomeseerInterface, HomeSeerCommandException
from mycroft.util.log import LOG


class HomeseerInterfaceSpoof(HomeseerInterface):
    def __init__(self, *args):
        super().__init__(*args)
        self._status = {
            "Name": "HomeSeer Devices",
            "Version": "1.0",
            "Devices": [
                {
                    "ref": 3398,
                    "name": "Temperature",
                    "location": "Z-Wave",
                    "location2": "Node 122",
                    "value": 82,
                    "status": "82 F",
                    "device_type_string": "Z-Wave Temperature",
                    "last_change": "\/Date(1410193983884)\/",
                    "relationship": 4,
                    "hide_from_view": False,
                    "associated_devices": [
                        3397
                    ],
                    "device_type": {
                        "Device_API": 16,
                        "Device_API_Description": "Thermostat API",
                        "Device_Type": 2,
                        "Device_Type_Description": "Thermostat Temperature",
                        "Device_SubType": 1,
                        "Device_SubType_Description": "Temperature"
                    },
                    "device_image": ""
                },
                {
                    "ref": 3570,
                    "name": "Switch Binary",
                    "location": "Z-Wave",
                    "location2": "Node 124",
                    "value": 255,
                    "status": "On",
                    "device_type_string": "Z-Wave Switch Binary",
                    "last_change": "\/Date(1410196540597)\/",
                    "relationship": 4,
                    "hide_from_view": False,
                    "associated_devices": [
                        3566
                    ],
                    "device_type": {
                        "Device_API": 4,
                        "Device_API_Description": "Plug-In API",
                        "Device_Type": 0,
                        "Device_Type_Description": "Plug-In Type 0",
                        "Device_SubType": 37,
                        "Device_SubType_Description": ""
                    },
                    "device_image": ""
                }
            ],
            "Events": [
                {
                    "Group": "Lighting",
                    "Name": "Outside Lights Off",
                    "id": 1234
                }
            ]
        }

    def _send_command(self, url: str):
        LOG.info("Calling {}".format(url))
        return "OK"

    def get_events(self):
        url = self.url + "request=getevents"
        response = self._send_command(url)
        return self._status["Events"]

    def get_status(self, ref="", location="", location2=""):
        url = self.url + "request=getstatus"
        if len(ref) > 0:
            url += "&ref={}".format(ref)
        if len(location) > 0:
            url += "&location1={}".format(location)
        if len(location2) > 0:
            url += "&location2={}".format(location2)
        response = self._send_command(url)

        if len(ref):
            for d in self._status["Devices"]:
                if d["ref"] == int(ref):
                    return {
                        "Devices": [
                            d
                        ]
                    }
            raise HomeSeerCommandException("Device with ref {} not found in status".format(ref))
        else:
            return self._status

    def control_by_value(self, deviceref, value: float):
        url = self.url + "request=controldevicebyvalue&ref={}&value={}".format(str(deviceref), str(value))
        response = self._send_command(url)
        return response

    def control_by_label(self, deviceref, label: str):
        url = self.url + "request=controldevicebylabel&ref={}&label={}".format(str(deviceref), label)
        response = self._send_command(url)
        return response

    def run_event_by_group(self, group_name: str, event_name: str):
        url = self.url + "request=runevent&group={}&name={}".format(group_name, event_name)
        response = self._send_command(url)
        return response

    def run_event_by_event_id(self, event_id):
        url = self.url + "request=runevent&id={}".format(str(event_id))
        response = self._send_command(url)
        return response