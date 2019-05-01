# Copyright 2019 rekkitcwts
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import feedparser
import re
import os
import subprocess

from adapt.intent import IntentBuilder
from mycroft.audio import wait_while_speaking
from mycroft.skills.core import intent_handler, intent_file_handler
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
import traceback
from requests import Session


# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# Audiobook Skill, based on this feature request on github: https://github.com/MycroftAI/mycroft-skills/issues/47
# Used the NPR News skill as a base.

class AudiobookSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(AudiobookSkill, self).__init__(name="AudiobookSkill")
        
        # TODO: Initialize working variables used within the skill.
        

    # Plays the audiobook.
    # Idea: Will save the audiobook zip file, then extract it, before
    # it can be played

    @intent_handler(IntentBuilder("").require("Play").require("Audiobook"))
    def handle_count_intent(self, message):
        utterance = message.data.get('utterance')
        self.speak_dialog('loading.audiobook', data={title: utterance})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return AudiobookSkill()
