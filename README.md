# Welcome :package:
A repository for sharing and collaboration for third-party Mycroft skills  
development.  This is a place to publish complete Skills and learn Skill  
writing as well as share best practices.

## Table of Contents
- [Mycroft Skills :package:](#mycroft-skills-package)
  - [How to Add Skills to the Repo!](#how-to-add-skills-to-the-repo)
    - [MSM Compliance](#msm-compliance)
  - [Official Skill List](#official-skill-list)
  - [Community Contributed Skill List](#community-contributed-skill-list)

## Default Skills and Triggering Them

|      Skill Name                                              |                Description<br>"handled phrases"                      |                                           
| -------------------------------------------------------------| ---------------------------------------------------------------------|
|[AIML Fallback](https://github.com/forslund/fallback-aiml)    |          AIML skill by JarbasAI                                      |
|[Alarm](https://github.com/MycroftAI/skill-alarm)             |          Alarm                                                       |
|[Audio Record](https://github.com/MycroftAI/skill-audio-record)|         Record and Play Audio<br>```record```                       |
|[Configuration](https://github.com/mycroftai/skill-configuration)|       Update Mycroft configuration<br>```configuration update```  |
|[Date Time](https://github.com/MycroftAI/skill-date-time)     |          Tell the date or time<br> ```what time is it```             |
|[Desktop Launcher](https://github.com/MycroftAI/skill-desktop-launcher)| Open Applications on Desktop<br>```open firefox```          |
|[Hello World](https://github.com/mycroftai/skill-hello-world) | Hello world and Mycroft manners<br> ```how are you```                |
|[IP](https://github.com/MycroftAI/skill-ip)                   | Check the device's IP Address<br> ```what is your ip address```      |
|[Joke](https://github.com/MycroftAI/skill-joke)               | Tell jokes<br> ```tell me a joke```                                  |
|[Installer](https://github.com/mycroftai/skill-installer)     | Install skills<br> ```install daily meditation```<br>```uninstall skill```                                                                                                                              |
|[Mark-1 Demo](https://github.com/MycroftAI/skill-mark1-demo)   | Demonstration of Mark 1                                             |
|[Media](https://github.com/MycroftAI/skill-media)             | Multimedia Control<br>```play, pause, next track```                  |
|[Naptime](https://github.com/mycroftai/skill-naptime)         | Put Mycroft to sleep<br>```go to sleep```                            |
|[NPR News](https://github.com/MycroftAI/skill-npr-news)       | Listen to the news from NPR<br>```news```<br>```stop news```         |
|[Pairing](https://github.com/mycroftai/skill-pairing)         | Pair Mycroft with home.mycroft.ai<br>```pair my device```            |
|[Personal](https://github.com/MycroftAI/skill-personal)       | Learn about Mycroft<br>```what are you```                            |
|[Playback Control](https://github.com/mycroftai/skill-playback-control)| Control audio subsystem<br>```play```                       |
|[Reminder](https://github.com/MycroftAI/skill-reminder)       | Reminders to do something<br>```remind me to turn off the oven in 5 minutes```                                                                                                                            |
|[Speak](https://github.com/MycroftAI/skill-speak)             | Repeat anything<br>```sya open source AI```                          |
|[Singing](https://github.com/MycroftAI/skill-singing)         | Sing some Songs<br>```sing a song```                                 |
|[Stock](https://github.com/MycroftAI/skill-stock)             | Stock prices<br>```stock price of google```                          |
|[Stop](https://github.com/mycroftai/skill-stop)               | Stop running skills<br>```stop```                                    |
|[Volume](https://github.com/mycroftai/skill-volume)           | Increases or Decreases/Mutes Volume<br>```reduce volume```           |
|[Weather](https://github.com/MycroftAI/skill-weather)         | Current Weather and Forecasts<br>```what is the weather```           |
|[Wiki](https://github.com/MycroftAI/skill-wiki)               | Wikipedia queries<br>```tell me about AI```                          |
|[Platform Patch](https://github.com/MycroftAI/skill-platform-patch)| Patching for official platforms<br>```platform patch```         |

## How to Add Skills to the Repo!

### Step 1 Make a Repo
If you want to submit a skill, simply make a repo for it organized   
as the template above. [How To Make a Repo](https://help.github.com/articles/create-a-repo/)

[Example Skill Template](https://github.com/MycroftAI/mycroft-skills/tree/master/00__skill_template)  

### Step 2 Clone Repo
Clone the mycroft-skills repo to a local directory, [How To Clone](https://help.github.com/articles/cloning-a-repository) if you are unfamiliar with the process.

### Step 3 Generate Readme
To get the skill added, generate the Readme file using the [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html) You will fill out all the relative fields and it will give you the Markdown to put into your README.md file.

### Step 4 Add Submodule
Next we need to add the submodule for your skill. For more help, feel free to check out [this guide](https://github.com/blog/2104-working-with-submodules)

Or, type the following in the terminal of your clone of the Skills-repo.
```
git submodule add $remote $name-your-skill
```
Where $remote is the git address for your repo (example https://github.com/mycroftai/skill-configuration) and $name-your-skill is what you want to name it. In general, we normally use BLANK-skill as a format for skill names.

This should have edited the .gitmodule file and added something similar to the bottom of the file:
```
+[submodule "NAME OF YOUR SKILL"]
 +	path = name-of-your-skill-skill
 +	url = URL.FOR.YOUR.SKILL.git
```

### Step 5 Submit PR (Pull Request)
Once you've got your repo organized properly, submit the PR consisting of the following:
* Ensure you use [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html) to create your standardized README.md file
* The URL of your repo
* A short name for the skill
* A one sentence description of what it does
* The development status of the skill (under construction or working)  

### MSM Compliance
To make your skill capable of being installed via MSM (the Mycroft Skill Manager) you need two additional files.
* requirements.txt
* requirements.sh
requirements.txt is a list of all pip libraries your skill needs (if any).
requirements.sh is a shell script that executes and installs package dependancies  your skill needs (if any).
So, if you need a specific pip library installed, like gensim, you can have it automatically installed in the correct vm using msm.
This requirements.txt file would look like this:
```
gensim
```
That's it!  

**Status meaning:**  
:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!


For an example pull request , check out [this PR](https://github.com/MycroftAI/mycroft-skills/pull/37)

## Community Contributed Skill List


| Status              | Skill Name                                                     | Description                                                                              |  
| ------------------- | -------------------------------------------------------------- | -------------------------------------
| :question:          |[amarok-media-player-skill](../../wiki/SKILL-amarok-media-player)               | Player controls for the Amarok Media Player |
| :heavy_check_mark:  | [autogui-skill](../../wiki/SKILL-Autogui)                      | Manipulate your mouse and keyboard with Mycroft                                                  |
| :heavy_check_mark:  | [basichelp](../../wiki/SKILL-basichelp)                        | Get basic mycroft questions and help answered                                            |
| :question:          |[bioinformatics](../../wiki/SKILL-bioinformatics)               | Adds Bio-Linux Commands to Mycroft   |  
| :question:          | [bitcoin](../../wiki/SKILL-bitcoin)                            | Check the price of bitcoin                                                               |  
| :construction:      | [bitcoin-price](../../wiki/SKILL-bitcoin-price)                |  Checks the price of bitcoin                             |
| :construction:      | [brain-skill](../../wiki/SKILL-brain)                          |  Chain intents and provide some services                                                 |
| :question:          | [cbc-news-skill](../../wiki/SKILL-cbc-news)        | Fetches CBC News Podcast             |  
| :question:          | [clarifai-image-recognition-skill](../../wiki/SKILL-clarifai-image-recognition)      | Image recognition skill based on clarifai   |
| :question:          | [clementine-player-skill](../../wiki/SKILL-clementine-player)  | Controls your clementine-player localy. A fork from amarok-player.   |
| :question:          | [cleverbot-skill](../../wiki/SKILL-cleverbot)        | cleverbot api fallback skill   |
| :heavy_check_mark:          | [coin-flip-skill](../../wiki/SKILL-coin-flip)        | Flip a virtual coin   |
| :question:          | [daily-meditation](../../wiki/SKILL-daily-meditation)          |Plays your Daily Meditation from the  Meditation Podcast     |
| :construction:      | [deepdream_skill](../../wiki/SKILL-deepdream)                  | Adds Deepdreaming image converstion to Mycroft       |
| :question:          | [diagnostics](../../wiki/SKILL-diagnostics)                    | Diagnostic tools (CPU %age, free space, etc)    |
| :construction:      | [dice-roll](../../wiki/SKILL-dice)                             | Rolls dice spoken in RPG notation.                                                       |
| :question:          | [domoticz_skill](../../wiki/SKILL-domoticz)                    | Skill integrating Mycroft with Domoticz    |
| :question:          | [drive_servos](../../wiki/SKILL-drive-servos)                  | Control Hacked-Servo-Engines to make your mycroft move around   |
| :heavy_check_mark:  | [easter-eggs](../../wiki/SKILL-easter-eggs)                    | Pop culture references and other easter eggs  |
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
| :heavy_check_mark:  | [home-assistant](../../wiki/SKILL-home-assistant)              | Control your devices in home-assistant                                                   |  
| :question:          | [irsend](../../wiki/SKILL-irsend)                              | Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| :question:          | [jb-podcasts](../../wiki/SKILL-Jupiter-Broadcasting-Podcasts)  | Play podcasts from Jupiter Broadcasting shows                                            |  
| :question:          | [krunner-search](../../wiki/SKILL-krunner-search)              | Search local KDE desktop for files, images, recent documents, bookmarks                  |
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
| :heavy_check_mark:  | [mp3-demo](../../wiki/SKILL-mp3-demo)                          | Simple sample of playing local MP3s                                                      |  
| :question:          | [mpd-control](../../wiki/SKILL-mpd-control)                    | Controls media players that use the MPD  protocol to play found local music           |  
| :question:          | [mqtt](../../wiki/SKILL-mqtt)                        | Control IoT devices (home automation) using MQTT protocol     |  
| :question:          | [mute-skill](../../wiki/SKILL-mute)            | Mutes Mycroft until re-enabled |
| :question:          | [nasa-picture-of-the-day](../../wiki/SKILL-nasa-pic-of-the-day)                    | Nasa picture of the day from the NASA API |
| :question:          | [near-earth-orbit-skill](../../wiki/SKILL-near-earth-orbit)                    | Near Earth orbit alert skill via the NASA API   |
| :construction:	  | [objective-skill](../../wiki/SKILL-objective)                  | skills can now register objectives almost the same has an intent would be registered with ObjectiveBuilder class              |
| :construction:	  |	[openhab-skill](../../wiki/SKILL-Openhab)					| This skill adds Openhab support to Mycroft |
| :question:          | [pandora-skill](../../wiki/SKILL-pandora)                   | Adds Pandora to mycroft via Pianobar  |
| :question:          | [photolocation-skill](../../wiki/SKILL-photolocation)          | Searches wikimedia for photos of location  |
| :question:          | [pickup-line-skill](../../wiki/SKILL-pickup-line)  | Responds with random nerdy pick-up lines          |
| :heavy_check_mark:          | [ping-skill](../../wiki/SKILL-ping)  | Pings websites and responds with latency time       |  
| :question:          | [plasma-activities-skill](../../wiki/SKILL-plasma-activities)  | This skill integrates Plasma 5 Activities with Mycroft|
| :question:          | [plasma-sendsms-skill](../../wiki/SKILL-plasma-sendsms)         |Send SMS through KDE Plasma     |
| :question:          | [plasma-user-control-skill](../../wiki/SILL-plasma-user-control)| This skills adds Plasma User control to Mycroft, allowing switch user, logout, and lock screen  |
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
| :heavy_check_mark:  | [skill-radio-rne](../..wiki/SKILL-radio-rne)       | Spanish news radio Radio Nacional de Espa?a RNE. | 
| :question:          | [spacelaunch-skill](../../wiki/SKILL-spacelaunch)  | Check when the next space launch is                                               |
| :question:          | [speedtest](../../wiki/SKILL-speedtest)  | Run a speedtest                                               |
| :question:          | [slack-skill](../../wiki/SKILL-slack)                          | Allows to post and listen to Slack messages.  |
| :question:          | [sunspot-skill](../../wiki/SKILL-sunspot-skill)                    | Answers questions on daily sunspots |
| :question:          | [sun-skill](../../wiki/SKILL-sun)  | Responds with sunrise and set times          |  
| :question:          |[system-skill](../../wiki/SKILL-system)               | Adds system controls like shutdown and reboot   |
| :question:          | [take_picture](../../wiki/SKILL-take-picture)  | Take Pictures using the Raspberry Pi Camera          |  
| :question:          | [traffic-skill](../../wiki/SKILL-traffic)  | Gets the commute time from Google distance matrix api         |  
| :heavy_check_mark:  | [twitter-skill](../../wiki/SKILL-twitter)              | Control twitter with mycroft                                                   |
| :question:          | [unsplash-wallpaper-plasma-skill](../../wiki/SKILL-unsplash-wallpaper-plasma)  | Change KDE Desktop wallpaper by category type from unsplash |
| :construction:      | [wallpaper-skill](../../wiki/SKILL-wallpaper)  | Downloads wallpapers from reddit and changes randomly         |
| :question:  	      | [wemo-skill](../../wiki/SKILL-wemo)              | Control Wemo devices with mycroft                                                   |
| :construction:      | [wifi-management-skill](../../wiki/SKILL-wifi-management)  | Various options for interacting with WiFi        |
| :construction:      | [wink-smart-home](../../wiki/SKILL-wink)                       | Interact with lights via a Wink-hub                                                      |  
| :question:          | [wiki-fact-scraper-skill](../../wiki/SKILL-wiki-fact-scraper)                        | Scrapes for random facts from wikipedia and stores locally    |
| :question:  | [youtube](../../wiki/SKILL-youtube)                            | Search and listen to a youtube video                                                        |  
| :question:  | [release-test](../../wiki/SKILL-release-test)                            | test mycroft release                                                        |  
