import lights, time

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
		else : 
			self._lights.setColor([123, 9, 237], group)

	def changeIntensity(self, velocity, group) : 
		self._lights.setBrightness(velocity, group)

	def colorFlicker(self, note, group) : 
		r, g, b = self._transformNoteInColor(note)
		self._lights.setLight([r, g, b], 127, group)
		self._lights.setLightFade(True, group)
		time.sleep(0.1)
		self._lights.setLightFade(False, group)
		time.sleep(0.1)

    # def wiii(self, note, velocity, group) : pass

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
		print str(r) + ', ' + str(g) + ', ' + str(b)
		return r, g, b
