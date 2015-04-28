import lights
import random
import time
import effects

def main() :
	#emulator = lights.MilightImpl("192.168.43.3", "8899")
	emulator = lights.EmulatorController("127.0.0.1", "8000")
	effectsController = effects.Effects(emulator)

	emulator.setLightOn(False, 0)
	time.sleep(1)
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

if __name__ == "__main__" :
	main()

