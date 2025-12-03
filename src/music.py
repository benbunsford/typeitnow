import fluidsynth
from mido import MidiFile
import time
import threading

sound_font = "music/undertale.sf2"
song = "music/type-it.mid"

class MusicPlayer:
    def __init__(self):
        self.fs = fluidsynth.Synth()
        self.fs.start()
        self.sfid = self.fs.sfload(sound_font)
        self.fs.program_select(0, self.sfid, 0, 0)
        self.speed = 1.0
        self._stop_flag = False

    def play(self):
        mid = MidiFile(song)
        self._stop_flag = False

        for msg in mid:
            if self._stop_flag == True:
                for chan in range(16):
                    self.fs.all_sounds_off(chan)
                break
            if msg.time > 0:
                time.sleep(msg.time/self.speed)
            if msg.type == 'note_on':
                self.fs.noteon(msg.channel, msg.note, msg.velocity)
            elif msg.type == 'note_off':
                self.fs.noteoff(msg.channel, msg.note)
            elif msg.type == 'control_change':
                self.fs.cc(msg.channel, msg.control, msg.value)
            elif msg.type == 'program_change':
                self.fs.program_change(msg.channel, msg.program)

    def speed_up(self):
        self.speed *= 1.0075

    def play_async(self):
        thread = threading.Thread(target=self.play, daemon=True)
        thread.start()
        return thread

    def stop(self):
        self._stop_flag = True
        #self.fs.delete()

