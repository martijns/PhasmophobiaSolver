#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Phasmophobia Solver """

#---------------------------------------
# Script Import Libraries
#---------------------------------------
import clr
clr.AddReference("IronPython.Modules.dll")

import os
import codecs
import json
import re
try:
    from streamlabs_stub import *
except:
    pass

#---------------------------------------
# Script Information
#---------------------------------------
ScriptName = "Phasmophobia Solver"
Website = "https://github.com/martijns"
Description = "Let your chat indicate evidence and the script will find the matching ghost"
Creator = "netripper"
Version = "2.0.3"
SpecialThanks = "https://www.twitch.tv/itspatokay" # The streamer that provided the idea
SpecialThanks2 = "https://www.twitch.tv/kruiser8" # This script will look slightly familiar to RaidNotify of kruiser8, since it's my first script and I used their script as starting point

#---------------------------------------
# Script Variables
#---------------------------------------

# Settings file location
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

# Raider file location
Evidence1File = os.path.join(os.path.dirname(__file__), "files", "evidence1.txt")
Evidence2File = os.path.join(os.path.dirname(__file__), "files", "evidence2.txt")
Evidence3File = os.path.join(os.path.dirname(__file__), "files", "evidence3.txt")
ResolvedGhostFile = os.path.join(os.path.dirname(__file__), "files", "resolved_ghost.txt")
GhostNameFile = os.path.join(os.path.dirname(__file__), "files", "ghost_name.txt")
PossibleGhostsFile = os.path.join(os.path.dirname(__file__), "files", "possible_ghosts.txt")
#---------------------------------------
# Script Classes
#---------------------------------------
class Settings(object):
    """ Load in saved settings file if available else set default values. """
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            pass

    def Reload(self, jsondata):
        """ Reload settings from Streamlabs user interface by given json data. """
        self.__dict__ = json.loads(jsondata, encoding="utf-8")

    def Save(self, settingsfile):
        """ Save settings contained within to .json and .js settings files. """
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8", ensure_ascii=False)
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8', ensure_ascii=False)))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")

#---------------------------------------
# Phasmophobia-stuff
#---------------------------------------
class Evidence:
    EMF_LEVEL_5 = 'EMF Level 5'
    GHOST_ORBS = 'Ghost Orbs'
    GHOST_WRITING = 'Ghost Writing'
    FREEZING_TEMPS = 'Freezing Temps'
    SPIRIT_BOX = 'Spirit Box'
    FINGERPRINTS = 'Fingerprints'
    DOTS_PROJECTOR = 'DOTS Projector'

EVIDENCES = [Evidence.EMF_LEVEL_5, Evidence.GHOST_ORBS, Evidence.GHOST_WRITING, Evidence.FREEZING_TEMPS, Evidence.SPIRIT_BOX, Evidence.FINGERPRINTS, Evidence.DOTS_PROJECTOR]

