from gtts import gTTS
import simpleaudio as sa
import os

def text_to_speech(text, lang='id'):
    tts = gTTS(text=text, lang=lang)
    filename = "output.wav"
    tts.save("output.mp3")
    os.system("ffmpeg -i output.mp3 -acodec pcm_s16le -ac 2 -ar 44100 output.wav")
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    os.remove("output.mp3")
    os.remove("output.wav")  # Hapus file setelah diputar untuk kebersihan

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah menjadi suara: ")
    text_to_speech(text)
