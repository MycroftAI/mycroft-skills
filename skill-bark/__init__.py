# The MIT License (MIT)	
# 
# Copyright (c) 2016 Ethan Ward
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from os.path import dirname, join
from os import listdir
import re

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
from random import randrange

__author__ = 'eward'

LOGGER = getLogger(__name__)


class MP3DemoSkill(MycroftSkill):

    def __init__(self):
        super(MP3DemoSkill, self).__init__(name="MP3DemoSkill")
        self.process = None

    def initialize(self):
        self.load_data_files(dirname(__file__))

        # Loop thru the "mp3" folder and build an intent for
        # each song contain therein.  Change underscores in
        # the title to spaces.
        #
       # for name in listdir(join(dirname(__file__), "mp3")):
        #    name = re.sub(".mp3", "", name)
        #    name = re.sub("_", " ", name)
         #   self.register_vocabulary(name, "SongTitle")

      #  play_song_intent = IntentBuilder("PlaySongIntent").\
       #     require("PlayKeyword").require("SongTitle").build()
      #  self.register_intent(play_song_intent,
       #                      self.handle_play_song_intent)
        play_music_intent = IntentBuilder("PlayMusicIntent").\
            require("PlayKeyword").build()
        self.register_intent(play_music_intent,
                             self.handle_play_music_intent)

   # def handle_play_song_intent(self, message):
        # Play the song requested
     #   title = message.metadata.get("SongTitle")
        # No need to speak the title...
        # self.speak_dialog("play.song", {'title': title})
     #   title += ".mp3"
      #  title = re.sub(" ", "_", title)
      #  self.process = play_mp3(join(dirname(__file__), "mp3", title))

    def handle_play_music_intent(self, message):
        # Play any song
        mp3s = listdir(join(dirname(__file__), "mp3"))
        index = randrange(0, len(mp3s))
        self.process = play_mp3(join(dirname(__file__), "mp3", mp3s[index]))

    def stop(self):
        if self.process:  # and self.process.poll() is None:
            # No reason to say "music stopped", that is obvious!
            # self.speak_dialog('music.stop')
            self.process.terminate()
            self.process.wait()


def create_skill():
    return MP3DemoSkill()