GHOSTS = {
    'Shade': [Evidence.EMF_LEVEL_5, Evidence.FREEZING_TEMPS, Evidence.GHOST_WRITING],
    'Phantom': [Evidence.SPIRIT_BOX, Evidence.FINGERPRINTS, Evidence.DOTS_PROJECTOR],
    'Jinn': [Evidence.EMF_LEVEL_5, Evidence.FREEZING_TEMPS, Evidence.FINGERPRINTS],
    'Yurei': [Evidence.GHOST_ORBS, Evidence.DOTS_PROJECTOR, Evidence.FREEZING_TEMPS],
    'Mare': [Evidence.GHOST_ORBS, Evidence.GHOST_WRITING, Evidence.SPIRIT_BOX],
    'Demon': [Evidence.GHOST_WRITING, Evidence.FREEZING_TEMPS, Evidence.FINGERPRINTS],
    'Banshee': [Evidence.DOTS_PROJECTOR, Evidence.GHOST_ORBS, Evidence.FINGERPRINTS],
    'Revenant': [Evidence.GHOST_ORBS, Evidence.GHOST_WRITING, Evidence.FREEZING_TEMPS],
    'Oni': [Evidence.EMF_LEVEL_5, Evidence.FREEZING_TEMPS, Evidence.DOTS_PROJECTOR],
    'Poltergeist': [Evidence.GHOST_WRITING, Evidence.SPIRIT_BOX, Evidence.FINGERPRINTS],
    'Spirit': [Evidence.EMF_LEVEL_5, Evidence.GHOST_WRITING, Evidence.SPIRIT_BOX],
    'Wraith': [Evidence.EMF_LEVEL_5, Evidence.SPIRIT_BOX, Evidence.DOTS_PROJECTOR],
    'Yokai': [Evidence.GHOST_ORBS, Evidence.SPIRIT_BOX, Evidence.DOTS_PROJECTOR],
    'Hantu': [Evidence.FINGERPRINTS, Evidence.FREEZING_TEMPS, Evidence.GHOST_ORBS],
    'Myling': [Evidence.FINGERPRINTS, Evidence.EMF_LEVEL_5, Evidence.GHOST_WRITING],
    'Goryo': [Evidence.EMF_LEVEL_5, Evidence.FINGERPRINTS, Evidence.DOTS_PROJECTOR],
    'Twins': [Evidence.EMF_LEVEL_5, Evidence.SPIRIT_BOX, Evidence.FREEZING_TEMPS],
    'Raiju': [Evidence.EMF_LEVEL_5, Evidence.GHOST_ORBS, Evidence.DOTS_PROJECTOR],
    'Onryo': [Evidence.SPIRIT_BOX, Evidence.GHOST_ORBS, Evidence.FREEZING_TEMPS],
    'Obake': [Evidence.EMF_LEVEL_5, Evidence.FINGERPRINTS, Evidence.GHOST_ORBS],
    'Mimic': [Evidence.SPIRIT_BOX, Evidence.FINGERPRINTS, Evidence.FREEZING_TEMPS],
    'Thaye': [Evidence.GHOST_ORBS, Evidence.GHOST_WRITING, Evidence.DOTS_PROJECTOR],
    'Deogen': [Evidence.SPIRIT_BOX, Evidence.GHOST_WRITING, Evidence.DOTS_PROJECTOR],
    'Moroi': [Evidence.SPIRIT_BOX, Evidence.GHOST_WRITING, Evidence.FREEZING_TEMPS]
}

