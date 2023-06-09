from genanki_ctrl import GeneratorAnki
import shutil
import en_dictionary
from get_audio import convert_to_audio
from gtranslator import get_translation

separator = "|||"

if __name__ == "__main__":
  filename = "input.csv"
  print(f"openning {filename} ...")
  ga = GeneratorAnki()

  file = open(filename)
  errfile = open("error.log", "a")

  for line in file:
    try:
      splitted = line.split(separator)
      word = splitted[0]
      sentence = splitted[1].strip("\n")
      meaning = en_dictionary.get_meaning(word)
      formated_sentence = sentence.replace(word, f"<b>{word}</b>")
      convert_to_audio(word, sentence)
      meaning += get_translation(word, sentence)

      ga.add_note(formated_sentence, meaning, word)
      print(f"OK! [{word} ||| {sentence}]")
    except Exception as e:
      print("FAIL! [" + line.strip('\n') + "] ")
      print(e)
      errfile.write(line + "\n")

  ga.save_file()
  try:
    shutil.rmtree("./audio")
  except OSError as e:
    print(f"Error:{ e.strerror}")

