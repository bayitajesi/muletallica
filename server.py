import sys
import rtmidi
import midilistener

def print_message(midi):
    if midi.isNoteOn():
        print 'ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity(), midi.getChannel()
    elif midi.isNoteOff():
        print 'OFF:', midi.getMidiNoteName(midi.getNoteNumber())
    elif midi.isController():
        print 'CONTROLLER', midi.getControllerNumber(), midi.getControllerValue()


midiListener = midilistener.MidiListener(sys.argv[1])
midiListener.start()
midiin = rtmidi.RtMidiIn()
ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print "Port: " + str(i) + " Name: " + midiin.getPortName(i)
    print "Select port to use: "
    c = sys.stdin.read(1)
    midiin.openPort(int(c))
    print "Listening on port: " + c
    while True:
        m = midiin.getMessage(250) # some timeout in ms
        if m is not None:
            midiListener.receiveMidi(m)
            #print_message(m)
else:
    print 'NO MIDI INPUT PORTS!'
