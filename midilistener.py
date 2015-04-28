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
        self.lightsController = lights.LightsController()
        emulator = lights.MilightController("192.168.43.3", "8899")
        emulator.setLightOn(True,1)
        self.effectsController = effects.Effects(emulator)

    def receiveMidi(self, midi):

        note = midi.getNoteNumber()
        velocity = midi.getVelocity()

        if midi.isNoteOn():
            if self.isPiano(midi):
                print "###################PIANO1:", midi

                self.effectsController.colorFlicker(note, MidiListener.GROUP_LEAP_MOTION)

            elif self.isBateria(midi):
        #        print "###################BATERIA:", midi
                self.effectsController.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
                if self.actualBateriaNote != note:
                    self.actualBateriaNote = note
                    #change gamma
                    print "GROUP: " + str(MidiListener.GROUP_BATERIA) +" Changing gamma to: " + str(note)
                    self.effectsController.changeColorGamma(note, MidiListener.GROUP_BATERIA)
         #   else:
        #        print midi


    def isPiano(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() < 40

    def isBateria(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_BATERIA

    def isDjWii(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=40 and midi.getNoteNumber() < 80

    def isDjWub(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=80
