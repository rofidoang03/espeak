from gtts import gTTS
from playsound import playsound
import os

text="""
Perkenalkan nama Saya Rofi.
Saya lahir di Bekasi."""

tts=gTTS(text=text, lang="id")
nama_file="sound.mp3"
tts.save(nama_file)
playsound(nama_file)
os.remove(nama_file)
