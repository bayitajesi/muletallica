import lights
import effects
import time
import threading
from Queue import Queue

class MidiListener:
    CHANNEL_BAJO = 1
    CHANNEL_DRUMS = 2
    CHANNEL_LEAP_MOTION = 3

    GROUP_BATERIA = 1
    GROUP_LEAP_MOTION = 2

    def __init__(self):
        self.channelQueues = {
            self.CHANNEL_BAJO: Queue(),
            self.CHANNEL_DRUMS: Queue(),
            self.CHANNEL_LEAP_MOTION: Queue()
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
            queue.put((time.time(), midi))

class MidiProcessor(threading.Thread):

    def __init__(self, queue):
        super(MidiProcessor, self).__init__()
        self.currentDrumsNote = 0
        self.lightsController = lights.LightsController("192.168.43.3", "8899")
        self.queue = queue
        emulator = lights.MilightController("192.168.43.3", "8899")
        emulator.setLightOn(True,1)
        self.effectsController = effects.Effects(emulator)
        self.ts_last_processed = time.time()

    def run(self):
        while True:
            try:
                self.process_midi()
            except:
                print "Error in thread"
                break

    def process_midi(self):
        timestamp, midi = self.queue.get()
        note = midi.getNoteNumber()
        velocity = midi.getVelocity()
        discarded = False
        if self.isDrums(midi) and self.currentDrumsNote != note:
            print "#DRUMS (GAMMA):", midi
            self.currentDrumsNote = note
            self.effectsController.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
            self.effectsController.changeColorGamma(note, MidiListener.GROUP_BATERIA)
        elif self.canDiscard(timestamp):
            discarded = True
            print "discarded 0"
        elif self.isDrums(midi):
            print "#DRUMS:", midi
            self.effectsController.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
        elif self.isPiano(midi):
            print "#PIANO1:", midi
            self.effectsController.colorFlicker(note, MidiListener.GROUP_LEAP_MOTION)
        else:
            discarded = True
            print "discarded 2", midi

        if not discarded:
            self.ts_last_processed = time.time()

        self.queue.task_done()

    def canDiscard(self, timestamp):
        return timestamp - self.ts_last_processed < 0.1

    def isPiano(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() < 40

    def isDrums(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_DRUMS

    def isDjWii(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=40 and midi.getNoteNumber() < 80

    def isDjWub(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=80
