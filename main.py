from genanki_ctrl import GeneratorAnki
import shutil
import en_dictionary
from get_audio import generate_audio
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
      generate_audio(word, sentence)
      pt_word = get_translation(word)
      pt_sentence = get_translation(sentence)

      ga.add_note(word, sentence, meaning, pt_word, pt_sentence)
      print(f"OK! [{word} ||| {sentence}]")
    except Exception as e:
      print("FAIL! [ " + line.strip('\n') + " ] - Error: " + str(e) )
      errfile.write(line + "\n")

  ga.save_file()
  print("output generated!")
  try:
    shutil.rmtree("./audio")
    print("audio removed!")
  except OSError as e:
    print(f"Error removing audios:{ e.strerror}")
