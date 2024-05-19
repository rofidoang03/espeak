from gtts import gTTS
import simpleaudio as sa
import os

def text_to_speech(text, lang='id', pitch=0.6, speed=0.8):
    # Mengatur pitch dan speed
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.speed = speed
    tts.pitch = pitch
    tts.save("output.mp3")
    # Konversi file MP3 ke WAV
    os.system("ffmpeg -loglevel panic -i output.mp3 -acodec pcm_s16le -ac 2 -ar 44100 output.wav")
    # Memutar file WAV
    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    # Hapus file setelah selesai diputar
    os.remove("output.mp3")
    os.remove("output.wav")

if __name__ == "__main__":
    text = input("Masukkan teks yang ingin diubah menjadi suara: ")
    # Mengatur pitch menjadi lebih rendah (misalnya, 0.5) untuk suara cowok
    text_to_speech(text, pitch=0.5)
