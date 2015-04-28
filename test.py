import lights
import random
import time
import effects

def main() :
	#emulator = lights.MilightImpl("192.168.43.3", "8899")
	emulator = lights.MilightController("192.168.43.3", "8899")
	effectsController = effects.Effects(emulator)

	emulator.setLightOn(False, 0)
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
	emulator.setLightOn(True, 0)
	effectsController.changeColorGamma(3, 0)
	time.sleep(1)
	effectsController.changeIntensity(127, 0)
	time.sleep(0.1)
	effectsController.changeIntensity(90, 0)
	time.sleep(0.1)
	effectsController.changeIntensity(50, 0)
	time.sleep(0.1)
	effectsController.changeIntensity(30, 0)

	emulator.setLightOn(False, 0)

	effectsController.colorFlicker(0, 0)
	effectsController.colorFlicker(10, 0)
	effectsController.colorFlicker(20, 0)
	effectsController.colorFlicker(30, 0)

	effectsController.colorFlicker(39, 0)
	effectsController.colorFlicker(50, 0)
	effectsController.colorFlicker(60, 0)

	effectsController.colorFlicker(70, 0)
	effectsController.colorFlicker(80, 0)
	effectsController.colorFlicker(90, 0)

	effectsController.colorFlicker(100, 0)
	effectsController.colorFlicker(110, 0)
	effectsController.colorFlicker(120, 0)
if __name__ == "__main__" :
	main()

