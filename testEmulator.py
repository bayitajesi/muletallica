import sys
import lightsclient
import random
import time
import midilistener

def main() :
	if len(sys.argv) > 1 and sys.argv[1] == 'rest' :
		lightsClient = lightsclient.LightsRestClient("127.0.0.1", "8081")
	else :
		lightsClient = lightsclient.LightsLocalClient("127.0.0.1", "8000", lightsclient.LightsLocalClient.EMULATOR)
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


if __name__ == "__main__" :
	main()