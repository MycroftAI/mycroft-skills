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

import feedparser
import time
from os.path import dirname
import re

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None

__author__ = 'jamespoole'

LOGGER = getLogger(__name__)

class GimletPodcastSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(GimletPodcastSkill, self).__init__(name="GimletPodcastSkill")

        #List of all of the currently available rss urls from gimlet
        self.rss_urls = {
                'reply-all': 'http://feeds.gimletmedia.com/hearreplyall',
                'startup': 'http://feeds.gimletmedia.com/hearstartup',
                'elt': 'http://feeds.gimletmedia.com/eltshow',
                'crimetown': 'http://feeds.gimletmedia.com/crimetownshow',
                'heavyweight': 'http://feeds.gimletmedia.com/heavyweightpodcast',
                'homecoming': 'http://feeds.gimletmedia.com/homecomingshow',
                'mogul': 'http://feeds.gimletmedia.com/mogulshow',
                'sampler': 'http://feeds.gimletmedia.com/samplershow',
                'svs': 'http://feeds.gimletmedia.com/sciencevs',
                'nod': 'http://feeds.gimletmedia.com/thenodshow',
                'pitch': 'http://feeds.gimletmedia.com/thepitchshow',
                'tremoved': 'http://feeds.gimletmedia.com/twiceremovedshow',
                'uncivil': 'http://feeds.gimletmedia.com/uncivil',
                'undone': 'http://feeds.gimletmedia.com/undoneshow'
                }

        self.process = None
        self.audioservice = None
        self.listen_url = ""

    def initialize(self):
        play_podcast_intent = IntentBuilder("PlayPodcastIntent").require(
            "PlayPodcastKeyword").build()
        self.register_intent(play_podcast_intent, self.handle_play_podcast_intent)

        if AudioService:
            self.audioservice = AudioService(self.emitter)

    def handle_play_podcast_intent(self, message):
        utter = message.data['utterance']

        #listen for some key words to trigger the correct podcast
        if "reply-all" in utter:
            self.listen_url = self.rss_urls['reply-all']
        elif "startup" in utter:
            self.listen_url = self.rss_urls['startup']
        elif "every little thing" in utter:
            self.listen_url = self.rss_urls['elt']
        elif "crimetown" or "crime" in utter:
            self.listen_url = self.rss_urls['crimetown']
        elif "heavyweight" in utter:
            self.listen_url = self.rss_urls['heavyweight']
        elif "homecoming" in utter:
            self.listen_url = self.rss_urls['homecoming']
        elif "mogul" in utter:
            self.listen_url = self.rss_urls['mogul']
        elif "sampler" in utter:
            self.listen_url = self.rss_urls['sampler']
        elif "science" in utter:
            self.listen_url = self.rss_urls['svs']
        elif "nod" in utter:
            self.listen_url = self.rss_urls['nod']
        elif "pitch" in utter:
            self.listen_url = self.rss_urls['pitch']
        elif "twice removed" in utter:
            self.listen_url = self.rss_urls['tremoved']
        elif "uncivil" in utter:
            self.listen_url = self.rss_urls['uncivil']
        elif "undone" in utter:
            self.listen_url = self.rss_urls['undone']

        self.speak_dialog('latest')

        time.sleep(3)

        data = feedparser.parse(self.listen_url)

        url = (data['entries'][0]['links'][0]['href'])
        # if audio service module is available use it
        if self.audioservice:
            self.audioservice.play(url, message.data['utterance'])

        self.enclosure.mouth_text(data['entries'][0]['title'])

    def stop(self):
        pass

def create_skill():
    return GimletPodcastSkill()
