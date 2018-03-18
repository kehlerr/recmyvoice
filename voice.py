import os

import argparse
import queue

import pygame
from pygame.locals import *

import sounddevice as sd
import soundfile as sf


parser = argparse.ArgumentParser(description=__doc__)

FILENAME = 'tmp.wav'
RATE = 48000*2
CHANNELS = 1

stopped = False

def stop_rec():
     global stopped
     stopped = True

def rec():
     try:
          global stopped
          stopped = False

          if os.path.isfile(FILENAME):
               os.remove(FILENAME)

          q = queue.Queue()

          def callback(indata, frames, time, status):
               """This is called (from a separate thread) for each audio block."""
               if status:
                    print(status)
               q.put(indata.copy())

          with sf.SoundFile(FILENAME, mode='x', samplerate=RATE, channels=CHANNELS) as file:
               with sd.InputStream(samplerate=RATE, channels=CHANNELS, callback=callback):
                    while not stopped:
                         file.write(q.get())
                         for event in pygame.event.get():
                              if event.type == KEYUP:
                                   stop_rec()
     
     except KeyboardInterrupt:
          print('\nFinished.')
          parser.exit(0)

def play():
     try:
          data, fs = sf.read(FILENAME, dtype='float32')
          sd.play(data, fs)
          status = sd.wait()
          if status:
               parser.exit('Error during playback: ' + str(status))
     except KeyboardInterrupt:
          parser.exit('\nInterrupted by user')
     except Exception as e:
          parser.exit(type(e).__name__ + ': ' + str(e))
     finally:
          os.remove(FILENAME)
