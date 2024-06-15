from gtts import gTTS
import os


def generate_audio(name, sentence):
    sentence = name + ". " + sentence
    audio = gTTS(text=sentence, lang="en", tld="com")
    os.makedirs("./audio", mode=0o777, exist_ok=True)
    audio.save(f"audio/{name}.mp3")
