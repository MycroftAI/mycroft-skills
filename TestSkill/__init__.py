# Copyright 2018 Mycroft AI Inc.
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
import re
import time
from mycroft.messagebus.message import Message
from mycroft import FallbackSkill
from threading import Lock


EXTENSION_TIME = 10


class TestSkill(FallbackSkill):
    def __init__(self):
        super().__init__()
        self.query_replies = {}     # cache of received replies
        self.query_extensions = {}  # maintains query timeout extensions
        self.lock = Lock()
        self.waiting = True
        self.answered = False

    def initialize(self):
        self.add_event('question:query.response',
                       self.handle_query_response)
        self.register_fallback(self.handle_question, 5)


    #@intent_handler(AdaptIntent().require('Question'))
    def handle_question(self, message):
        """ Send the phrase to the CommonQuerySkills and prepare for handling
            the replies.
        """
        self.waiting = True
        self.answered = False
        utt = message.data.get('utterance')
        self.enclosure.mouth_think()

        self.query_replies[utt] = []
        self.query_extensions[utt] = []
        self.log.info('Searching for {}'.format(utt))
        # Send the query to anyone listening for them
        self.bus.emit(message.forward('question:query', data={'phrase': utt}))

        self.timeout_time = time.time() + 1
        self.schedule_event(self._query_timeout, 1,
                            data={'phrase': utt},
                            name='QuestionQueryTimeout')

        while True:
            if not self.waiting or time.time() > self.timeout_time + 1:
                break

            time.sleep(1)
        return self.answered

    def handle_query_response(self, message):
        with self.lock:
            search_phrase = message.data['phrase']
            skill_id = message.data['skill_id']
            searching = message.data.get('searching')
            answer = message.data.get('answer')

            # Manage requests for time to complete searches
            if searching:
                # extend the timeout by 5 seconds
                self.cancel_scheduled_event('QuestionQueryTimeout')
                self.timeout_time = time.time() + EXTENSION_TIME
                self.schedule_event(self._query_timeout,
                                    EXTENSION_TIME,
                                    data={'phrase': search_phrase},
                                    name='QuestionQueryTimeout')

                # TODO: Perhaps block multiple extensions?
                if (search_phrase in self.query_extensions and
                        skill_id not in self.query_extensions[search_phrase]):
                    self.query_extensions[search_phrase].append(skill_id)
            elif search_phrase in self.query_extensions:
                # Search complete, don't wait on this skill any longer
                if answer and search_phrase in self.query_replies:
                    self.log.info('Answer from {}'.format(skill_id))
                    self.query_replies[search_phrase].append(message.data)
                # Remove the skill from list of extensions
                if skill_id in self.query_extensions[search_phrase]:
                    self.query_extensions[search_phrase].remove(skill_id)
                    if not self.query_extensions[search_phrase]:
                        self.cancel_scheduled_event('QuestionQueryTimeout')
                        self.schedule_event(self._query_timeout, 1,
                                            data={'phrase': search_phrase},
                                            name='QuestionQueryTimeout')
            else:
                self.log.warning('{} Answered too slowly,'
                                 'will be ignored.'.format(skill_id))

    def _query_timeout(self, message):
        # Prevent any late-comers from retriggering this query handler
        with self.lock:
            self.log.info('Timeout occured check responses')
            search_phrase = message.data['phrase']
            if search_phrase in self.query_extensions:
                self.query_extensions[search_phrase] = []
            self.enclosure.mouth_reset()

            # Look at any replies that arrived before the timeout
            # Find response(s) with the highest confidence
            best = None
            ties = []
            if search_phrase in self.query_replies:
                for handler in self.query_replies[search_phrase]:
                    if not best or handler['conf'] > best['conf']:
                        best = handler
                        ties = []
                    elif handler['conf'] == best['conf']:
                        ties.append(handler)

            if best:
                if ties:
                    # TODO: Ask user to pick between ties or do it automagically
                    pass

                # invoke best match
                self.speak(best['answer'])
                self.log.info('Handling with: ' + str(best['skill_id']))
                self.bus.emit(message.forward('question:action',
                                      data={'skill_id': best['skill_id'],
                                            'phrase': search_phrase,
                                            'callback_data':
                                            best.get('callback_data')}))
                self.answered = True
            else:
                self.answered = False
            self.waiting = False
            if search_phrase in self.query_replies:
                del self.query_replies[search_phrase]
            if search_phrase in self.query_extensions:
                del self.query_extensions[search_phrase]


def create_skill():
    return TestSkill()
