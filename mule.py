import sys
sys.path.append('/Users/federicoamdan/Projects/hackathon/muletallica')
sys.path.append('/Library/Python/2.7/site-packages/requests-2.6.2-py2.7.egg')
sys.path.append('/Library/Python/2.7/site-packages')
import json
import lights,effects
#print sys.path

def newMessage(self):
    return str(bytearray([self._b1, self._b2, 0x55]))

import milight
milight.Command.message = newMessage

print command
print group
print payload

COMMAND_GAMMA = '0'
COMMAND_FLICKER = '1'
COMMAND_INTENSITY = '2'
COMMAND_WIII = '3'
COMMAND_WUB = '4'

emulator = lights.MilightController("192.168.43.3", "8899")
effectsController = effects.Effects(emulator)

if command == COMMAND_GAMMA:
    print 'command gamma received'
    bodyObject = json.loads(payload)
    note = bodyObject['note']
    effectsController.changeColorGamma(note, int(group))
if command == COMMAND_FLICKER:
    print 'command flicker received'
    bodyObject = json.loads(payload)
    note = bodyObject['note']
    effectsController.colorFlicker(note, int(group))
if command == COMMAND_INTENSITY:
    print 'command intensity received'
    bodyObject = json.loads(payload)
    velocity = bodyObject['velocity']
    effectsController.changeIntensity(velocity, int(group))
if command == COMMAND_WIII:
    print 'command wiii received'
    bodyObject = json.loads(payload)
    note = bodyObject['note']
    velocity = bodyObject['velocity']
    effectsController.wiii(note, velocity, int(group))
if command == COMMAND_WUB:
    print 'command wub received'
    bodyObject = json.loads(payload)
    note = bodyObject['note']
    print 'note' + str(note)
    velocity = bodyObject['velocity']
    print 'velocity' + str(velocity)
    effectsController.wub(note, velocity, int(group))
