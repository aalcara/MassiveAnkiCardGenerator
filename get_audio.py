from gtts import gTTS


def convert_to_audio(name, sentence):
    audio =gTTS(text=sentence, lang='en', tld='com')
    audio.save(f"audio/{name}.mp3")
