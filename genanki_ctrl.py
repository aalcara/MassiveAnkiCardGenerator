import genanki

class GeneratorAnki:
  
  def __init__(self):
    self.my_model = genanki.Model(
      1607392319,
      'Simple Model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Media'}
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{Question}}<br>{{Media}}',
          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
      ],
      css=""".card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
}
"""
      )

    self.my_deck = genanki.Deck(
      2059400110,
      'English::AutoVocabulary')

    self.my_package = genanki.Package(self.my_deck)

  def add_note(self, field1, field2, word):
    audio = f"[sound:{word}.mp3]"
    self.my_note = genanki.Note(model=self.my_model,
      fields=[field1, field2, audio])
    self.my_package.media_files.append(f"audio/{word}.mp3")

    self.my_deck.add_note(self.my_note)
    
  def save_file(self, filename="output.apkg"):
    self.my_package.write_to_file(filename)

