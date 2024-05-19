from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text, lang='id'):
    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # Hapus file setelah diputar untuk kebersihan

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah menjadi suara: ")
    text_to_speech(text)
