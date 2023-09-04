from googletrans import Translator

def get_translation(name, string):
  translator = Translator()
  translation = translator.translate(string, src="en", dest="pt").text
  word = translator.translate(name, src="en", dest="pt").text
  if word in translation:
    translation = translation.replace(word, f"<b>{word}</b>")
  result = f"<p style='color: green;'>{translation}</p>"
  return (result)
