import sys
import lightsclient
import random
import time
import midilistener

def main() :
	if len(sys.argv) > 1 and sys.argv[1] == 'rest' :
		lightsClient = lightsclient.LightsRestClient("127.0.0.1", "8081")
	else :
		lightsClient = lightsclient.LightsLocalClient("192.168.43.3", "8899", lightsclient.LightsLocalClient.REAL_SETUP)
		lightsController = lightsClient._lightsController
		lightsController.setLightOn(False, 0)
	'''time.sleep(1)
	for group in range(1, 2):
		emulator.setLight([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 254, group)
		time.sleep(0.2)
		emulator.setLightOn(False, group)
		time.sleep(0.2)
		emulator.setLightOn(True, group)
		time.sleep(0.2)'''

	#emulator.setLightOn(False, 0)
	#time.sleep(1)
	#lightsController.setLightOn(True, 0)
	lightsClient.changeColorGamma(3, 0)
	time.sleep(1)
	lightsClient.changeIntensity(127, 0)
	time.sleep(0.1)
	lightsClient.changeIntensity(90, 0)
	time.sleep(0.1)
	lightsClient.changeIntensity(50, 0)
	time.sleep(0.1)
	lightsClient.changeIntensity(30, 0)

	#lightsController.setLightOn(False, 0)

	lightsClient.colorFlicker(0, 0)
	lightsClient.colorFlicker(10, 0)
	lightsClient.colorFlicker(20, 0)
	lightsClient.colorFlicker(30, 0)

	lightsClient.colorFlicker(39, 0)
	lightsClient.colorFlicker(50, 0)
	lightsClient.colorFlicker(60, 0)

	lightsClient.colorFlicker(70, 0)
	lightsClient.colorFlicker(80, 0)
	lightsClient.colorFlicker(90, 0)

	lightsClient.colorFlicker(100, 0)
	lightsClient.colorFlicker(110, 0)
	lightsClient.colorFlicker(120, 0)

def test_listener():
	midiListener = midilistener.MidiListener(1)
	midiListener.start()

	for i in xrange(1000):
		m = createMidi()
		time.sleep(0.025)
		midiListener.receiveMidi(m)

def createMidi():
	channel = random.randint(2, 3)
	if channel == 2:
		note_number = 1 if random.randint(1, 100) > 10 else 2
	else:
		note_number = random.randint(1, 40)

	velocity = random.randint(1, 127)
	return Midi(channel, note_number, velocity)

class Midi(object):

	def __init__(self, channel, note_number, velocity):
		self.channel = channel
		self.note_number = note_number
		self.velocity = velocity

	def getNoteNumber(self):
		return self.note_number

	def getVelocity(self):
		return self.velocity

	def getChannel(self):
		return self.channel

	def isNoteOn(self):
		return True

	def __str__(self):
		return "Midi(channel: %s, note: %s, velocity: %s)" % (self.channel, self.note_number, self.velocity)

if __name__ == "__main__" :
	test_listener()

