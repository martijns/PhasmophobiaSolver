# About

Phasmophobia Solver lets your chat help keep track of collected evidence. When evidence is collected and the bot is updated, the
bot will inform chat of the remaining possibilities. Users can also type the !<ghosttype> to get more information about the ghosts.

Textfiles are updated in order to display the contents on stream.
HTML files are updated if you'd like to display and image on stream as a browser source, recommended 500 x 500 size

If you'd like to use your own image, simply replace the image in the file as a png (recommend 500px x 500px with transparency) 

# Commands

The following commands are available:
- !ghostname - set the name of the ghost
- !ev1 - set evidence #1
- !ev2 - set evidence #2
- !ev3 - set evidence #3
- !ghostinfo Get a list of the ghost name and current evidence, with possible ghosts left
- !evreset - reset evidence

# Files

The following files are updated (or empty) with the evidence or ghost type:
- evidence1.txt
- evidence2.txt
- evidence3.txt
- possibleghosts.txt
- resolved_ghost.txt
- ghost_name.txt

These files are updated for the image overlay:
- ev1.html
- ev2.html
- ev3.html

# Changes
- 2.0
	-Added support for image overlays! Now you can piecemeal this overlay how you would like with images or text.

- 1.2
	-Added two ghost types; The Goryo and Myling, added ghostinfo command, added possible ghost text, updated all evidence to match the reshuffling of evidence, updated descriptions with the new evidence types.

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

# License

The MIT License (MIT) Copyright (c) 2021 Martijn Stolk
