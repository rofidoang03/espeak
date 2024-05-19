from gtts import gTTS
import simpleaudio as sa
import os

def text_to_speech(text, lang='id'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    # Menggunakan ffmpeg untuk mengonversi file MP3 ke WAV
    os.system("ffmpeg -loglevel panic -i output.mp3 -acodec pcm_s16le -ac 2 -ar 44100 output.wav")
    # Memuat file WAV menggunakan simpleaudio
    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    # Menghapus file setelah selesai diputar
    os.remove("output.mp3")
    os.remove("output.wav")

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah menjadi suara: ")
    text_to_speech(text)
