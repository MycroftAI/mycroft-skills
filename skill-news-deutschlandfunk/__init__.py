
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# http://api.rtve.es/api/programas/1750/audios.rss
# http://api.rtve.es/api/programas/36019/audios.rss

import feedparser
import time
from os.path import dirname
import re

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util import play_mp3
from mycroft.util.log import getLogger

__author__ = 'laaky'

LOGGER = getLogger(__name__)


class DeutschlandfunkSkill(MycroftSkill):
    def __init__(self):
        super(DeutschlandfunkSkill, self).__init__(name="DeutschlandfunkSkill")
        self.process = None

    def initialize(self):
        intent = IntentBuilder("DeutschlandfunkIntent").require(
                "DeutschlandfunkKeyword").build()
        self.register_intent(intent, self.handle_intent)


    def handle_intent(self, message):
        try:

            data = feedparser.parse("http://www.deutschlandfunk.de/podcast-nachrichten.1257.de.podcast.xml")
            self.speak_dialog('deutschlandfunk.news')
            time.sleep(5)

            self.process = play_mp3(
                re.sub(
                    'https', 'http', data['entries'][0]['enclosures'][0]['href']))

        except Exception as e:
            LOGGER.error("Error: {0}".format(e))


    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()


def create_skill():
    return DeutschlandfunkSkill()
