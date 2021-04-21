#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	dir(Parent)
except:
	class Parent:
		@staticmethod
		def Log(p1, p2):
			pass

		@staticmethod
		def SendStreamMessage(p1):
			pass

		@staticmethod
		def SendStreamWhisper(p1, p2):
			pass

		@staticmethod
		def GetRequest(url, p2):
			return ''

		@staticmethod
		def GetChannelName():
			return ''

		@staticmethod
		def GetRandom(min,max):
			return 0

try:
	dir(Data)
except:
	class Data:

		User = "",
		UserName = "",
		Message = "",
		RawData = "",
		ServiceType = ""

		@staticmethod
		def IsChatMessage():
			return False

		@staticmethod
		def IsRawData():
			return False

		@staticmethod
		def IsFromTwitch():
			return False

		@staticmethod
		def IsFromYoutube():
			return False

		@staticmethod
		def IsFromMixer():
			return False

		@staticmethod
		def IsFromDiscord():
			return False

		@staticmethod
		def IsWhisper():
			return False

		@staticmethod
		def GetParam(id):
			return ''

		@staticmethod
		def GetParamCount():
			return 0
