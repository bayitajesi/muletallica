import lights
import random
import time

def main() :
	emulator = lights.EmulatorImpl("172.16.21.88", "8000")

	emulator.setLightOn(False, 0)
	time.sleep(1)
	for group in range(1, 5):
		emulator.setLight([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 254, group)
		time.sleep(0.2)
		emulator.setLightOn(False, group)
		time.sleep(0.2)
		emulator.setLightOn(True, group)
		time.sleep(0.2)

if __name__ == "__main__" :
	main()

