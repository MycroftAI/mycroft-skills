# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


from os.path import dirname, join
import time
import random
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util import play_mp3
from mycroft.util.log import getLogger

__author__ = 'kfezer'

LOGGER = getLogger(__name__)


class SingingSkill(MycroftSkill):
    def __init__(self):
        super(SingingSkill, self).__init__(name="SingingSkill")
        self.process = None
        self.play_list = {
        0: join(dirname(__file__), "popey-favourite.mp3"),
        1: join(dirname(__file__), "popey-jackson.mp3"),
        2: join(dirname(__file__), "popey-jerusalem.mp3"),
        3: join(dirname(__file__), "popey-lose-yourself.mp3"),
        4: join(dirname(__file__), "popey-lovemetender.mp3"),
        5: join(dirname(__file__), "popey-rocketman.mp3"),
        }

    def initialize(self):
        intent = IntentBuilder("SingingIntent").require(
            "SingingKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        rando = random.randint(0,5) 
        file = self.play_list[rando]
        try:
            self.speak_dialog('singing')
            time.sleep(3)
            self.process = play_mp3(file)


        except Exception as e:
            LOGGER.error("Error: {0}".format(e))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.speak_dialog('singing.stop')
            self.process.terminate()
            self.process.wait()


def create_skill():
    return SingingSkill()
