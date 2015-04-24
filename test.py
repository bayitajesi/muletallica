import lights
import random
import time
import effects

def main() :
	emulator = lights.EmulatorImpl("172.16.21.88", "8000")
	effectsController = effects.Effects(emulator)

	'''emulator.setLightOn(False, 0)
	time.sleep(1)
	for group in range(1, 5):
		emulator.setLight([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 254, group)
		time.sleep(0.2)
		emulator.setLightOn(False, group)
		time.sleep(0.2)
		emulator.setLightOn(True, group)
		time.sleep(0.2)'''

	emulator.setLightOn(False, 0)
	time.sleep(1)
	effectsController.changeColorGamma(0, 1)
	'''effectsController.changeIntensity(75, 1)
	effectsController.changeIntensity(50, 1)
	effectsController.changeIntensity(25, 1)
	effectsController.changeIntensity(10, 1)'''

if __name__ == "__main__" :
	main()

