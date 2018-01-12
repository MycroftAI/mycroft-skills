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


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname, join
from os import listdir

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None

__author__ = 'Hasinator7'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)


# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class NatureSoundSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(NatureSoundSkill, self).__init__(name="NatureSoundSkill")
        self.audioservice = None

    def getPath(self, name):
        return (join(dirname(__file__), "mp3", name))
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.audioservice = None
        
        if AudioService:
            self.audioservice = AudioService(self.emitter)
        
        river_intent = IntentBuilder("RiverIntent").\
                         require("PlayKeyword").\
                         require("RainyRiverKeyword").build()
        self.register_intent(river_intent, self.handle_river_intent)
        
        dawn_intent = IntentBuilder("DawnIntent").\
                         require("PlayKeyword").\
                         require("DawnKeyword").build()
        self.register_intent(dawn_intent, self.handle_dawn_intent)
        
        thunderstorm_intent = IntentBuilder("ThunderstormIntent").\
                         require("PlayKeyword").\
                         require("ThunderstormKeyword").build()
        self.register_intent(thunderstorm_intent, self.handle_thunderstorm_intent)
        
        tropical_storm_intent = IntentBuilder("TropicalStormIntent").\
                         require("PlayKeyword").\
                         require("TropicalStormKeyword").build()
        self.register_intent(tropical_storm_intent, self.handle_tropical_storm_intent)
        
        ocean_intent = IntentBuilder("OceanIntent").\
                         require("PlayKeyword").\
                         require("OceanKeyword").build()
        self.register_intent(ocean_intent, self.handle_ocean_intent)
        
        rainforest_intent = IntentBuilder("RainforestIntent").\
                         require("PlayKeyword").\
                         require("RainforestKeyword").build()
        self.register_intent(rainforest_intent, self.handle_rainforest_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    #TODO: Loop mp3s

    def handle_river_intent(self, message):
        path = self.getPath("rainy-river.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Rainy river"})
    
    def handle_dawn_intent(self, message):
        path = self.getPath("dawn-chorus.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Dawn chorus"})

    def handle_thunderstorm_intent(self, message):
        path = self.getPath("urban-thunderstorm.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Thunderstorm"})

    def handle_tropical_storm_intent(self, message):
        path = self.getPath("tropical-storm.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Tropical Storm"})

    def handle_rainforest_intent(self, message):
        path = self.getPath("rainforest.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Rainforest"})

    def handle_ocean_intent(self, message):
        path = self.getPath("ocean-waves.mp3")
        if self.audioservice:
            self.audioservice.play(path, message.data['utterance'])
        else:
            self.process = play_mp3(path)
        self.speak_dialog("info",{"environment":"Ocean waves"})
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return NatureSoundSkill()
