import os
import time
import keyboard
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
from random import randint


def getRandom():
    x = randint(4,5)
    if x == 5:
        sayJoke(randint(0,5))


def sayJoke(yeet):
    print("called:{} ".format(yeet))
    i = 0
    f = open("Jokes.txt")
    while True:
        line = f.readline()
        i += 1
        if not line:
            break
        elif i == yeet:
            voiceSynth(line)
            break
    f.close()


def voiceSynth(text):
    print("called")
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    audio = MP3("output.mp3")
    mixer.init()
    mixer.music.load("output.mp3")
    mixer.music.play()
    time.sleep(audio.info.length)
    mixer.quit()


def checkForCon(con):
    if keyboard.is_pressed(';'):
        con[0] = False


con = [True]
while con[0] is True:
    checkForCon(con)
    getRandom()
    time.sleep(4)
