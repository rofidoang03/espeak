from gtts import gTTS
import os

def text_to_speech(text, lang='id'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah menjadi suara: ")
    text_to_speech(text)
