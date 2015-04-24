import lights
import effects

class MidiListener:
    CHANNEL_BAJO = 1
    CHANNEL_BATERIA = 2
    CHANNEL_LEAP_MOTION = 3

    GROUP_BATERIA = 1
    GROUP_LEAP_MOTION = 2

    def __init__(self):
        self.actualBateriaNote = 0
        self.lightsController = EffectsController()

    def receiveMidi(self, midi):
        note = midi.getNoteNumber()
        velocity = midi.getVelocity()

        if midi.isNoteOn():
            if self.isPiano(midi):
                self.lightsController.colorFlicker(note, MidiListener.GROUP_LEAP_MOTION)

            elif self.isBateria(midi):
                self.lightsController.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
                if self.actualBateriaNote != note:
                    self.actualBateriaNote = note
                    #change gamma
                    self.lightsController.changeGamma(note, MidiListener.GROUP_BATERIA)


    def isPiano(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() < 40

    def isBateria(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_BATERIA

    def isDjWii(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=40 and midi.getNoteNumber() < 80

    def isDjWub(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=80


class EffectsController:
    def __init__(self):
        emulator = lights.EmulatorImpl("172.16.22.19", "8000")
        emulator.setLightOn(True,0)
        self.effectsController = effects.Effects(emulator)

    def changeGamma(self, note, group):
        print "GROUP: " + str(group) +" Changing gamma to: " + str(note)
        self.effectsController.changeColorGamma(note, group)
    def changeIntensity(self,intensity, group):
        print "GROUP: " + str(group) +" Changing intensity to: " + str(intensity + 50)
        self.effectsController.changeIntensity(intensity + 50, group)
    def colorFlicker(self, note, group):
        print "GROUP: " + str(group) + " Sending flicker. note " + str(note)