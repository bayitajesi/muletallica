import requests
import milight

class Lights :

	def __init__(self, host, port) :
		self._host = host
		self._port = port

	def setLight(self, rgb, brightness, group) : pass
	def setLightOn(on, group) : pass
	def setLightFade(up, group) : pass

class MilightImpl(Lights) : 

	def __init__(self, host, port) :
		super(MilightImpl, self).__init__(host, port)
		self._controller = milight.MiLight({'host': self._host, 'port': int(self._port)}, wait_duration=0) #Create a controller with 0 wait between commands
		self._light = milight.LightBulb(['rgbw'])

	def setLight(self, rgb, brightness, group) : 
		self._controller.send(self._light.color(milight.color_from_rgb(*rgb), group))

	def setLightOn(self, on, group) :
		if on :
			self._controller.send(self._light.on(group))
		else :
			self._controller.send(self._light.off(group))

	def setLightFade(self, up, group) : 
		if up :
			self._controller.send(self._light.fade_up(group))
		else :
			self._controller.send(self._light.fade_down(group))


class EmulatorImpl(Lights) :

	def setLight(self, rgb, brightness, group) : 
		groupString = "" if group == 0 else str(group)
		x, y = self.from_rgb_to_xy(*rgb)
		payload = { "xy":[x, y], "on": True, "bri": brightness}
		requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/"+ groupString +"/state", json = payload)

	def setLightOn(self, on, group) :
		payload = { "on": on }
		if group == 0 :
			requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/1/state", json = payload)
			requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/2/state", json = payload)
			requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/3/state", json = payload)
			requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/4/state", json = payload)
		else :
			requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/groups/"+ str(group) +"/state", json = payload)

	def setLightFade(self, on, group) : 
		groupString = "" if group == 0 else str(group)
		payload = { "on": on }
		requests.put("http://" + self._host + ":" + self._port + "/api/newdeveloper/lights/"+ groupString +"/state", json = payload)



	def from_rgb_to_xy (self, red, green, blue) :

		convertedRed = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
		convertedGreen = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
		convertedBlue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

		X = convertedRed * 0.649926 + convertedGreen * 0.103455 + convertedBlue * 0.197109
		Y = convertedRed * 0.234327 + convertedGreen * 0.743075 + convertedBlue * 0.022598
		Z = convertedRed * 0.0000000 + convertedGreen * 0.053077 + convertedBlue * 1.035763

		x = X / (X + Y + Z)
		y = Y / (X + Y + Z)

		return x, y



