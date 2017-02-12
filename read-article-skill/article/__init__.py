
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import newspaper
import random
import re
import webbrowser

__author__ = 'jarbas'

logger = getLogger(__name__)


class ArticleSkill(MycroftSkill):

    def __init__(self):
        super(ArticleSkill, self).__init__(name="ArticleSkill")

        self.newssauce = []
        self.memorize = True
        self.news = None
        self.defaulturls = False
        self.language = "en"

        path = dirname(__file__) + '/newssauce.txt'
        with open(path) as f:
            links = re.sub(" ", "", f.read()).lower().split('\n')
        for link in links:
            self.newssauce.append(link)

        if self.defaulturls:
            for link in newspaper.popular_urls():
                self.newssauce.append(link)

        f.close()

    def initialize(self):
        self.load_data_files(dirname(__file__))

        ###to do
        # intents to open article link
        # intents for individual sauces
        # write vocabulary
        # make article summarys for reading
        # article keyword analisys / entropy update

        article_intent = IntentBuilder("ArticleIntent") \
            .require("article").build()
        self.register_intent(article_intent,
                             self.handle_article_intent)

        show_article_intent = IntentBuilder("ShowArticleIntent") \
            .require("showarticle").build()
        self.register_intent(show_article_intent,
                             self.handle_show_article_intent)

    def getnews(self):

        i = 0
        while i <15:
            sauce = random.choice(self.newssauce)
            ########## this always throws an exception by default that can be safely ignored, however that means we get infinite retrys here
            ########## TypeError: not all arguments converted during string formatting
            ########## need to handle exception better, what exeption is thrown when invalid url?
            try:
                self.news = newspaper.build(sauce, memoize_articles=self.memorize, language=self.language, fetch_images=False)
                logger.info("number of articles found: " + str(self.news.size()))
                i = 20
                if self.news.size() == 0:
                    i = 0
                    logger.error("no articles found, trying new sauce")

            except:
                logger.error("error, bad source link: "+ sauce)
                i+=1
                logger.error("retrying: " + str(i))
                if i > 10:
                    logger.error("check newssauce.txt , could only find invalid urls")

    def handle_article_intent(self, message):
        self.getnews()
        text = "I've been reading " + self.news.brand + "\n\n"
        i=0
        while i<5:
            try:
                # print cnn_paper.feed_urls()
                article = random.choice(self.news.articles)
                article.download()
                article.parse()
                logger.info( "reading "+article.title)
                ###check for 404
                i = 0
                while ("the page you are looking for has not been found" or "404") in article.text:
                    article = random.choice(self.news.articles)
                    i += 1
                    if i > 10:
                        logger.error("404 limit, trying new category")
                        self.getnews()  # get new source
                    if i > 20:
                        logger.error("getting too much 404's, aborting")
                        return

                #if article.summary != ("" or " " or "\n"):
                    # print article.text
                #    text += "\n" + article.summary
                #else:
                    # print article.summary
                text += "\n" + article.text

                text += "\n\nsource: " + article.url
                text += "\n\ndate: " + str(article.publish_date)
                #process text
                text.replace("Read More","")
                text.replace("Comment this news or article", "")
                text.replace("Photo", "")
                self.speak(text)
                i = 6
            except:
                logger.error("trying next article")
                i+=1
                if i >= 5:
                    logger.error(" bad article source")

    def handle_show_article_intent(self, message):
        self.getnews()
        i=0
        while i<5:
            try:
                article = random.choice(self.news.articles)
                ###check for 404
                i = 0
                while i==0 or ("the page you are looking for has not been found" or "404") in article.text:
                    article = random.choice(self.news.articles)
                    i += 1
                    if i > 10:
                        logger.error("404 limit, trying new category")
                        self.getnews() #get new source
                    if i > 20:
                        logger.error("getting too much 404's, aborting")
                        return
                #####
                i=6
                logger.info("opening " + article.url)
                webbrowser.open(article.url)
            except:
                i+=1
                logger.error("error, trying next article")
                if i >= 5:
                    logger.error("error, bad article source")

    def stop(self):
        pass


def create_skill():
    return ArticleSkill()
