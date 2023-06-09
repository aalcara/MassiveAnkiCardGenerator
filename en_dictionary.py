from PyDictionary import PyDictionary

def get_meaning(string):
  dictionary = PyDictionary()
  meaning = dictionary.meaning(string)

  formated_meaning = ""
  for word_class in meaning:
    formated_meaning += (f"<i>{word_class}</i><br />")
    for item in meaning[word_class]:
      formated_meaning += (f"\t- {item}<br />")
    formated_meaning += ("<br />")

  return (formated_meaning)
