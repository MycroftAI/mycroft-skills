# Mycroft Skills Repo
![logo](https://avatars1.githubusercontent.com/u/14171097?v=4&s=200 "Logo")

2

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

The official home of skills for the Mycroft ecosystem.  These skills are written by both the MycroftAI team and others within the Community.
**[HTML version of this document](https://mycroftai.github.io/mycroft-skills)**

## Available Skills

|      Skill Name                                                               |                Description<br>"handled phrases"                      |                                           
| ------------------------------------------------------------------------------| ---------------------------------------------------------------------|
| [AIML Fallback](https://github.com/forslund/fallback-aiml#readme)             | AIML skill by JarbasAI |
| [Alarm](https://github.com/MycroftAI/skill-alarm#readme)                      | Alarm |
| [Audio Record](https://github.com/MycroftAI/skill-audio-record#readme)        | Record and Play Audio<br>```"record"``` |
| [Configuration](https://github.com/mycroftai/skill-configuration#readme)      | Update Mycroft configuration<br>```"configuration update"``` |
| [Date Time](https://github.com/MycroftAI/skill-date-time#readme)              | Tell the date or time<br> ```"what time is it"``` |
| [Desktop Launcher](https://github.com/MycroftAI/skill-desktop-launcher#readme)| Open Applications on Desktop<br>```"open firefox"``` |
| [DuckDuckGo](https://github.com/MycroftAI/fallback-duckduckgo#readme)         | Query DuckDuckGo's Instant Answer API for general questions<br> ```"what is frankenstein"``` |
| [Hello World](https://github.com/mycroftai/skill-hello-world#readme)          | Hello world and Mycroft manners<br> ```"how are you"``` |
| [IP](https://github.com/MycroftAI/skill-ip#readme)                            | Check the device's IP Address<br> ```"what is your ip address"``` |
| [Joke](https://github.com/MycroftAI/skill-joke#readme)                        | Tell jokes<br> ```"tell me a joke"``` |
| [Installer](https://github.com/mycroftai/skill-installer#readme)              | Install skills<br> ```"install daily meditation"```<br>```"uninstall skill daily meditation"``` |
| [Mark-1 Demo](https://github.com/MycroftAI/skill-mark1-demo#readme)           | Demonstration of Mark 1 <br> DEMO from the Mark 1 menu |
| [Naptime](https://github.com/mycroftai/skill-naptime#readme)                  | Put Mycroft to sleep<br>```"go to sleep"``` |
| [NPR News](https://github.com/MycroftAI/skill-npr-news#readme)                | Listen to the news from NPR<br>```"what's the latest news"``` |
| [Pairing](https://github.com/mycroftai/skill-pairing#readme)                  | Pair Mycroft with home.mycroft.ai<br>```"pair my device"``` |
| [Personal](https://github.com/MycroftAI/skill-personal#readme)                | Learn about Mycroft<br>```"what are you"``` |
| [Playback Control](https://github.com/mycroftai/skill-playback-control#readme)| Control audio subsystem<br>```"play", "pause", "next" ``` |
| [Reminder](https://github.com/MycroftAI/skill-reminder#readme)                | Reminders to do something<br>```"remind me to turn off the oven in 5 minutes"``` |
| [Speak](https://github.com/MycroftAI/skill-speak#readme)                      | Repeat anything<br>```"say open source AI"``` |
| [Singing](https://github.com/MycroftAI/skill-singing#readme)                  | Sing a song!<br>```"sing a song"``` |
| [Stock](https://github.com/MycroftAI/skill-stock#readme)                      | Stock prices<br>```"what is the stock price of Autodesk"``` |
| [Stop](https://github.com/mycroftai/skill-stop#readme)                        | Stop running skills<br>```"stop"``` |
| [Unknown Fallback](https://github.com/mycroftai/fallback-unknown#readme)      | When Mycroft doesn't know an answer or understand a command<br>```"green jelly wood"```   |
| [Version Checker](https://github.com/MycroftAI/skill-version-checker#readme)  | Find the version of mycroft-core<br>```"check version"``` |
| [Volume](https://github.com/mycroftai/skill-volume#readme)                    | Control Volume<br>```"turn up the volume", "mute audio"``` |
| [Weather](https://github.com/MycroftAI/skill-weather#readme)                  | Current Weather and Forecasts<br>```"what is the weather"``` |
| [Wiki](https://github.com/MycroftAI/skill-wiki#readme)                        | Wikipedia queries<br>```"tell me about AI"``` |
| [Wink IoT](https://github.com/MycroftAI/skill-wink-iot#readme)                | Control lights via a Wink hub<br>```"turn on the lights"``` ```"dim the kitchen light"``` |
| [Platform Patch](https://github.com/MycroftAI/skill-platform-patch#readme)    | Patch for official platforms<br>```"platform patch"``` |
| [Mark 1 settings](https://github.com/MycroftAI/mycroft-mark-1)                | Control your Mark 1<br>```change eye color to red``` |
| [Spotify](https://github.com/forslund/spotify-skill) | Listen to music from your Spotify Premium account<br>```play discover weekly``` |
| [Pandora](https://github.com/ethanaward/pianobar-skill) | Listen to Pandora stations<br>```play pandora``` |


## How to Submit a Skill

### 1) Make a Repo
Create the skill in a repo under your own Github user account.  You can follow the guide at [How To Make a Repo](https://help.github.com/articles/create-a-repo/), or use the [skiller.sh script](https://github.com/MycroftAI/mycroft-core/blob/dev/skiller.sh).

### 2) Clone Repo
Clone the mycroft-skills repo to a local directory, [How To Clone](https://help.github.com/articles/cloning-a-repository) if you are unfamiliar with the process.

```git clone https://github.com/MycroftAI/mycroft-skills.git```

### 3) Generate the README.md
All skills must have a standard README.md.  You can use the [Meta Editor](http://rawgit.com/MycroftAI/mycroft-skills/master/meta_editor.html) to create it.

### 4) Add your Skill as a submodule
Add the your skill to this repo as a submodule.  You can type the following in the terminal of within your clone of
the mycroft-skills repo.
```
git submodule add $remote $name-of-your-skill
```
Where ```$remote``` is the git address for your repo (for example "https://github.com/MycroftAI/skill-configuration") and
```$name-your-skill``` is the name used to install it via MSM or "Hey Mycroft, install ...".  The recommended format for skill names is "publisher-descriptive-name", where 'publisher' is a unique name for you or your organization.  For example, "penrod-nautical-speed-translator".

When picking a name keep in mind that the installer will match by whole words between the dashes.  So if a user says
"install speed translator" it will look for all skills in the repo with the words 'speed' AND 'translator'.  That
means it will find "penrod-nautical-speed-translator" but would not find "abc-nautical-speeds-translator".  Make
sure the pieces of the name are 'speakable' to allow verbal installs.  That means "fubar-v2timer" would be a bad
name since you can't speak "v2timer" as a word.  A better name would be "fubar-timer-v2" or "fubar-timer-version-2".

The above command should have modified the .gitmodules file and added something similar to the bottom of the file:
```
+[submodule "NAME-OF-YOUR-SKILL"]
 +	path = YOUR-SKILL-REPO (or any unique path withing the mycroft-skills repo)
 +	url = https://github.com/USERNAME/YOUR-SKILL-REPO.git
```

For more help, feel free to check out this [guide to working with submodules](https://github.com/blog/2104-working-with-submodules)

### 5) Modify this README.md
Modify the table section below to include the direct link to your repo.  Including the break HTML tag and an example phrase
or two that trigger your skill:

```
| :heavy_check_mark:  | [home-assistant](https://github.com/btotharye/mycroft-homeassistant#readme)| Control your devices in home-assistant<br>```turn on office``` |

```
Chose an appropriate status icon from the list below:

**Status:**  
:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!

### 6) Submit a PR (Pull Request)
Once you've got your local version of the repo organized properly, submit a PR.

### MSM Compliance
To make your skill capable of being installed via MSM (the Mycroft Skill Manager) you can include two additional files.

##### requirements.txt
A list of all Python modules which must be installed for it to work.  These will be installed via the Python PIP utility

##### requirements.sh
A script to run that will perform any additional steps needed to prepare the system for your skill.  This can include package installations.


**Status meaning:**  
:heavy_check_mark: good working order  
:construction:     still being developed and not ready for general use (for reference/collaboration)  
:question:         untested (by us)  
:skull:            Broken, but good for ideas!

For an example pull request , check out [this PR](https://github.com/MycroftAI/mycroft-skills/pull/37)


## Community Contributed Skill List

**When submitting a skill make sure skill name links to main repo for the skill, we are doing away with
wiki pages.  Also please include the phrase to trigger on as well for your skill.**


| Status              | Skill Name                                                                      | Description<br>```"phrase to trigger"```    |
| ------------------- | ------------------------------------------------------------------------------- | --------------------------------------------|
| :heavy_check_mark:  | [AVmusic](https://github.com/NeonGeckoCom/AVmusic-skill#readme)| Lets the user request playback of any music or video available. Version 1.0 <br>```"AVmusic play chopin"``` |
| :heavy_check_mark:  | [Australian news](https://github.com/KathyReid/skill-australian-news/README.md)	| Play ABC news from Australia<br />```"Play Australian news"```|
| :heavy_check_mark:  | [AutoGUI](https://github.com/eClarity/skill-autogui#skill-autogui)              | Manipulate your mouse and keyboard with Mycroft                                                  |
| :heavy_check_mark:  | [Basic help](https://github.com/btotharye/mycroft-skill-basichelp#readme)       | Get basic Mycroft questions and help answered<br>```"where is the documentation", "how do I install from source"```         |
| :heavy_check_mark:  | [Better jokes](https://github.com/tjoen/skill-better-jokes#readme)              | Get mycroft to make better jokes<br>```be funny``` |
| :heavy_check_mark:  | [Caffeine Wiz](https://github.com/reginaneon/skill-caffeinewiz.git)             | Provides the caffeine content of various drinks on request.<br>```what's caffeine content of *drink*?``` |
| :heavy_check_mark:  | [Coin flip](https://github.com/wligtenberg/coin-flip-skill#coin-flip)           | Flip a virtual coin   |
| :heavy_check_mark:  | [Deutschland Funk](https://github.com/ofosos/deutschlandfunk-skill)             | Listen to Deutschlandfunk and query schedule
| :heavy_check_mark:  | [Federal Closings](https://github.com/mason88/skill-federal-closings)           | List Federal Government Closings<br>```"are there federal closings?"```
| :heavy_check_mark:  | [Home Assistant](https://github.com/btotharye/mycroft-homeassistant#readme)     | Control your devices in home-assistant<br>```"turn on office"```                                                      |  
| :heavy_check_mark:  | [Pandora](https://github.com/ethanaward/pianobar-skill)                         | Play Pandora stations via Pianobar  |
| :heavy_check_mark:  | [Parrot](https://github.com/JarbasAl/skill-parrot)                              | Repeat everything back to user  |
| :heavy_check_mark:  | [Ping](https://github.com/nogre/ping-skill#mycroft-ai-ping-skill)               | Pings websites and responds with latency time       |  
| :heavy_check_mark:  | [Radio RNE](https://github.com/normandmickey/skill-internet-radio/tree/3fb352430daa09082f41f20742836a996a19ff1d#internet-radio)                                     | Spanish news radio Radio Nacional de Espa?a RNE. |
| :heavy_check_mark:  | [Timer](https://github.com/MycroftAI/mycroft-timer.git)                         | Set a timer on your device<br>```set a timer for 30 minutes```
| :heavy_check_mark:  | [Internet Radio](https://github.com/normandmickey/skill-internet-radio#readme)  | Listen to Internet Radio<br>```internet radio``` |
| :heavy_check_mark:  | [Number Generator](https://github.com/angry-frog/number-generator-skill#readme) | Mycroft will pick a random number<br>```pick a number``` |
| :heavy_check_mark:  | [Bitcoin price](https://github.com/dmp1ce/mycroft-bitcoinprice-skill#readme)    | Check the price of bitcoin<br>```what is the bitcoin price?``` |
| :heavy_check_mark:  | [ESP8266](https://github.com/Dark5ide/esp8266-skill.git#readme)                 | Communicate with an ESP8266 in the context of home automation.<br>```Turn on the lamp``` |
| :heavy_check_mark:  | [Repeat Recent](https://github.com/matthewscholefield/skill-repeat-recent#readme) | Repeat what you or Mycroft just said<br>```What did you just say?``` |
| :construction:      | [Podcast Skill](https://github.com/JamesPoole/podcast-skill#readme)             | Listen to the latest episodes of your favourite podcasts.<br>  ```play the latest episode of the reply-all podcast``` |
| :construction:      | [Brain](https://github.com/skeledrew/brain-skill#brain-skill)                   | Chain intents and provide some services                                                 |
| :construction:      | [Calculator](https://github.com/TREE-Edu/calculator-skill.git)                  | Conversation-based calculator.<br>```Do some math```
| :construction:      | [Dice roll](https://github.com/Friday811/skill-dice#skill-dice-skill)           | Roll dice spoken in RPG notation.                                                       |
| :construction:      | [Facebook marketing](https://github.com/ProsperousHeart/mycroft-facebook-marketing#facebook-marketing-skill)                       | Work with Facebook Marketing API                                                        |
| :construction:      | [GPIO example](https://github.com/MycroftAI/picroft_example_skill_gpio#raspberry-pi-gpio-demo)  | Example of using the GPIO pins on the Raspberry Pi to blink an LED                                         |    
| :construction:      | [MiLight](https://github.com/maxppc/Mycroft-milight-skill/tree/ba88e4aadc574e086964c1769347a01fe8a1d97b#mycroft-milight-skill)                                             | Lighting control using MiLight                                                           |  
| :construction:      | [Mopidy and BT lights](https://github.com/swilso793/mycroft_third_party_skills) | Remote control of BT lights and Mopidy music playback                                    |  
| :construction:      | [Mosquito speak](https://github.com/CarstenAgerskov/skill-mosquito-speak)       | Allow Mycroft to notify you on events, by speaking text received on a mqtt bus.                                    |  
| :construction:      |	[OpenHAB](https://github.com/openhab/openhab-mycroft#openhab-skill-for-mycroft) | Add Openhab support to Mycroft |
| :construction:      | [The Cows Lists](https://github.com/CarstenAgerskov/skill-the-cows-lists#readme)| Interact with "Remember The Milk" list and task management ecosystem.<br>```"add milk to my grocery list"```    |
| :construction:      | [Whats Nearby](https://github.com/AIIX/whats-nearby#readme) | Search for nearby Places for Mycroft on Plasma (Search For Resturants, Hotels, Parks etc)<br>```"search for nearby bars/pubs/parks/hospitals/etc"``` |
| :construction:      | [Kickstarter Tracker](https://github.com/MatthewScholefield/skill-kickstarter-tracker#readme) | Track the pledge amount of a project on Kickstarter<br>```"track mycroft on kickstarter"``` |
| :construction:      | [FlightGear Copilot](https://github.com/merspieler/flight-gear-copilot/#readme) | This skillacts as an copilot for flight gear that assists you by following your voice commands.      |
| :question:          | [Amarok media player control](https://github.com/AIIX/amarok-player-skill#readme) | Player controls for the Amarok Media Player<br>```"amarok play/stop/next/previous music"``` |
| :question:          | [Angry Beanie podcast](https://github.com/purserj/mycroft-angrybeanie#readme)   | Query and play Angry Beanie Podcasts<br />```"Get Angry Beanie shows"``` |
| :question:          | [Plasma audio control](https://github.com/AIIX/audio-control-plasma#readme)     | Audio control for Plasma Desktop<br>```"increase volume to maximum", "decrease microphone to minimum volume"```         |
| :question:          | [Bioinformatics](https://github.com/TicklishGiraffe/mycroft_genomics#mycroft_bioinformatics) | Add Bio-Linux Commands to Mycroft   |  
| :question:          | [Bitcoin](https://github.com/Red5d/mycroft_skills/tree/master/bitcoin)          | Check the price of bitcoin                                                               |  
| :heavy_check_mark:  | [CBC news](https://github.com/chrison999/mycroft-skill-cbc-news#mycroft-skill-cbc-news)  | Fetch CBC News Podcast             |  
| :question:          | [Clarifai image recognition](https://github.com/AIIX/clarifai-image-recognition-skill#readme) | Image recognition based on clarifai<br> ```"search image url [imagelocation]"```   |
| :question:          | [Clementine player](https://github.com/Skills-And-Translations/mycroft-clementine-skill/tree/270a79f66f49b1f2d98d83a4c676ce27bad99c19#mycroft-clementine-player-plasma-skill)             | Control your clementine-player localy. A fork from amarok-player.   |
| :question:          | [Daily Meditation](https://github.com/kfezer/daily_meditation#daily_meditation) | Play your Daily Meditation from the  Meditation Podcast     |
| :question:          | [Diagnostics](https://github.com/the7erm/mycroft-skill-diagnostics/tree/6b30ed6b9e0a701c179eb8452674a2bd52040bf4#mycroft-skill-diagnostics)                    | Diagnostic tools (CPU %age, free space, etc)    |
| :question:          | [Domoticz](https://github.com/treussart/domoticz_skill#domoticz_skill)          | Integrate Mycroft with Domoticz    |
| :question:          | [Drive servos](https://github.com/Nold360/mycroft_skill-drive_servos)           | Control Hacked-Servo-Engines to make your Mycroft move around   |
| :question:          | [Fox newsskill](https://github.com/chrison999/mycroft-skill-fox-news#mycroft-skill-fox-news)  | Fetch Fox News Podcast                                                                 |
| :question:          | [Google Calendar](https://github.com/jcasoft/GoogleCalendarSkill/tree/d26b18fe44b3c0efbfbd156731c7e48c104fdf27#googlecalendarskill-with-add-events-mycroft-new-api)                             | Check and add google calendar events                                                     |  
| :question:          | [Gmail](https://github.com/jcasoft/GoogleGmailSkill/tree/8a79f382d958e3bddf12543640796f6d1062ecff#googlegmailskill-mycroft-new-api)                                          | Get email from your Gmail Inbox                                                         |  
| :question:          | [Google translate](https://github.com/jcasoft/TranslateSkill#translateskill-google-translate-skill)                       | Translate English phrases into other languages                                           |
| :question:          | [Hue](../../wiki/SKILL-hue)                                                     | Control your Phillips Hue lights                                                         |  
| :question:          | [IR Send](../../wiki/SKILL-irsend)                                              | Control devices via [lirc's](http://www.lirc.org/) [irsend](http://www.lirc.org/html/irsend.html)                                                         |
| :question:          | [JB podcasts](../../wiki/SKILL-Jupiter-Broadcasting-Podcasts)                   | Play podcasts from Jupiter Broadcasting shows                                            |  
| :question:          | [KDE Kate control](https://github.com/AIIX/kde-kate-control#readme)             | Kate Editor control skill <br>```"new document, close document, goto next/previous tabs/views"```                  |
| :question:          | [KDE Krunner search](https://github.com/AIIX/krunner-search-skill#readme)       | Search local KDE desktop for files, images, recent documents, bookmarks<br>```"search this computer for [any keyword]"```                  |
| :question:          | [Kodi cadair](https://github.com/Cadair/mycroft-kodi#kodi-skill-for-mycroft-ai) | Kodi playback and search                                                                 |  
| :question:          | [Kodi cbenning](https://github.com/cbenning/kodi-skill#kodi-skill)              | Control a local or remote Kodi instance                                                  |  
| :question:          | [Kodi k3yb0ardn1nja](https://github.com/k3yb0ardn1nja/mycroft-skill-kodi/tree/84d74b687d5fbb7a86993f8b8aa537955a364743#kodi-remote-control-skill-for-mycroft)               | Play or pause a Kodi video                                                               |  
| :question:          | [Let's talk](https://github.com/chrison999/mycroft-skill-lets-talk#mycroft-skill-lets-talk)  | More salutations |
| :question:          | [Media console control](https://github.com/the7erm/mycroft-skill-simple-media-controls#mycroft-skill-simple-media-controls)                 | Add media controls that are mapped to console commands                                  |  
| :question:          | [Mopidy](https://github.com/forslund/mopidy_skill#readme)                       | Mopidy-based players for local music, Google Music, and Spotify                          |  
| :question:          | [MPD control](https://github.com/forslund/mpd_skill#mpd-skill)                  | Control media players that use the MPD protocol to play found local music           |
| :question:          | [MQTT](https://github.com/jamiehoward430/mycroft-mymqtt#mqtt-for-mycroftai)     | Control IoT devices (home automation) using MQTT protocol     |  
| :question:          | [Nature Sounds](https://github.com/Hasinator7/nature-sound-skill#readme)        | Play relaxing nature sounds recorded at various locations<br>```play [river/thunderstorm/songbird]``` |  
| :question:          | [Pickup line](https://github.com/JarbasAl/skill-pick-up-lines#mycroft---pick-up-line---skill)  | Responds with random nerdy pick-up lines          |
| :question:          | [Plasma activities](https://github.com/AIIX/plasma-activities-skill#readme)     | Integrate Plasma 5 Activities with Mycroft<br>```"show activities / switch activity [name]"```|
| :question:          | [Plasma Mycroft plasmoid control](https://github.com/AIIX/plasma-mycroftplasmoid-control#readme)  | Control the Mycroft Plasmoid<br>```"show mycroft applet / display skills page"```|
| :question:          | [Plasma send SMS](https://github.com/AIIX/plasma-sendsms-skill#readme)          | Send SMS through KDE Plasma<br>```"send a sms"```     |
| :question:          | [Plasma user control](https://github.com/AIIX/plasma-user-control-skill#readme) | Add Plasma User control to Mycroft, allowing switch user, logout, and lock screen<br>```"switch user/logout/lock screen"```  |
| :question:          | [Pushbullet](https://github.com/jcasoft/PushbulletSkill#pushbulletskill)        | Send messsages and photos using Pushbullet                                                  |
| :question:          | [Pushetta](https://github.com/marksev1/Mycroft-Pushetta-skill#pushetta-skill)   | Add push notifications |
| :question:          | [Quodlibet](https://github.com/kfarwell/mycroft-skill-quodlibet#mycroft-skill-quodlibet)  | Control Quod Libet music playback                                                        |  
| :question:          | [RATP timetables](https://github.com/ldubost/mycroft-skills/tree/master/ratp-timetables#ratp-timetable)   | Access schedules for the RATP Network of trains and buses in Paris                       |
| :question:          | [Spaceflight schedule](https://github.com/praxeo/mycroft_spaceflightnow_skill#mycroft_spaceflightnow_skill)   | Check when the next space flight launch is scheduled                                              |
| :question:          | [Spacelaunch](https://github.com/marksev1/Mycroft-SpaceLaunch-Skill#spacelaunch-skill)   | Check when the next space launch is scheduled                                              |
| :question:          | [Speedtest](https://github.com/ChristopherRogers1991/mycroft-speedtest#mycroft-speedtest)  | Run a speedtest                                               |
| :heavy_check_mark:    | [Subsonic Media Player](https://github.com/mycroftai/skill-subsonic-media#readme)   | Subsonic Media Skill<br>```"play something i can never have by nine inch nails"```  |
| :question:          | [Slack](https://github.com/guilhembn/Mycroft-Slack-skill#mycroft-slack-skill)   | Post and listen to Slack messages.  |
| :question:          | [Sunspot](https://github.com/BoatrightTBC/sunspots#sunspots)                    | Answer questions on daily sunspots |
| :question:          | [Sun](https://github.com/marksev1/Mycroft-SunSkill#sun-skill)                   | Respond with sunrise and set times        |  
| :question:          | [System](https://github.com/CloneMMDDCVII/systemSkill-Mycroft-core-Skill-#systemskill-mycroft-core-skill-)   | System controls like shutdown and reboot   |
| :question:          | [Take picture](https://github.com/Nold360/mycroft_skill-take_picture)           | Take pictures using the Raspberry Pi Camera          |  
| :question:          | [Traffic](https://github.com/Nold360/mycroft_skill-take_picture)                | Commute time from Google distance matrix api         |  
| :question:          | [White House Adventure](https://github.com/forslund/white-house-adventure)      | Play the old text adventure Zork 1                   |
| :question:          | [Unsplash wallpaper-plasma-skill](https://github.com/AIIX/unsplash-wallpaper-plasma-skill#readme)  | Change KDE Desktop wallpaper by category type from unsplash<br>```"change wallpaper type [nature\abstract\any]"``` |
| :question:	        | [WEMO](https://github.com/martymulligan/skill-wemo#wemo-skill)                    | Control WEMO devices with Mycroft                                                   |
| :question:          | [Youtube](https://github.com/augustnmonteiro/mycroft-youtube#readme)            | Search and listen to a Youtube video                                                        |
| :question:          | [Release test](https://github.com/MycroftAI/skill-release-test#release-test)    | Test a mycroft-core release                                                        |  
| :skull:             | [Enhanced Bitcoin](https://github.com/chrison999/mycroft-skill-bitcoin-enhanced#mycroft-skill-bitcoin-enhanced)    | Enhanced bitcoin from api.bitcoinaverage.com        |
| :heavy_check_mark:   | [Farting](https://github.com/aussieW/skill-farting)                      | Fart on request or randomly    |
| :heavy_check_mark:   | [Confucius Say](https://github.com/aussieW/skill-confucius-say)   | Get quotes from Confucius, including humorous quotes.       |
