from genanki_ctrl import GeneratorAnki
import sys
import en_dictionary
from get_audio import convert_to_audio
from gtranslator import get_translation

if __name__ == "__main__":
  filename = "input.csv"
  print(f"openning {filename} ...")
  ga = GeneratorAnki()

  file = open(filename)
  errfile = open("error.log", "a")

  for line in file:
    try:
      splitted = line.split(";")
      word = splitted[0]
      sentence = splitted[1].strip("\n")
      meaning = en_dictionary.get_meaning(word)
      formated_sentence = sentence.replace(word, f"<b>{word}</b>")
      convert_to_audio(word, sentence)
      meaning += get_translation(sentence)

      ga.add_note(formated_sentence, meaning, word)
      print(f"[{sentence}] added to deck")
    except:
      print(f"Could not find [{line}]")
      errfile.write(line)

    
  ga.save_file()

