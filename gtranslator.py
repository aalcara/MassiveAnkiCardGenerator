from googletrans import Translator, constants
from pprint import pprint

def get_translation(string):
  translator = Translator()
  translation = translator.translate(string, src="en", dest="pt")
  result = f"<p style='color: green;'>{translation.text}</p>"
  return (result)
