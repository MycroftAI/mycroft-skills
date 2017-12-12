# Mycroft Skills Repo
![logo](https://avatars1.githubusercontent.com/u/14171097?v=4&s=200 "Logo")

# Content
- [Welcome](#welcome)
  - [Available Skills](#available-skills)
  - [How to Submit a Skill](#how-to-submit-a-skill)
    - [1) Make a Repo](#1-make-a-repo)
    - [2) Clone Repo](#2-clone-repo)
    - [3) Generate Readme](#3-generate-readme)
    - [4) Add Submodule](#4-add-submodule)
    - [5) Modify Skills Repo README.md](#5-modify-skills-repo-readmemd)
    - [6) Submit PR (Pull Request)](#6-submit-pr-pull-request)
    - [MSM Compliance](#msm-compliance)
  - [Community Contributed Skill List](#community-contributed-skill-list)


# Welcome

The Skills Repo is the official home of skills for the Mycroft ecosystem.  These skills are written by both the MycroftAI team and others within the Community.


**You can visit the new HTML version of this document at https://mycroftai.github.io/mycroft-skills/**

## Available Skills

|      Skill Name                                              |                Description<br>"handled phrases"                      |                                           
| -------------------------------------------------------------| ---------------------------------------------------------------------|
|[AIML Fallback](https://github.com/forslund/fallback-aiml#readme)|          AIML skill by JarbasAI                                   |
|[Alarm](https://github.com/MycroftAI/skill-alarm#readme)             |          Alarm                                                       |
|[Audio Record](https://github.com/MycroftAI/skill-audio-record#readme)|         Record and Play Audio<br>```"record"```                       |
|[Configuration](https://github.com/mycroftai/skill-configuration#readme)|       Update Mycroft configuration<br>```"configuration update"```  |
|[Date Time](https://github.com/MycroftAI/skill-date-time#readme)     |          Tell the date or time<br> ```"what time is it"```             |
|[Desktop Launcher](https://github.com/MycroftAI/skill-desktop-launcher#readme)| Open Applications on Desktop<br>```"open firefox"```          |
|[DuckDuckGo](https://github.com/MycroftAI/fallback-duckduckgo#readme)| Query DuckDuckGo's Instant Answer API for general questions<br> ```"what is frankenstein"```|
|[Hello World](https://github.com/mycroftai/skill-hello-world#readme) | Hello world and Mycroft manners<br> ```"how are you"```                |
|[IP](https://github.com/MycroftAI/skill-ip#readme)                   | Check the device's IP Address<br> ```"what is your ip address"```      |
|[Joke](https://github.com/MycroftAI/skill-joke#readme)               | Tell jokes<br> ```"tell me a joke"```                                  |
|[Installer](https://github.com/mycroftai/skill-installer#readme)     | Install skills<br> ```"install daily meditation"```<br>```"uninstall skill daily meditation"``` |
|[Mark-1 Demo](https://github.com/MycroftAI/skill-mark1-demo#readme)  | Demonstration of Mark 1                                              |
|[Naptime](https://github.com/mycroftai/skill-naptime#readme)         | Put Mycroft to sleep<br>```"go to sleep"```                          |
|[NPR News](https://github.com/MycroftAI/skill-npr-news#readme)       | Listen to the news from NPR<br>```"what's the latest news"```    |
|[Pairing](https://github.com/mycroftai/skill-pairing#readme)         | Pair Mycroft with home.mycroft.ai<br>```"pair my device"```          |
|[Personal](https://github.com/MycroftAI/skill-personal#readme)       | Learn about Mycroft<br>```"what are you"```                          |
|[Playback Control](https://github.com/mycroftai/skill-playback-control#readme)| Control audio subsystem<br>```"play", "pause", "next" ```                     |
|[Reminder](https://github.com/MycroftAI/skill-reminder#readme)       | Reminders to do something<br>```"remind me to turn off the oven in 5 minutes"```                                                                                                                           |
|[Speak](https://github.com/MycroftAI/skill-speak#readme)             | Repeat anything<br>```"say open source AI"```                        |
|[Singing](https://github.com/MycroftAI/skill-singing#readme)         | Sing some Songs<br>```"sing a song"```                               |
|[Stock](https://github.com/MycroftAI/skill-stock#readme)             | Stock prices<br>```"what is the stock price of Autodesk"```                        |
|[Stop](https://github.com/mycroftai/skill-stop#readme)               | Stop running skills<br>```"stop"```                                  |
|[Unknown Fallback](https://github.com/mycroftai/fallback-unknown#readme)| When Mycroft doesn't know an answer or understand a command<br>```"green jelly wood"```   |
|[Version Checker](https://github.com/MycroftAI/skill-version-checker#readme)| Find the version of mycroft-core<br>```"check version"```     |
|[Volume](https://github.com/mycroftai/skill-volume#readme)           | Control Volume<br>```"turn up the volume", "mute audio"```         |
|[Weather](https://github.com/MycroftAI/skill-weather#readme)         | Current Weather and Forecasts<br>```"what is the weather"```         |
|[Wiki](https://github.com/MycroftAI/skill-wiki#readme)               | Wikipedia queries<br>```"tell me about AI"```                        |
|[Platform Patch](https://github.com/MycroftAI/skill-platform-patch#readme)| Patching for official platforms<br>```"platform patch"```       |

| [Mark 1 settings](https://github.com/MycroftAI/mycroft-mark-1) | Control your Mark 1 enclosure<br>```change eye color to red``` |


## How to Submit a Skill

### 1) Make a Repo
Create the skill in a repo under your own Github user account.  You can follow the guide at [How To Make a Repo](https://help.github.com/articles/create-a-repo/), or use the [skiller.sh script](https://github.com/MycroftAI/mycroft-core/blob/dev/skiller.sh).

### 2) Clone Repo
Clone the mycroft-skills repo to a local directory, [How To Clone](https://help.github.com/articles/cloning-a-repository) if you are unfamiliar with the process.

```git clone https://github.com/MycroftAI/mycroft-skills.git```

### 3) Generate the README.md
All skills must have a standard README.md.  You can use the [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html) to create it.

### 4) Add your Skill as a submodule
Add the your skill to this repo as a submodule. For more help, feel free to check out [this guide](https://github.com/blog/2104-working-with-submodules)

Or, type the following in the terminal of your clone of the Skills-repo.
```
git submodule add $remote $name-of-your-skill
```
Where $remote is the git address for your repo (example https://github.com/mycroftai/skill-configuration) and $name-your-skill is what you want to name it. In general, we normally use BLANK-skill as a format for skill names.

This should have edited the .gitmodule file and added something similar to the bottom of the file:
```
+[submodule "NAME-OF-YOUR-SKILL"]
 +	path = YOUR-SKILL-REPO (or any path unique to this repo)
 +	url = https://github.com/USERNAME/YOUR-SKILL-REPO.git
```

```NAME-OF-YOUR-SKILL```

This name is used to install via MSM and verbally.  Users install by speaking sufficient portions of this name to be unique.  For example "mycroft-mark-1-demo" would install if a user only said "install mark 1 demo" -- assuming there is no other skill that matches this queury, such as "another mark 1 demo".

We recommend starting your name with a name or organization name that makes it unique.

### 5) Modify Skills Repo README.md
Modify the table section to include the direct link to your repo like the following example including the break tag and the phrase to trigger your skill:

```
| :heavy_check_mark:  | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)| Control your devices in home-assistant<br>```turn on office```

``````
Ensure to put a proper status as well from the list below:

**Status meaning:**  
:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!

### 6) Submit a PR (Pull Request)
Once you've got your local version of the repo organized properly, submit a PR.

### MSM Compliance
To make your skill capable of being installed via MSM (the Mycroft Skill Manager) you can include two additional files.

> requirements.txt
A list of Python modules to be installed via the Python PIP utility

> requirements.sh
A script to run that will perform any additional steps needed by your skill.  This can include package installations.


**Status meaning:**  
:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!


For an example pull request , check out [this PR](https://github.com/MycroftAI/mycroft-skills/pull/37)

## Community Contributed Skill List
**When submitting a skill make sure skill name links to the location of the skill, we are doing away with the wiki pages.  Also please include the phrase to trigger on as well for your skill.**


| Status              | Skill Name                                                     | Description<br>```"phrase to trigger"```    |
| ------------------- | -------------------------------------------------------------- | --------------------------------------------|
| :heavy_check_mark:  | [Australian news](https://github.com/KathyReid/skill-australian-news/README.md)	| Skill for playing ABC news from Australia<br />```"Play Australian news"```|
| :heavy_check_mark:  | [AutoGUI skill](../../wiki/SKILL-Autogui)                      | Manipulate your mouse and keyboard with Mycroft                                                  |
| :heavy_check_mark:  | [Basic help](https://github.com/btotharye/mycroft-skill-basichelp#readme)| Get basic mycroft questions and help answered<br>```"where is the documentation", "how do I install from source"```         |
| :heavy_check_mark:  | [Caffeine Wiz](https://github.com/reginaneon/skill-caffeinewiz.git)| Provides the caffeine content of various drinks on request.<br>```what's caffeine content of *drink*?``` |
| :heavy_check_mark:          | [Coin flip](../../wiki/SKILL-coin-flip)        | Flip a virtual coin   |
| :heavy_check_mark:  | [Deutschland Funk](https://github.com/ofosos/deutschlandfunk-skill)| Listen to Deutschlandfunk and query schedule
| :heavy_check_mark:  | [Home Assistant](https://github.com/btotharye/mycroft-homeassistant#readme)| Control your devices in home-assistant<br>```"turn on office"```                                                      |  
| :heavy_check_mark:          | [Pandora](../../wiki/SKILL-pandora)                   | Play Pandora stations via Pianobar  |
| :heavy_check_mark:          | [Ping](../../wiki/SKILL-ping)  | Pings websites and responds with latency time       |  
| :heavy_check_mark:  | [Radio RNE](../..wiki/SKILL-radio-rne)       | Spanish news radio Radio Nacional de Espa?a RNE. |
| :heavy_check_mark:  | [Timer](https://github.com/MycroftAI/mycroft-timer.git)| Set a timer on your device<br>```set a timer for 30 minutes```
| :heavy_check_mark:  | [Internet Radio](https://github.com/normandmickey/skill-internet-radio#readme)| Listen to Internet Radio<br>```internet radio``` |
| :question:          |[Amarok media player control](https://github.com/AIIX/amarok-player-skill#readme)               | Player controls for the Amarok Media Player<br>```"amarok play/stop/next/previous music"``` |
| :question:         | [Angry Beanie podcast](https://github.com/purserj/mycroft-angrybeanie#readme)         | Skill for querying and playing Angry Beanie Podcasts<br />```"Get Angry Beanie shows"``` |
| :question:  | [Plasma audio control](https://github.com/AIIX/audio-control-plasma#readme)| Audio control for Plasma Desktop<br>```"increase volume to maximum", "decrease microphone to minimum volume"```         |
| :question:          |[bioinformatics](../../wiki/SKILL-bioinformatics)               | Adds Bio-Linux Commands to Mycroft   |  
| :question:          | [bitcoin](../../wiki/SKILL-bitcoin)                            | Check the price of bitcoin                                                               |  
| :construction:      | [bitcoin-price](../../wiki/SKILL-bitcoin-price)                |  Checks the price of bitcoin                             |
| :construction:      | [brain-skill](../../wiki/SKILL-brain)                          |  Chain intents and provide some services                                                 |
| :construction:  | [skill-calculator](https://github.com/TREE-Edu/calculator-skill.git)| Provides a conversational based calculator.<br>```Do some math```
| :question:          | [cbc-news-skill](../../wiki/SKILL-cbc-news)        | Fetches CBC News Podcast             |  
| :question:          | [clarifai-image-recognition-skill](https://github.com/AIIX/clarifai-image-recognition-skill#readme)      | Image recognition skill based on clarifai<br> ```"search image url [imagelocation]"```   |
| :question:          | [clementine-player-skill](../../wiki/SKILL-clementine-player)  | Controls your clementine-player localy. A fork from amarok-player.   |
| :question:          | [cleverbot-skill](../../wiki/SKILL-cleverbot)        | cleverbot api fallback skill   |
| :question:          | [daily-meditation](../../wiki/SKILL-daily-meditation)          |Plays your Daily Meditation from the  Meditation Podcast     |
| :construction:      | [deepdream_skill](../../wiki/SKILL-deepdream)                  | Adds Deepdreaming image converstion to Mycroft       |
| :question:         | [diagnostics](../../wiki/SKILL-diagnostics)                    | Diagnostic tools (CPU %age, free space, etc)    |
| :construction:      | [dice-roll](../../wiki/SKILL-dice)                             | Rolls dice spoken in RPG notation.                                                       |
| :question:          | [domoticz_skill](../../wiki/SKILL-domoticz)                    | Skill integrating Mycroft with Domoticz    |
| :question:          | [drive_servos](../../wiki/SKILL-drive-servos)                  | Control Hacked-Servo-Engines to make your mycroft move around   |
| :question:          | [earth-orbit-pic-skill](../../wiki/SKILL-earth-orbit-pic)      | Earth orbit picture skill   |
| :skull:             | [enhanced-bitcoin-skill](../../wiki/SKILL-enhanced-bitcoin)  | Enhanced bitcoin skill from api.bitcoinaverage.com        |
| :construction:      | [facebook](../../wiki/SKILL-facebook)                          | Generates posts for Facebook                  |
| :construction:      | [facebook-marketing](../../wiki/SKILL-facebook-marketing)      | Works with Facebook Marketing API                                                        |
| :question:          | [feedback-skill](../../wiki/SKILL-feedback)                    | triggers positive feedback intent -> calls feedback method on last active skill          |  
| :question:          | [fox-news-skill](../../wiki/SKILL-fox-news)                    | Fetches Fox News Podcast                                                                 |
| :question:          | [google-calendar](../../wiki/SKILL-google-calendar)            | Check and add google calendar events                                                     |  
| :question:          | [google-gmail](../../wiki/SKILL-google-gmail)                  | Get emails from your Gmail Inbox                                                         |  
| :question:          | [google-image-search](../../wiki/SKILl-google-image-search)    | Search google images for search term and display                                         |
| :question:          | [google-translate](../../wiki/SKILL-google-translate)          | Translate English phrases into other languages                                           |
| :construction:  | [gpio-example](../../wiki/SKILL-gpio-example)                            | Example skill using the GPIO pins on the Raspberry Pi to blink an LED                                         |    
| :question:          | [hue](../../wiki/SKILL-hue)                                    | Control your Phillips Hue lights                                                         |  
| :question:          | [irsend](../../wiki/SKILL-irsend)                              | Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| :question:          | [jb-podcasts](../../wiki/SKILL-Jupiter-Broadcasting-Podcasts)  | Play podcasts from Jupiter Broadcasting shows                                            |  
| :question:          | [kde-kate-control](https://github.com/AIIX/kde-kate-control#readme) | Kate Editor control skill <br>```"new document, close document, goto next/previous tabs/views"```                  |
| :question:          | [krunner-search](https://github.com/AIIX/krunner-search-skill#readme) | Search local KDE desktop for files, images, recent documents, bookmarks<br>```"search this computer for [any keyword]"```                  |
| :question:          | [kodi-cadair](../../wiki/SKILL-cadair-kodi)                    | Kodi playback and search                                                                 |  
| :question:          | [kodi-cbenning](../../wiki/SKILL-cbenning-kodi)                | Control a local or remote Kodi instance                                                  |  
| :question:          | [kodi-k3yb0ardn1nja](../../wiki/SKILL-kodi-k3yb0ardn1nja)      | Play or pause a Kodi video                                                               |  
| :question:          | [let's-talk-skill](../../wiki/SKILL-lets-talk)                 | More salutations |
| :question:          | [lottery-skill](../../wiki/SKILL-lottery)                      | Reads Euromillion Lottery Numbers     |
| :question:          | [media-console-control](../../wiki/SKILL-media-console-control)| Adds media controls that are mapped to console commands                                  |  
| :question:          | [metal-band-skill](../../wiki/SKILL-metal-band)                | Recommends a metal band and gives basic information    |
| :construction:      | [milight](../../wiki/SKILL-milight)                            | Lighting control using MiLight                                                           |  
| :question:          | [mopidy](../../wiki/SKILL-mopidy)                              | Mopidy-based players for local music, Google Music, and Spotify                          |  
| :construction:      | [mopidy-and-bt-lights](../../wiki/SKILL-mopidy-and-bt-lights)  | Remote control of BT lights and Mopidy music playback                                    |  
| :question:          | [mopidy-media-player](../../wiki/SKILL-Mopidy-Media-Players)   | Mopidy-based players for local MP3 library, Spotify and a Swedish radio station's stream |
| :question:          | [movie-recommendation-skill](../../wiki/SKILL-movie-recomentation)                        | Recomends a movie  |
| :question:          | [mpd-control](../../wiki/SKILL-mpd-control)                    | Controls media players that use the MPD  protocol to play found local music           |  
| :question:          | [mqtt](../../wiki/SKILL-mqtt)                        | Control IoT devices (home automation) using MQTT protocol     |  
| :question:          | [mute-skill](../../wiki/SKILL-mute)            | Mutes Mycroft until re-enabled |
| :question:          | [nasa-picture-of-the-day](../../wiki/SKILL-nasa-pic-of-the-day)                    | Nasa picture of the day from the NASA API |
| :question:          | [near-earth-orbit-skill](../../wiki/SKILL-near-earth-orbit)                    | Near Earth orbit alert skill via the NASA API   |
| :construction:	  | [objective-skill](../../wiki/SKILL-objective)                  | skills can now register objectives almost the same has an intent would be registered with ObjectiveBuilder class              |
| :construction:	  |	[openhab-skill](../../wiki/SKILL-Openhab)					| This skill adds Openhab support to Mycroft |
| :question:          | [photolocation-skill](../../wiki/SKILL-photolocation)          | Searches wikimedia for photos of location  |
| :question:          | [pickup-line-skill](../../wiki/SKILL-pickup-line)  | Responds with random nerdy pick-up lines          |
| :question:          | [plasma-activities-skill](https://github.com/AIIX/plasma-activities-skill#readme)  | This skill integrates Plasma 5 Activities with Mycroft<br>```"show activities / switch activity [name]"```|
| :question:          | [plasma-mycroftplasmoid-control](https://github.com/AIIX/plasma-mycroftplasmoid-control#readme)  | This skill lets you control the Mycroft Plasmoid<br>```"show mycroft applet / display skills page"```|
| :question:          | [plasma-sendsms-skill](https://github.com/AIIX/plasma-sendsms-skill#readme)         |Send SMS through KDE Plasma<br>```"send a sms"```     |
| :question:          | [plasma-user-control-skill](https://github.com/AIIX/plasma-user-control-skill#readme) | This skills adds Plasma User control to Mycroft, allowing switch user, logout, and lock screen<br>```"switch user/logout/lock screen"```  |
| :question:          | [poetry-skill](../../wiki/SKILL-poetry)                      | Reads poetry based on Hidden Markov Models     |
| :question:          | [proxy-scrape-skill](../../wiki/SKILL-proxy-scrape)          | Scrape proxies from the internet    |
| :question:          | [pushbullet](../../wiki/SKILL-pushbullet)                      | Send messsages and photos using Pushbullet                                                  |  
| :question:          | [pushetta-skill](../../wiki/SKILL-pushetta)                    | Adds push notifications|
| :question:          | [quodlibet](../../wiki/SKILL-quodlibet)                        | Control Quod Libet music playback                                                        |  
| :question:          | [random-quote-skill](../../wiki/SKILL-random-quote)            | Adds random quotes,random facts about numbers, and your time left to live          |
| :question:          | [ratp-timetables](../../wiki/SKILL-ratp-timetables)            | Access schedules for the RATP Network of trains and buses in Paris                       |  
| :construction:      | [read-article-skill](../../wiki/SKILL-read-article)            | Scrapes text from online articles and reads them to you.   |
| :question:          | [rss-skill](../../wiki/SKILL-rss)            | Fetches from RSS feed   |
| :construction:      | [sentiment-analysis-skill](../../wiki/SKILL-sentiment-analysis)  | Sentiment analysis              |
| :question:          | [spaceflight-schedule](../../wiki/SKILL-spaceflight-schedule)  | Check when the next space flight launch is                                               |
| :question:          | [spacelaunch-skill](../../wiki/SKILL-spacelaunch)  | Check when the next space launch is                                               |
| :question:          | [speedtest](../../wiki/SKILL-speedtest)  | Run a speedtest                                               |
| :question:          | [slack-skill](../../wiki/SKILL-slack)                          | Allows to post and listen to Slack messages.  |
| :question:          | [sunspot-skill](../../wiki/SKILL-sunspot-skill)                    | Answers questions on daily sunspots |
| :question:          | [sun-skill](../../wiki/SKILL-sun)  | Responds with sunrise and set times          |  
| :question:          |[system-skill](../../wiki/SKILL-system)               | Adds system controls like shutdown and reboot   |
| :question:          | [take_picture](../../wiki/SKILL-take-picture)  | Take Pictures using the Raspberry Pi Camera          |  
| :construction:      | [the-cows-lists-skill](https://github.com/CarstenAgerskov/skill-the-cows-lists#readme)  | This skill adds "Remember The Milk" support to Mycroft.<br>```"add milk to my grocery list"```    |
| :question:          | [traffic-skill](../../wiki/SKILL-traffic)  | Gets the commute time from Google distance matrix api         |  
| :question:          | [unsplash-wallpaper-plasma-skill](https://github.com/AIIX/unsplash-wallpaper-plasma-skill#readme)  | Change KDE Desktop wallpaper by category type from unsplash<br>```"change wallpaper type [nature\abstract\any]"``` |
| :construction:      | [wallpaper-skill](../../wiki/SKILL-wallpaper)  | Downloads wallpapers from reddit and changes randomly         |
| :question:	      | [wemo-skill](../../wiki/SKILL-wemo)              | Control Wemo devices with mycroft                                                   |
| :construction:      | [wifi-management-skill](../../wiki/SKILL-wifi-management)  | Various options for interacting with WiFi        |
| :question:          | [wiki-fact-scraper-skill](../../wiki/SKILL-wiki-fact-scraper)                        | Scrapes for random facts from wikipedia and stores locally    |
| :question:  | [youtube](../../wiki/SKILL-youtube)                            | Search and listen to a youtube video                                                        |  
| :question:  | [release-test](../../wiki/SKILL-release-test)                            | test mycroft release                                                        |  


