import requests, lights, effects

class LightsClient :
	
	def changeIntensity(velocity, group): pass
	def changeColorGamma(velocity, group): pass
	def colorFlicker(note, group): pass
	def wiii(note, velocity, group): pass
	def wub(note, velocity, group): pass

class LightsRestClient(LightsClient) :

	def __init__(self, host, port):
		self._host = host
		self._port = port

	def changeIntensity(self, velocity, group) :
		payload = { "velocity" : velocity }
		self._executeCommand(payload, "intensity", group)

	def changeColorGamma(self, note, group) :
		payload = { "note" : note }
		self._executeCommand(payload, "gamma", group)

	def colorFlicker(self, note, group) :
		payload = { "note" : note }
		self._executeCommand(payload, "flicker", group)

	def wiii(self, note, velocity, group) :
		payload = { "note" : note, "velocity" : velocity }
		self._executeCommand(payload, "wiii", group)

	def wub(self, note, velocity, group) :
		payload = { "note" : note, "velocity" : velocity }
		self._executeCommand(payload, "wub", group)

	def _executeCommand(self, payload, commandName, group) :
		requests.put("http://" + self._host + ":" + self._port + "/api/effects/" + str(group) + "/"+commandName, json = payload)


class LightsLocalClient(LightsClient) :

	EMULATOR = 0
	REAL_SETUP = 1 

	def __init__(self, host, port, clientType) :
		if clientType == self.REAL_SETUP :
			self._lightsController = lights.MilightController(host, port)
		else :
			self._lightsController = lights.EmulatorController(host, port)
		self._lightsController.setLightOn(True,1)
		self._effectsController = effects.Effects(self._lightsController)

	def changeIntensity(self, velocity, group) :
		self._effectsController.changeIntensity(velocity, group)

	def changeColorGamma(self, note, group) :
		self._effectsController.changeColorGamma(note, group)

	def colorFlicker(self, note, group) :
		self._effectsController.colorFlicker(note, group)

	def wiii(self, note, velocity, group) :
		self._effectsController.wiii(note, velocity, group)

	def wub(self, note, velocity, group) :
		self._effectsController.wub(note, velocity, group)