GHOSTINFO = {
    'Shade': 'A Shade is known to be a Shy Ghost. There is evidence that a Shade will stop all paranormal activity if there are multiple people nearby. Unique Strengths: Being shy means the Ghost will be harder to find. Weaknesses: The Ghost will not enter hunting mode if there is multiple people nearby. Evidence: EMF 5, Ghost Writing, Freezing Temperatures',
    'Phantom': 'A spirit is the most common Ghost you will come across however it is still very powerful and dangerous. They are usually discovered at one of their hunting grounds after an unexplained death. Unique Strengths: Looking at a Phantom will considerably drop your sanity. Weaknesses: Taking a photo of the Phantom will make it temporarily disappear. Evidence: Spirit Box, Fingerprints, DOTS Projector',
    'Jinn': 'A Jinn is territorial Ghost that will attack when threatened. It has also been known to be able to travel at significant speed. Unique Strengths: A Jinn will travel at a faster speed if it\'s victim is far away. Weaknesses: Turning off the locations power source will prevent the Jinn from using it\'s ability. Evidence: EMF Level 5, Freezing Temperatures, Fingerprint',
    'Yurei': 'A Yurei is a Ghost that has returned to the physical world, usually for the purpose of revenge or hatred. Unique Strengths: Yurei\'s have been known to have a stronger effect on people\'s sanity. Weaknesses: Smudging the Yurei\'s room will cause it to not wander around the location for a long time. Evidence: Ghost Orbs, Freezing Temperatures, DOTS Projector',
    'Mare': 'A Mare is the source of all nightmares, making it most powerful in the dark. Unique Strengths: A Mare will have an increased chance to attack in the dark. Weaknesses: Turning the lights on around the Mare will lower it\'s chance to attack. Evidence: Ghost Orbs, Ghost Writing, Spirit Box',
    'Demon': 'A Demon is one of the worst Ghosts you can encounter. It has been known to attack without a reason. Unique Strengths: Demons will attack more often then any other Ghost. Weaknesses: Asking a Demon successful questions on the Ouija Board won\'t lower the users sanity. Evidence: Freezing Temperatures, Ghost Writing, Fingerprints',
    'Banshee': 'A Banshee is a natural hunter and will attack anything. It has been known to stalk it\'s prey one at a time until making it\'s kill. Unique Strengths: A Banshee will only target one person at a time. Weaknesses: Banshees fear the Crucifix and will be less aggressive when near one. Evidence: Ghost Orbs, Fingerprints, DOTS Projector',
    'Revenant': 'A Revenant is a slow but violent Ghost that will attack indiscriminately. It has been rumoured to travel at a significantly high speed when hunting. Unique Strengths: A Revenant will travel at a significantly faster speed when hunting a victim. Weaknesses: Hiding from the Revenant will cause it to move very slowly. Evidence: Ghost Orbs, Ghost Writing, Freezing Temperatures',
    'Oni': 'Oni\'s are a cousin to the Demon and possess the extreme strength. There have been rumours that they become more active around their prey. Unique Strengths: Oni\'s are more active when people are nearby and have been seen moving objects at great speed. Weaknesses: Being more active will make the Oni easier to find and identify. Evidence: EMF Level 5, Freezing Temperature, DOTS Projector',
    'Poltergeist': 'One of the most famous Ghosts, a Poltergeist, also known as a noisy ghost can manipulate objects around it to spread fear into it\'s victims. Unique Strengths: A Poltergeist can throw huge amounts of objects at once. Weaknesses: A Poltergeist is almost ineffective in an empty room. Evidence: Ghost Writing, Spirit Box, Fingerprints',
    'Spirit': 'A spirit is the most common Ghost you will come across however it is still very powerful and dangerous. They are usually discovered at one of their hunting grounds after an unexplained death. Unique Strengths: Nothing Weaknesses: Using Smudge Sticks on a Spirit will stop it attacking for a long period of time. Evidence: EMF Level 5, Ghost Writing, Spirit Box',
    'Wraith': 'A Wraith is one of the most dangerous Ghosts you will find. It is also the only known Ghost that has the ability of flight and has sometimes been known to travel through walls. Unique Strengths: Wraiths almost never touch the ground meaning it can\'t always be tracked by footsteps. Weaknesses: Wraiths have a toxic reaction to Salt. Evidence: EMF Level 5, Spirit Box, DOTS Projector',
    'Yokai': 'A common type of ghost that is attracted to human voices. They can usually be found haunting family homes. Unique Strengths: Talking near a Yokai will anger it and cause it to attack more often. Weaknesses: While hunting, it can only hear voices close to it Evidence: Ghost Orbs, Spirit Box, DOTS Projector',
    'Hantu': 'A rare ghost that can be found in hot climates. They are known to attack more often in cold weather. Unique Strengths: Moves faster in colder areas. Weaknesses: Moves slower in warmer areas. Evidence: Fingerprints, Ghost Orb, Freezing Temperatures',
    'Goryo': 'Using a video camera is the only way to view a Goryo, when it passes through a DOTS projector. Unique Strengths: A Goryo will usually only show itself on camera if there are no people nearby. Weaknesses: They are rarely seen far from their place of death. Evidence: EMF Level 5, Fingerprints, D.O.T.S. Projector',
    'Myling': 'A Myling is a very vocal and active ghost. They are rumoured to be quiet when hunting their prey. Unique Strengths: A Myling is known to be quieter when hunting. Weaknesses: Mylings more frequently make paranormal sounds. Evidence: EMF Level 5, Fingerprints, Ghost Writing',
    'Twins': 'These ghosts have been reported to mimic each other''s actions. They alternate their attacks to confuse their prey Strengths: Either Twin can be angered and initiate an attack on their prey. Weaknesses: The Twins will often interact with the environment at the same time.',
    'Raiju': 'A Raiju is a demon that thrives on electrical current. While generally calm, they can become agitated when overwhelmed with power. Strengths: A Raiju can siphon power from nearby electrical devices, making it move faster. Weaknesses: Raiju are constantly disrupting electronic equipment, making it easier to track when attacking.',
    'Onryo': 'The Onryo is often referred to as "The Wrathful Spirit." It steals souls from dying victims'' bodies to seek revenge. This ghost has been known to fear any form of fire, and will do anything to be far from it. Strength: Extinguishing a flame can cause an Onryo to attack. Weakness: When threatened, this ghost will be less likely to attack.',
    'Obake': 'Obake are terrifying shape-shifters, capable of taking on many forms. They have been seen taking on humanoid shapes to attract their prey. Strength: When interacting with the environment, an Obake will rarely leave a trace. Weakness: Sometimes this ghost will shapeshift, leaving behind unique evidence.',
    'Mimic':'The Mimic is an elusive, mysterious, copycat ghost that mirrors traits and behaviours from others, including other ghost types. Strength: We''re unsure what this ghost is capable of. Be careful. Weakness: Several reports have noted ghost orb sightings near mimics.',
    'Thaye': 'Thaye have been known to rapidly age over time, even in the afterlife. From what we''ve learned, they seem to deteriorate faster while within the presence of the living. Strength: Upon entering the location, Thaye will become active, defensive and agile Weakness: Thaye will weaken over time, making them weaker, slower and less aggressive',
    'Deogen': 'Sometimes surrounded by an endless fog, Deogen have been eluding ghost hunters for years. These ghosts have been reported to find even the most hidden prey, before stalking them into exhaustion. Strength: Deogen constantly sense the living. You can run but you can''t hide. Weakness: Deogen require a lot of energy to form and will move very slowly when approaching its victim.',
    'Moroi': 'Moroi have risen from the grave to drain energy from the living. They have been known to place curses on their victims, curable only by antidotes or moving very far away. Strength: The weaker their victims, the stronger the Moroi becomes. Weakness: Moroi suffer from hyperosmia, weakening them for longer periods.'
}

