# About

Phasmophobia Solver lets your chat help keep track of collected evidence. When evidence is collected and the bot is updated, the
bot will inform chat of the remaining possibilities. Users can also type the !<ghosttype> to get more information about the ghosts.

Textfiles are updated in order to display the contents on stream.

# Commands

The following commands are available:
- !ghostname - set the name of the ghost
- !ev1 - set evidence #1
- !ev2 - set evidence #2
- !ev3 - set evidence #3
- !evreset - reset evidence

Here's how it looks:
```
12:06  user: !ghostname Rick Morty
12:06  bot: [PS] Name updated!

12:06  user: !ev1 emf
12:06  bot: [PS] Evidence #1 set to EMF Level 5, ghost could be any of: Phantom, Shade, Oni, Banshee, Jinn, Revenant

12:06  user: !ev2 orbs
12:06  bot: [PS] Evidence #2 set to Ghost Orbs, ghost could be any of: Phantom, Shade, Jinn

12:06  user: !ev3 writing
12:06  bot: [PS] Evidence #3 set to Ghost Writing, ghost must be a Shade

12:08  user: !ev3 finger
12:08  bot: [PS] Evidence #3 set to Fingerprints, no ghost for this combination (EMF Level 5,Ghost Orbs,Fingerprints)

12:08  user: !evreset
12:08  bot: [PS] Cleared

11:39  user: !poltergeist
11:39  bot: [PS] Poltergeist: One of the most famous Ghosts, a Poltergeist, also known as a noisy ghost can manipulate objects around it to spread fear into it's victims. Unique Strengths: A Poltergeist can throw huge amounts of objects at once. Weaknesses: A Poltergeist is almost ineffective in an empty room. Evidence: Spirit Box, Fingerprints and Ghost Orb
```

# Files

The following files are updated (or empty) with the evidence or ghost type:
- evidence1.txt
- evidence2.txt
- evidence3.txt
- resolved_ghost.txt
- ghost_name.txt

# Changes

- 1.0.4
  - Ghostname is no longer forced to lower case

- 1.0.3
  - Added !ghostname

- 1.0.2
  - Setting evidence immediately shows remaining ghost types

- 1.0.1
  - Added stuff like !banshee but for each ghost
  - Fixed !evreset

- 1.0.0
  - Initial public release

# Special thanks

- https://www.twitch.tv/itspatokay (The streamer that provided the idea)
- https://www.twitch.tv/kruiser8 (This script will look familiar to RaidNotify of kruiser8, since I used their script as template)

# Installation instructions

*If you've never used scripts in Streamlabs Chatbot before, [refer to this guide to enable the ability to use scripts first.](https://streamlabs.com/content-hub/post/chatbot-scripts-desktop)*

1) Go to the [PhasmophobiaSolver Website](https://github.com/martijns/PhasmophobiaSolver), click "Code" and "Download ZIP".

![](https://i.imgur.com/bMuFdLj.png)

2) Open Streamlabs Chatbot, go to the "Scripts" section, then click the "Import" button.

![](https://i.imgur.com/c23AdVu.png)

3) Select the `PhasmophobiaSolver-main.zip` file you just downloaded.

![](https://i.imgur.com/csiXae6.png)

The script should now be installed and ready to go. You'll likely also want to show this to your viewers.

1) Create or download an existing overview (like [this one](https://drive.google.com/drive/folders/1cpgeYY5vTtEmqdORb6eq8qJ-mX1rqOw_) provided in a video of [JenEricLive](https://www.youtube.com/watch?v=llpGUNF1sls))

2) Add the image to your OBS overlay

3) Add 'Text (GDI+)' sources to your overlay where you set 'Read from file'. You can find the files by clicking the script in Streamlabs Chatbot, then clicking 'Open File Location'. *Typically you can also find it by entering this in the address bar of your File Explorer: `%APPDATA%\Streamlabs\Streamlabs Chatbot\Services\Scripts\PhasmophobiaSolver\files`*

![](https://i.imgur.com/ISf6BIN.png)

# License

The MIT License (MIT) Copyright (c) 2021 Martijn Stolk
