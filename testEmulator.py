import lights
import random
import time
import effects

def main() :
	emulator = lights.EmulatorController("127.0.0.1", "8000")
	effectsController = effects.Effects(emulator)

	emulator.setLightOn(False, 0)
	'''time.sleep(1)
	for group in range(1, 5):
		emulator.setLight([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 254, group)
		time.sleep(0.2)
		emulator.setLightOn(False, group)
		time.sleep(0.2)
		emulator.setLightOn(True, group)
		time.sleep(0.2)

	emulator.setLightOn(False, 0)
	time.sleep(1)
	emulator.setLightOn(True, 1)
	effectsController.changeColorGamma(0, 1)
	time.sleep(1)
	effectsController.changeIntensity(127, 1)
	time.sleep(0.1)
	effectsController.changeIntensity(90, 1)
	time.sleep(0.1)
	effectsController.changeIntensity(50, 1)
	time.sleep(0.1)
	effectsController.changeIntensity(30, 1)

	effectsController.changeIntensity(127, 1)'''
	emulator.setLightOn(False, 0)

	effectsController.colorFlicker(0, 0)
	effectsController.colorFlicker(10, 0)
	effectsController.colorFlicker(20, 0)
	effectsController.colorFlicker(30, 0)

	effectsController.colorFlicker(40, 0)
	effectsController.colorFlicker(50, 0)
	effectsController.colorFlicker(60, 0)

if __name__ == "__main__" :
	main()