Evidence1 = None
Evidence2 = None
Evidence3 = None
GhostName = None

#---------------------------------------
# Script Functions
#---------------------------------------

def saveFile(filename, content):
    try:
        with open(filename, 'w') as writeFile:
            writeFile.write(content)
        Parent.Log(ScriptName, 'File {} updated with: {}'.format(filename, content))
    except Exception as e:
        Parent.Log(ScriptName, str(e.args))

def possibleGhosts():
    ghosts = GHOSTS.keys()
    global Evidence1, Evidence2, Evidence3
    if Evidence1:
        ghosts = [x for x in ghosts if Evidence1 in GHOSTS[x]]
    if Evidence2:
        ghosts = [x for x in ghosts if Evidence2 in GHOSTS[x]]
    if Evidence3:
        ghosts = [x for x in ghosts if Evidence3 in GHOSTS[x]]
    return ghosts
    
def possibleGhostDescriber():
    global ghostComboDescriptor
    ghosts = possibleGhosts()
    if len(ghosts) == 0:
        ghostComboDescriptor = 'No ghost for this combination'
        saveFile(ResolvedGhostFile, '')
    if len(ghosts) == 1:
        ghostComboDescriptor = 'Ghost must be a {}'.format(str.join(', ', ghosts or 'None'))
        saveFile(ResolvedGhostFile, ghosts[0] or '')
    if len(ghosts) > 1:
        ghostComboDescriptor = 'Ghost could be any of: {}'.format(str.join(', ', ghosts or 'None'))
        saveFile(ResolvedGhostFile, '')
    saveFile(PossibleGhostsFile, ghostComboDescriptor)
    return ghostComboDescriptor
    
def updateImage(evidence, eventName):
    global ImageData
    if(evidence == ''):
        ImageData = {"srclink": '', "height": 500 }
    else:
        ImageData = {"srclink": "Images\\" + evidence +".png", "height": 500 }
    Parent.BroadcastWsEvent(eventName,str(ImageData).replace("'",'"'))

#---------------------------------------
# Chatbot Initialize Function
#---------------------------------------
def Init():

    # Load settings from file and verify
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)

    # End of Init
    return

#---------------------------------------
# Chatbot Save Settings Function
#---------------------------------------
def ReloadSettings(jsondata):

    # Reload newly saved settings and verify
    ScriptSettings.Reload(jsondata)

    # End of ReloadSettings
    return

