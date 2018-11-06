import matplotlib
matplotlib.use("Agg")
import numpy as np
import pylab as pl
import wave

file = wave.open("testSounds/18871__zippi1__sound-bell-440hz.wav", mode="rb")
song = []
for x in file.readframes(3000):
    song.append(x)
print(song)

pl.close()
pl.plot(song[::100])
pl.xlabel("X")
pl.ylabel("Y")
pl.title("Title")

pl.savefig("testgraph.png")
