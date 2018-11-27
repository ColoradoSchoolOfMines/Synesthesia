import matplotlib
matplotlib.use("Agg")
import numpy as np
import pylab as pl
import wave

file = wave.open("testSounds/92002__jcveliz__violin-origional.wav", mode="rb")
print(file.getnchannels())
print(file.getnframes())
song = []
for x in file.readframes(50864):
    song.append(x)
#print(song)
x = [x for x in range(193)]

print(type(song[1]))
pl.plot(song[38833:39026], 'r.')
pl.xlabel("X")
pl.ylabel("Y")
pl.title("Title")

pl.savefig("testgraph.png")