#---------------------------------------
# Chatbot Execute Function
#---------------------------------------
def Execute(data):

    if not data.IsChatMessage() or not data.IsFromTwitch() or data.IsWhisper():
        return

    global Evidence1, Evidence2, Evidence3, GhostName

    # Set first evidence with !ev1
    if data.GetParam(0).lower() in ['!ev1']:
        param = str.join(' ', data.Message.split(' ')[1:]).lower()
        if param:
            Evidence1 = next(iter([x for x in EVIDENCES if x.lower().startswith(param) or x.lower().endswith(param) or param in x.lower()] or []), None)
            if Evidence1:
                saveFile(Evidence1File, Evidence1 or '')
                updateImage(Evidence1 or '','ev1Image')
                Parent.SendStreamMessage("/me [PS] Evidence #1 set to {}. {}".format(Evidence1, possibleGhostDescriber()))
            else:
                Parent.SendStreamMessage("/me [PS] Couldn't find this type of evidence, pick from: {}".format(str.join(', ', EVIDENCES)))
        else:
            Parent.SendStreamMessage("/me [PS] Evidence #1 is currently {}, but can be any of: {}".format(Evidence1, str.join(', ', EVIDENCES)))

    # Set second evidence with !ev2
    if data.GetParam(0).lower() in ['!ev2']:
        param = str.join(' ', data.Message.split(' ')[1:]).lower()
        if param:
            Evidence2 = next(iter([x for x in EVIDENCES if x.lower().startswith(param) or x.lower().endswith(param) or param in x.lower()] or []), None)
            if Evidence2:
                saveFile(Evidence2File, Evidence2 or '')
                updateImage(Evidence2 or '','ev2Image')
                Parent.SendStreamMessage("/me [PS] Evidence #2 set to {}. {}".format(Evidence2, possibleGhostDescriber()))
            else:
                Parent.SendStreamMessage("/me [PS] Couldn't find this type of evidence, pick from: {}".format(str.join(', ', EVIDENCES)))
        else:
            Parent.SendStreamMessage("/me [PS] Evidence #2 is currently {}, but can be any of: {}".format(Evidence2, str.join(', ', EVIDENCES)))

    # Set third evidence with !ev3
    if data.GetParam(0).lower() in ['!ev3']:
        param = str.join(' ', data.Message.split(' ')[1:]).lower()
        if param:
            Evidence3 = next(iter([x for x in EVIDENCES if x.lower().startswith(param) or x.lower().endswith(param) or param in x.lower()] or []), None)
            if Evidence3:
                saveFile(Evidence3File, Evidence3 or '')
                updateImage(Evidence3 or '','ev3Image')
                Parent.SendStreamMessage("/me [PS] Evidence #3 set to {}. {}".format(Evidence3, possibleGhostDescriber()))
            else:
                Parent.SendStreamMessage("/me [PS] Couldn't find this type of evidence, pick from: {}".format(str.join(', ', EVIDENCES)))
        else:
            Parent.SendStreamMessage("/me [PS] Evidence #3 is currently {}, but can be any of: {}".format(Evidence3, str.join(', ', EVIDENCES)))

    if data.GetParam(0).lower() in ['!ghostname']:
        param = str.join(' ', data.Message.split(' ')[1:])
        if param:
            GhostName = param
            saveFile(GhostNameFile, param or '')
            Parent.SendStreamMessage("/me [PS] Name updated!")
        else:
            Parent.SendStreamMessage("/me [PS] Name's currently: {}".format(GhostName))


# Grab the info as it stands right now
    if data.GetParam(0).lower() in ['!ghostinfo']:
        Parent.SendStreamMessage("/me [PS] Name's currently: {}. Evidence #1 is {}, Evidence #2 is {}, Evidence #3 is {}. {}".format(GhostName, Evidence1, Evidence2, Evidence3, possibleGhostDescriber()))

    # Allow reset with '!evreset'
    if data.GetParam(0).lower() in ['!evreset']:
        Evidence1 = None
        Evidence2 = None
        Evidence3 = None
        GhostName = None
        saveFile(Evidence1File, '')
        saveFile(Evidence2File, '')
        saveFile(Evidence3File, '')
        saveFile(ResolvedGhostFile, '')
        saveFile(GhostNameFile, '')
        saveFile(PossibleGhostsFile,'')
        updateImage('','ev1Image')
        updateImage('','ev2Image')
        updateImage('','ev3Image')
        Parent.SendStreamMessage("/me [PS] Cleared")

    # Respond to stuff like !banshee
    if data.GetParam(0).startswith('!') and data.GetParam(0).lower()[1:] in [x.lower() for x in GHOSTINFO.keys()]:
        query = data.GetParam(0).lower()[1:]
        ghostname = next(iter([x for x in GHOSTINFO.keys() if x.lower() == query] or []), None)
        info = GHOSTINFO[ghostname]
        Parent.SendStreamMessage("/me [PS] {}: {}".format(ghostname, info))

#---------------------------------------
# Chatbot Tick Function
#---------------------------------------
def Tick():
    pass

#---------------------------------------
# Chatbot Button Function
#---------------------------------------
def OpenReadMe():
    """Open the README.txt in the scripts folder"""
    os.startfile(os.path.join(os.path.dirname(__file__), "README.txt"))

def OpenOutputFiles():
    """Open output folder"""
    os.startfile(os.path.join(os.path.dirname(__file__), "files"))
