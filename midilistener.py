import lights
import effects
import time
import threading
from Queue import Queue

class MidiListener:
    CHANNEL_BAJO = 1
    CHANNEL_BATERIA = 2
    CHANNEL_LEAP_MOTION = 3

    GROUP_BATERIA = 1
    GROUP_LEAP_MOTION = 2

    def __init__(self):
        self.channelQueues = {
            self.CHANNEL_BAJO: Queue(1),
            self.CHANNEL_BATERIA: Queue(1),
            self.CHANNEL_LEAP_MOTION: Queue(1)
        }
        self.channelProcessors = {}

    def start(self):
        for channel, queue in self.channelQueues.iteritems():
             t = MidiProcessor(queue)
             self.channelProcessors[channel] = t
             t.daemon = True
             t.start()

    def receiveMidi(self, midi):
        if midi.isNoteOn():
            channel = midi.getChannel()
            queue = self.channelQueues[channel]
            processor = self.channelProcessors[channel]
            if processor.isBateria(midi) and processor.actualBateriaNote != midi.getNoteNumber():
                print "changeColorGamma", midi
                queue.join()
                queue.put(midi)
            else:
                try:
                    queue.put_nowait(midi)
                except:
                    print "discarded"

class MidiProcessor(threading.Thread):

    def __init__(self, queue):
        super(MidiProcessor, self).__init__()
        self.actualBateriaNote = 0
        self.lightsController = lights.LightsController("192.168.43.3", "8899")
        self.queue = queue
        emulator = lights.MilightController("192.168.43.3", "8899")
        emulator.setLightOn(True,1)
        self.effectsController = effects.Effects(emulator)

    def run(self):
        while True:
            midi = self.queue.get()
            note = midi.getNoteNumber()
            velocity = midi.getVelocity()
            if self.isPiano(midi):
                print "###################PIANO1:", midi

                self.effectsController.colorFlicker(note, MidiListener.GROUP_LEAP_MOTION)

            elif self.isBateria(midi):
                print "###################BATERIA:", midi
                self.effectsController.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
                if self.actualBateriaNote != note:
                    self.actualBateriaNote = note
                    #change gamma
                    print "GROUP: " + str(MidiListener.GROUP_BATERIA) +" Changing gamma to: " + str(note)
                    self.effectsController.changeColorGamma(note, MidiListener.GROUP_BATERIA)
         #   else:
        #        print midi

            time.sleep(0.1)
            self.queue.task_done()

    def isPiano(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() < 40

    def isBateria(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_BATERIA

    def isDjWii(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=40 and midi.getNoteNumber() < 80

    def isDjWub(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=80
