# Mycroft Skills :package:
A repository for sharing and collaboration for third-party Mycroft skills  
development.  This is a place to publish complete Skills and learn Skill  
writing as well as share best practices.

## How to Add Skills to the Repo!

If you want to submit a skill, simply make a repo for it organized   
as the template above.
[Example Skill Template](https://github.com/MycroftAI/mycroft-skills/tree/master/00__skill_template)  

Clone the mycroft-skills repo to a local directory then:

To get the skill added, modify the Readme file.
* The README.md  

In the README, add a line under "Community Contributed Skill List" (alphabetically, please!) describing your skill and linking to it in the wiki. Feel free to make a new wiki page for your skill! Also, indicate the status according to the guide below.

After that, you need to add the submodule for your skill. For more help, feel free to check out [this guide](https://github.com/blog/2104-working-with-submodules)

Or, type the following in the terminal of your clone of the Skills-repo.
```
git submodule add $remote $name-your-skill
```
Where $remote is the git address for your repo and $name-your-skill is what you want to name it. In general, we normally use BLANK-skill as a format for skill names.

This should have edited the .gitmodule file and added something similar to the bottom of the file:
```
+[submodule "NAME OF YOUR SKILL"]
 +	path = name-of-your-skill-skill
 +	url = URL.FOR.YOUR.SKILL.git
```

Once you've got your repo organized properly, submit the PR consisting of the following:
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

## Official Skill List
| Status              | Skill Name                                                     | Description                                                                              |  
| ------------------- | -------------------------------------------------------------- | ---------------------------------
| :heavy_check_mark:          |[Alarm](../../wiki/SKILL-Alarm)                         | Alarm                            |
| :heavy_check_mark:          |[Audio Record](../../wiki/SKILL-Audio-Record)           | Record and Play Audio            |
| :heavy_check_mark:          |[Date Time](../../wiki/SKILL-Date-Time)                 | Tell the date or time            |
| :heavy_check_mark:          |[Desktop Launcher](../../wiki/SKILL-Desktop-Launcher)   | Open Applications on Desktop     |
| :heavy_check_mark:          |[IP](../../wiki/SKILL-IP)                               | Check the device's IP Address    |
| :heavy_check_mark:          |[Joke](../../wiki/SKILL-Joke)                           | Tell jokes                       |
| :heavy_check_mark:          |[Media](../../wiki/SKILL-Media)                         | Multimedia Control               |
| :heavy_check_mark:          |[NPR News](../../wiki/SKILL-NPR-News)                   | Listen to the news from NPR      |
| :heavy_check_mark:          |[Personal](../../wiki/SKILL-Personal)                   | Learn about Mycroft              |
| :heavy_check_mark:          |[Reminder](../../wiki/SKILL-Reminder)                   | Reminders to do something        |
| :heavy_check_mark:          |[Speak](../../wiki/SKILL-Speak)                         | Repeat anything                  |
| :heavy_check_mark:          |[Singing](../../wiki/SKILL-Singing)                     | Sing some Songs                  |
| :heavy_check_mark:          |[Stock](../../wiki/SKILL-Stock)                         | Stock prices                     |
| :heavy_check_mark:          |[Weather](../../wiki/SKILL-Weather)                     | Current Weather and Forecasts    |
| :heavy_check_mark:          |[Wiki](../../wiki/SKILL-Wiki)                           | Wikipedia queries                |
| :heavy_check_mark:          |[Wolfram Alpha](../../wiki/SKILL-Wolfram-Alpha)         | Wolfram Alpha                    |

## Community Contributed Skill List


| Status              | Skill Name                                                     | Description                                                                              |  
| ------------------- | -------------------------------------------------------------- | -------------------------------------
| :question:          |[amarok-media-player-skill](../../wiki/SKILL-amarok-media-player)               | Player controls for the Amarok Media Player   |
| :question:          |[bioinformatics](../../wiki/SKILL-bioinformatics)               | Adds Bio-Linux Commands to Mycroft   |  
| :question:          | [bitcoin](../../wiki/SKILL-bitcoin)                            | Check the price of bitcoin                                                               |  
| :construction:      | [bitcoin-price](../../wiki/SKILL-bitcoin-price)                |  Checks the price of bitcoin                             |
| :question:          | [cbc-news-skill](../../wiki/SKILL-cbc-news)        | Fetches CBC News Podcast             |  
| :question:          | [clementine-player-skill](../../wiki/SKILL-clementine-player)  | Controls your clementine-player localy. A fork from amarok-player.   |
| :skull:             | [cleverbot-skill](../../wiki/SKILL-cleverbot)                  | when wolpham alpha doesnt have an answer asks cleverbot   |
| :question:          | [daily-meditation](../../wiki/SKILL-daily-meditation)          |Plays your Daily Meditation from the  Meditation Podcast     |
| :construction:      | [deepdream_skill](../../wiki/SKILL-deepdream)                  | Adds Deepdreaming image converstion to Mycroft       |
| :question:          | [diagnostics](../../wiki/SKILL-diagnostics)                    | Diagnostic tools (CPU %age, free space, etc)    |
| :question:          | [domoticz_skill](../../wiki/SKILL-domoticz)                    | Skill integrating Mycroft with Domoticz    |
| :question:          | [drive_servos](../../wiki/SKILL-drive-servos)                  | Control Hacked-Servo-Engines to make your mycroft move around   |
| :question:          | [earth-orbit-pic-skill](../../wiki/SKILL-earth-orbit-pic)      | Earth orbit picture skill   |
| :question:          | [enhanced-bitcoin-skill](../../wiki/SKILL-enhanced-bitcoin)    | Enhanced bitcoin skill from api.bitcoinaverage.com        |  
| :construction:      | [facebook](../../wiki/SKILL-facebook)                          | Generates posts for Facebook                  |
| :construction:      | [facebook-marketing](../../wiki/SKILL-facebook-marketing)      | Works with Facebook Marketing API                                                        |
| :question:          | [feedback-skill](../../wiki/SKILL-feedback)                    | triggers positive feedback intent -> calls feedback method on last active skill          |  
| :question:          | [fox-news-skill](../../wiki/SKILL-fox-news)                    | Fetches Fox News Podcast                                                                 |
| :question:          | [google-calendar](../../wiki/SKILL-google-calendar)            | Check and add google calendar events                                                     |  
| :question:          | [google-gmail](../../wiki/SKILL-google-gmail)                  | Get emails from your Gmail Inbox                                                         |  
| :question:          | [google-image-search](../../wiki/SKILl-google-image-search)    | Search google images for search term and display                                         |
| :question:          | [google-translate](../../wiki/SKILL-google-translate)          | Translate English phrases into other languages                                           |  
| :question:          | [hue](../../wiki/SKILL-hue)                                    | Control your Phillips Hue lights                                                         |  
| :heavy_check_mark:  | [home-assistant](../../wiki/SKILL-home-assistant)              | Control your devices in home-assistant                                                   |  
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
| :construction:	      | [objective-skill](../../wiki/SKILL-objective)                  | skills can now register objectives almost the same has an intent would be registered with ObjectiveBuilder class              |
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
| :question:          | [read-article-skill](../../wiki/SKILL-read-article)            | Scrapes text from online articles and reads them to you.   |
| :question:          | [rss-skill](../../wiki/SKILL-rss)            | Fetches from RSS feed   |
| :question:          | [sentiment-analysis-skill](../../wiki/SKILL-sentiment-analysis)  | Sentiment analysis              |  
| :question:          | [spaceflight-schedule](../../wiki/SKILL-spaceflight-schedule)  | Check when the next space flight launch is                                               |  
| :question:          | [spacelaunch-skill](../../wiki/SKILL-spacelaunch)  | Check when the next space launch is                                               |
| :question:          | [sunspot-skill](../../wiki/SKILL-sunspot-skill)                    | Answers questions on daily sunspots |
| :question:          | [sun-skill](../../wiki/SKILL-sun)  | Responds with sunrise and set times          |  
| :question:          |[system-skill](../../wiki/SKILL-system)               | Adds system controls like shutdown and reboot   |
| :question:          | [take_picture](../../wiki/SKILL-take-picture)  | Take Pictures using the Raspberry Pi Camera          |  
| :question:          | [traffic-skill](../../wiki/SKILL-traffic)  | Gets the commute time from Google distance matrix api         |  
| :heavy_check_mark:  | [twitter-skill](../../wiki/SKILL-twitter)              | Control twitter with mycroft                                                   |
| :question:          | [wallpaper-skill](../../wiki/SKILL-wallpaper)  | Downloads wallpapers from reddit and changes randomly         |
| :question:          | [wifi-management-skill](../../wiki/SKILL-wifi-management)  | Various options for interacting with WiFi        |  
| :construction:      | [wink-smart-home](../../wiki/SKILL-wink)                       | Interact with lights via a Wink-hub                                                      |  
| :question:          | [wiki-fact-scraper-skill](../../wiki/SKILL-wiki-fact-scraper)                        | Scrapes for random facts from wikipedia and stores locally    |
| :question:  | [youtube](../../wiki/SKILL-youtube)                            | Search and listen to a youtube video                                                        |  
