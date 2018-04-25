# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

import sys
import requests
import html5lib
from titlecase import titlecase
from bs4 import BeautifulSoup
from adapt.intent import IntentBuilder
import re
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

headers = {'User-Agent':'Mozilla/5.0'}

cstatus = ""
coverview = ""
fullcountry = ""

# TODO: Change "Template" to a unique name for your skill
class CivicusMonitorSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(CivicusMonitorSkill, self).__init__(name="CivicusMonitorSkill")

    @intent_handler(IntentBuilder("").require("Monitor"))
    def handle_civicus_monitor(self,message):

        # Remove everything up to the speak keyword and repeat that
        utterance = message.data.get('utterance')
        country = re.sub('^.*?' + message.data['Monitor'], '', utterance)
        CountryProcessor(country)

        self.speak(cstatus)
        self.speak(coverview)

        global cstatus
        cstatus = ""
        global coverview
        coverview = ""


        #self.speak_dialog("monitor-speak")
        #self.log.debug("test")

def create_skill():
    return CivicusMonitorSkill()

def CountryProcessor(query): #find the right URL for the country in question
    fullcountry = query  #preserve the country with the "the" for speaking later.
    query = query.lower().replace('the ', '').replace('of ','').replace('for ','').lstrip()

    if query == "antigua and barbuda" or query == "antigua" or query == "barbuda":
        country = "antigua-and-barbuda"
    elif query == "boznia and herzegovina" or query == "bosnia" or query == "herzegovina":
        country = "bosnia-herzegovina"
    elif query == "brunei darusallam" or query == "brunei" or query == "darusallam":
        country = "brunei-darusallam"
    elif query == "burkina faso":
        country = "burkina-faso"
    elif query == "cape verde":
        country = "cape-verde"
    elif query == "central african republic" or query == "car":
        country = "central-african-republic"
    elif query == "costa rica":
        country = "costa-rica"
    elif query == "cote d'ivoire":
        country = "cote-divoire"
    elif query == "czech republic":
        country = "czech-republic"
    elif query == "democratic republic of congo" or query == "drc":
        country = "democratic-republic-congo"
    elif query == "dominican republic":
        country = "dominican-republic"
    elif query == "el salvador":
        country = "el-salvador"
    elif query == "equatorial guinea" or query == "guinea":
        country = "equatorial-guinea"
    elif query == "guinea bissau":
        country = "guinea-bissau"
    elif query == "marshall islands":
        country = "marshall-islands"
    elif query == "new zealand":
        country = "new-zealand"
    elif query == "north korea":
        country = "north-korea"
    elif query == "papua new guinea":
        country = "papua-new-guinea"
    elif query == "republic of congo":
        country = "republicofthecongo"
    elif query == "saint lucia":
        country = "saint-lucia"
    elif query == "san marino":
        country = "san-marino"
    elif query == "sao tome and principe" or query == "sao tome" or query == "principe":
        country ="sao-tome-and-principe"
    elif query == "saudi arabia" or query == "saudi":
        country = "saudi-arabia"
    elif query == "sierra leone":
        country = "sierra-leone"
    elif query == "solomon islands":
        country = "solomon-islands"
    elif query == "south africa":
        country = "south-africa"
    elif query == "south korea":
        country = "south-korea"
    elif query == "south sudan":
        country = "south-sudan"
    elif query == "sri lanka":
        country = "sri-lanka"
    elif query == "saint kitts and nevis" or query == "saint kitts":
        country = "st-kitts-and-nevis"
    elif query == "saint vincent and grenadines" or query == "saint vincent":
        country = "st-vincent-and-grenadines"
    elif query == "timor leste":
        country = "timor-leste"
    elif query == "trinidad and tabago" or query == "trinidad" or query == "tabago":
        country = "trinidad-and-tabago"
    elif query == "uae" or query == "united arab emirates":
        country = "united-arab-emirates"
    elif query == "united kingdom" or query == "u k" or query == "u.k." or query == "uk":
        country = "united-kingdom"
    elif query == "united states of america" or query == "united states" or query == "u s" or query == "america" or query == "u.s." or query == "us":
        country = "united-states-america"
    else:
        country = query

    #print ("country is "+country)
    QueryPage(fullcountry, country,query)

def QueryPage(fullcountry, countryurl,country):
    url = "https://monitor.civicus.org/country/"+countryurl
    print(url)
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        country = titlecase(country)


        status = soup.find('div', attrs={'class':'intro'}).get_text().split()[2]
        print(status)

        global coverview
        coverview = soup.find('div', attrs={'class':'half'}).find('p').get_text()

        global cstatus
        cstatus = ("The civic space level of "+fullcountry+ " is "+status)


    except:
        print("search failed!")
        cstatus = "I don't understand."