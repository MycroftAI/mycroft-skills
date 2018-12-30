# PROJECT_NAME skill

This skill illustrates a very simple MP3 music player.  It works by loading
MP3 files from the /mp3 subfolder using the format:  song_title.mp3

## Sample Songs
   
The catchy sample MP3 songs included are from http://www.bensound.com/ and are
licensed under the "Creative commons - Attribution - No Derivative Works"
license:  https://creativecommons.org/licenses/by-nd/3.0/legalcode.

Thanks, Ben!

## Current state

Working features:
Phrases you can use with this:
   "Play some music"
   "Play song title"
   "Stop" (although the action button works better usually)

Known issues:
 - Currently the song title must be lowercase and separated with underscores.

TODO:
 - Loosen up name match
 - Handle title with spaces in the name
 - Handle queuing up multiple songs (will proably become part of mycroft-core)

