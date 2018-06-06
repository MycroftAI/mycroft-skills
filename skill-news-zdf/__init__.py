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


class ZdfSkill(MycroftSkill):
    def __init__(self):
        super(ZdfSkill, self).__init__(name="ZdfSkill")
        self.process = None

    def initialize(self):
        intent = IntentBuilder("ZdfIntent").require(
                "ZdfKeyword").optionally("ZdfJournalKeyword").build()
        self.register_intent(intent, self.handle_intent)


    def handle_intent(self, message):
        try:
            zdfjournal = message.data.get('ZdfJournalKeyword')
            if zdfjournal:
                data = feedparser.parse("http://www.zdf.de/rss/podcast/audio/zdf/nachrichten/heute-journal")
            else:
                data = feedparser.parse("http://www.zdf.de/rss/podcast/audio/zdf/nachrichten/heute-19-uhr")
                self.speak_dialog('zdf.news')
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
    return ZdfSkill()
