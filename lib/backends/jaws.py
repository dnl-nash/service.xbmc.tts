# -*- coding: utf-8 -*-

import sys
from base import ThreadedTTSBackend

class JAWSTTSBackend(ThreadedTTSBackend):
	provider = 'JAWS'
	displayName = 'JAWS'
	interval = 50
	def __init__(self):
		import comtypes.client
		try:
			self.jaws = comtypes.client.CreateObject('FreedomSci.JawsApi')
		except:
			self.jaws = comtypes.client.CreateObject('jfwapi')
		self.threadedInit()
		
	def threadedSay(self,text):
		if not self.jaws: return
		self.jaws.SayString(text,False) #Say text, do not interrupt
		
	def stop(self):
		if not self.jaws: return
		self.jaws.StopSpeech()

		
	def close(self):
		del self.jaws
		self.jaws = None
		
	@staticmethod
	def available():
		if not sys.platform.lower().startswith('win'): return False
		try:
			import comtypes
			comtypes.GUID.from_progid('FreedomSci.JawsApi') #If we fail on this, we haven't loaded anything
			import comtypes.client
			test = comtypes.client.CreateObject("FreedomSci.JawsApi")
			return test.SayString("",False)
		except:
			return False
		return True