import numpy as np
import sounddevice as sd
import soundfile as sf
import time

def playAudio(filename):
    sfx, sR = sf.read(filename)
    print(f"read {filename}")
    sd.play(sfx)
    sd.wait()
audioFiles = [
    "squeaky-toy_1.mp3",
    "mlg-airhorn.mp3",
    "cow-moo.mp3",
    "vine-boom.mp3"
]

print("Enter the number of a sound you'd like to play (1-4): ")
answer = input()
playAudio(audioFiles[int(answer)-1])