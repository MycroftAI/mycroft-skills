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
| [WeMo](https://github.com/martymulligan/skill-wemo#readme)                  | Discover and control WeMo devices<br>```"discover my devices"``` |
| [Wiki](https://github.com/MycroftAI/skill-wiki#readme)                        | Wikipedia queries<br>```"tell me about AI"``` |
| [Wink IoT](https://github.com/MycroftAI/skill-wink-iot#readme)                | Control lights via a Wink hub<br>```"turn on the lights"``` ```"dim the kitchen light"``` |
| [Platform Patch](https://github.com/MycroftAI/skill-platform-patch#readme)    | Patch for official platforms<br>```"platform patch"``` |
| [Mark 1 settings](https://github.com/MycroftAI/mycroft-mark-1)                | Control your Mark 1<br>```change eye color to red``` |
| [Spotify](https://github.com/forslund/spotify-skill) | Listen to music from your Spotify Premium account<br>```play discover weekly``` |
| [Pandora](https://github.com/ethanaward/pianobar-skill) | Listen to Pandora stations<br>```play pandora``` |
| [openHAB](https://github.com/openhab/openhab-mycroft)							| Add an AI Voice assistant to your openHAB system<br>```"turn on Diningroom Light"``` ```"regulate Main Thermostat to 20 degrees"```  |


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
| :heavy_check_mark:  | [AVmusic](https://github.com/reginaneon/AVmusic/blob/master/README.md)| Provides the playback of any music/video requested by the user. No login required. <br>```play some imagine dragons music``` |
| :heavy_check_mark:  | [CaffeineWiz](https://github.com/reginaneon/caffeinewiz.reginaneon/blob/master/README.md)| Request caffeine content of selected drinks<br>```what's the caffeine content of *drink*?```|
| :heavy_check_mark:  | [mycroft-hue](https://github.com/ChristopherRogers1991/mycroft-hue/blob/master/README.md)| Control your Phillips Hue lights<br>```turn on the lights``` |
| :heavy_check_mark:  | [Homeassistant](https://github.com/btotharye/mycroft-homeassistant#readme)               | Control your devices in home-assistant<br>```"turn on office"``` |
| :heavy_check_mark:  | [Plasma Activities Skill](https://github.com/AIIX/plasma-activities-skill#readme)| Control KDE Plasma 5 Activities with Mycroft```show/create/switch/remove activity [name]``` |
| :heavy_check_mark:  | [translate-skill](https://github.com/jcasoft/translate-skill/tree/84db4da986c1ae165d4c31bb5f907398feb19326#readme)              | Translate phrases into several languages<br>```"translate good morning into japanese"``` |
| :heavy_check_mark:  | [Zork](https://github.com/forslund/white-house-adventure/blob/master/README.md)| Play the old school adventure game<br>```and explore the underground empire``` |
| :heavy_check_mark:  | [Score](https://github.com/deejcunningham/skill-score/blob/master/README.md)| Reports latest MLB scores<br>```what is the Royals score``` |

