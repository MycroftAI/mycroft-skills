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

import requests
from json import JSONDecodeError
from mycroft.util.log import LOG


class HomeSeerCommandException(Exception):
    pass


class HomeseerInterface:
    TIMEOUT = 10

    def __init__(self, url, user=None, password=None):
        if url[:4] != "http":  # ensure user-entered IP address has `http` prefix
            url = "http://" + url
        self.url = url + "/JSON?"
        if user:
            self.url += "user={}&pass={}&".format(user, password)

    def _send_command(self, url: str):
        LOG.info("Sending request to {}".format(url))
        try:
            website = requests.get(url, timeout=self.TIMEOUT)
            website.close()
        except requests.exceptions.ConnectionError as detail:
            raise requests.exceptions.ConnectionError("Could not connect to HomeSeer. "
                                                      "Ensure service is running and IP address is correct.")
        if website.text.strip() == "error":
            raise HomeSeerCommandException("Request returned error.")
        try:
            if "Response" in website.json().keys() and "error" in website.json()["Response"].lower():
                raise HomeSeerCommandException(website.json()["Response"])
        except JSONDecodeError:
            raise HomeSeerCommandException("Request returned non-JSON result")
        LOG.info("...Request returned {}".format(website.json()))
        return website.json()

    def get_status(self, ref="", location="", location2=""):
        url = self.url + "request=getstatus"
        if len(ref) > 0:
            url += "&ref={}".format(ref)
        if len(location) > 0:
            url += "&location1={}".format(location)
        if len(location2) > 0:
            url += "&location2={}".format(location2)
        response = self._send_command(url)
        return response

    def get_events(self) -> list:
        url = self.url + "request=getevents"
        response = self._send_command(url)
        return response["Events"]

    def control_by_value(self, deviceref: int, value: float):
        url = self.url + "request=controldevicebyvalue&ref={}&value={}".format(str(deviceref), str(value))
        response = self._send_command(url)
        return response

    def control_by_label(self, deviceref: int, label: str):
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
