import lights, lightsclient
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
    USE_MULE = 1

    def __init__(self, mode):
        self.channelQueues = {
            # self.CHANNEL_BAJO: Queue(),
            # self.CHANNEL_DRUMS: Queue(),
            self.CHANNEL_LEAP_MOTION: Queue()
        }
        self._mode = mode
        self.channelProcessors = {}

    def start(self):
        for channel, queue in self.channelQueues.iteritems():
            t = MidiProcessor(queue, self._mode)
            self.channelProcessors[channel] = t
            t.daemon = True
            t.start()

    def receiveMidi(self, midi):
        if midi.isNoteOn() and midi.getChannel() == self.CHANNEL_LEAP_MOTION:
            channel = midi.getChannel()
            queue = self.channelQueues[channel]
            queue.put((time.time(), midi))

class MidiProcessor(threading.Thread):

    def __init__(self, queue, mode):
        super(MidiProcessor, self).__init__()
        self.currentDrumsNote = 0
        self.queue = queue
        if mode == MidiListener.USE_MULE :
            self._lightsClient = lightsclient.LightsRestClient("127.0.0.1", "8081")
        else :
            self._lightsClient = lightsclient.LightsRestClient("192.168.43.3", "8899", lightsclient.LightsLocalClient.REAL_SETUP)
        self.ts_last_processed = time.time()

    def run(self):
        while True:
            try:
                self.process_midi()
            except:
                print "Error in thread"
                raise
                break

    def process_midi(self):
        timestamp, midi = self.queue.get()
        note = midi.getNoteNumber()
        velocity = midi.getVelocity()
        discarded = False
        # print midi
        if self.isDrums(midi) and self.currentDrumsNote != note:
            # print "#DRUMS (GAMMA):", midi
            self.currentDrumsNote = note
            self._lightsClient.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
            self._lightsClient.changeColorGamma(note, MidiListener.GROUP_BATERIA)
        elif self.canDiscard(timestamp):
            discarded = True
            print "discarded", midi
        elif self.isDrums(midi):
            print "#DRUMS:", midi
            self._lightsClient.changeIntensity(velocity, MidiListener.GROUP_BATERIA)
        elif self.isPiano(midi):
            print "#PIANO1:", midi
            self._lightsClient.colorFlicker(note, MidiListener.GROUP_LEAP_MOTION)
        elif self.isDjWii(midi):
            print "#DjWii", midi
            self._lightsClient.wiii(note, velocity, MidiListener.GROUP_LEAP_MOTION)
        elif self.isDjWub(midi):
            print "#DjWub", midi
            self._lightsClient.wub(note, velocity, MidiListener.GROUP_LEAP_MOTION)
        else:
            discarded = True
            # print "discarded 2", midi

        if not discarded:
            self.ts_last_processed = time.time()

        self.queue.task_done()

    def canDiscard(self, timestamp):
        return timestamp - self.ts_last_processed < 0.025

    def isPiano(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() < 40

    def isDrums(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_DRUMS

    def isDjWii(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=40 and midi.getNoteNumber() < 80

    def isDjWub(self, midi):
        return midi.getChannel() == MidiListener.CHANNEL_LEAP_MOTION and midi.getNoteNumber() >=80
