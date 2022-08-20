# About

Phasmophobia Solver lets your chat help keep track of collected evidence. When evidence is collected and the bot is updated, the
bot will inform chat of the remaining possibilities. Users can also type the !<ghosttype> to get more information about the ghosts.

Textfiles are updated in order to display the contents on stream. HTML files are provided if you'd like to display the status as images.

Please check the installation instructions at the bottom.

# Commands

The following commands are available:
- !ghostname - set the name of the ghost
- !ev1 - set evidence #1
- !ev2 - set evidence #2
- !ev3 - set evidence #3
- !ghostinfo Get a list of the ghost name and current evidence, with possible ghosts left
- !evreset - reset evidence

Here's how it looks in the chat:
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

Here's how it looks if you use the overlay with text sources:

![](https://i.imgur.com/O8JILAW.png)

Here's how it looks if you add the evidence images via browser source:

![](https://i.imgur.com/EmjI3hh.png)

# Files

The following files are updated (or empty) with the evidence or ghost type:
- evidence1.txt
- evidence2.txt
- evidence3.txt
- possibleghosts.txt
- resolved_ghost.txt
- ghost_name.txt

The following files can be used as browser source with updated images for evidence:
- ev1.html
- ev2.html
- ev3.html

# Changes
- 2.0.3
	- Added New Ghost Types: Thaye, Moroi, Deogen
- 2.0.2
	- Added New Ghost Types: The Mimic
- 2.0.1
	- Added New Ghost Types: Twins, Raiju, Onryo, and Obake
- 2.0.0
  - Added support for image overlays! Now you can piecemeal this overlay how you would like with images or text.

- 1.2.0
	- Added two ghost types: The Goryo and Myling
	- Added ghostinfo command
	- Added possible ghost text
	- Updated all evidence to match the reshuffling of evidence
	- updated descriptions with the new evidence types

- 1.1.0
  - Added new ghosts: Hantu and Yokai

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
- https://www.twitch.tv/GreatisNate (For adding visible evidence images via browser source, and adding new ghosts)

# Installation instructions (overlay + text)

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

# Installation instructions (images)

***Follow the above instructions first***

1) Right click the PhasmophobiaSolver script and choose 'Insert API key'

![](https://i.imgur.com/0IjZNpC.png)

2) Add three browser sources in your OBS (Ev1.html, Ev2.html, Ev3.html)
   1) Create browser source
   2) Check "Local file" checkbox
   3) Select the .html file
   4) Set the width/height to 500px (the .html assumes this size, you can resize the browser source though)

![](https://i.imgur.com/mZI5Iad.png)

# License

The MIT License (MIT) Copyright (c) 2021 Martijn Stolk
