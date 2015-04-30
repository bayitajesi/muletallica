import lights, time
import random

class Effects :

	def __init__(self, lights) :
		self._lights = lights

	def changeColorGamma(self, note, group) :
		if note == 0 :
			self._lights.setColor([245, 135, 10], group)
		elif note == 1 : 
			self._lights.setColor([245, 10, 159], group)
		elif note == 2 : 
			self._lights.setColor([9, 237, 237], group)
		elif note == 3: 
			self._lights.setColor([123, 9, 237], group)

	def changeIntensity(self, velocity, group) : 
		self._lights.setBrightness(velocity, group)

	def colorFlicker(self, note, group) : 
		r, g, b = self._transformNoteInColor(note)
		self._lights.setColor([r, g, b], group)
		self._lights.setLightOn(True, group)
		self._lights.setLightOn(False, group)

	def wiii(self, note, velocity, group):
		self._lights.setLightOn(True, group)
		if note >= 40 and note <= 50:
			r, g, b = self._transformNoteInColor(note)
			self._lights.setLight([r, g, b], velocity, group)
		elif note == 69:
			random_note = random.randint(0, 127)
			r, g, b = self._transformNoteInColor(random_note)
			self._lights.setLight([r, g, b], velocity, group)

	def wub(self, note, valocity, group):
		if note >= 80 and note <= 127:
			r, g, b = self._transformNoteInColor(note)
			self._lights.setLight([r, g, b], velocity, group)

	def _transformNoteInColor(self, note) :
		if note < 21 :
			r = 255 - note
			g = int(note*255/21.0)
			b = 0
		elif note >= 21 and note < 42 :
			r = 255 - int((note-21)*255/21.0)
			g = 255 - (note - 21)
			b = 0
		elif note >= 42 and note < 63 :
			r = 0
			g = 255 - (note - 42)
			b = int((note-42)*255/21.0)
		elif note >= 63 and note < 84 :
			r = 0
			g = 255 - int((note-63)*255/21.0)
			b = 255 - (note - 63)
		elif note >= 84 and note < 105 :
			r = int((note-84)*255/21.0)
			g = 0
			b = 255 - (note - 84)
		elif note >= 105 and note < 128 :
			r = 255 - (note - 105)
			g = 0
			b = 255 - int((note-105)*255/21.0)
		return r, g, b
