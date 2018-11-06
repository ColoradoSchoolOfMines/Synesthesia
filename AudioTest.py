# all this commented out stuff is just to convert mp3 to wav
# import pydub
import wave
#from os import path
# from pydub import AudioSegment
src = input('File Name: ')
#dst = 'test.wav'
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format ="wav")
file = wave.open(src, mode="rb")
song = []
for x in file.readframes(3000):
    song.append(x)
print(song)

