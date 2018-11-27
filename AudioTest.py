import matplotlib
matplotlib.use("Agg")
import numpy as np
import pylab as pl
import wave


file = wave.open("testSounds/92002__jcveliz__violin-origional.wav", mode="rb")
#print(file.getnchannels()) 
#print(file.getnframes())
song = []
bytelist = file.readframes(50896)

#print(int.from_bytes(ioobject.read(2), 'little', signed = True))
for x in range(0, len(bytelist),2):
    song.append(int.from_bytes(bytelist[x:x+2], 'little', signed = True))


pl.plot(song[38833:39026], 'r')
pl.xlabel("X")
pl.ylabel("Y")
pl.title("Title")

pl.savefig("testgraph.png")
