import genanki


class GeneratorAnki:
    def __init__(self):
        self.my_model = genanki.Model(
            1607392320,
            "AutoVocabulary",
            fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Media"}],
            templates=[
                {
                    "name": "Card 1",
                    "qfmt": "{{Question}}<br>{{Media}}",
                    "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ],
            css=""".card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
}
""",
        )

        self.new_model = genanki.Model(
            1607333320,
            "AutoVocabularyV2",
            fields=[
                {"name": "Word"},
                {"name": "Sentence"},
                {"name": "Meaning"},
                {"name": "Media"},
                {"name": "Word (Portuguese)"},
                {"name": "Sentence (Portuguese)"},
            ],
            templates=[
                {
                    "name": "Audio Card",
                    "qfmt": "{{Media}}",
                    "afmt": '{{FrontSide}}<hr id="answer"><b>{{Word}}</b><p>{{Sentence}}<p><p>{{Meaning}}</p><p class="translate"><b>{{Word (Portuguese)}}</b><br>{{Sentence (Portuguese)}}</p>',
                },
                {
                    "name": "Translate Card",
                    "qfmt": '<p><b>Traduzir</b></p><p class="translate"><b>{{Word (Portuguese)}}</b></p><p class="translate">{{Sentence (Portuguese)}}</p>',
                    "afmt": '{{FrontSide}}<hr id="answer"><b>{{Word}}</b>{{Media}}<p>{{Sentence}}<p><p>{{Meaning}}</p>',
                },
            ],
            css=""".card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
}

.translate {
  color: green
}
""",
        )

        self.my_deck = genanki.Deck(2059400110, "English::AutoVocabulary")
        self.new_deck = genanki.Deck(2059400198, "English::AutoVocabularyV2")

        self.my_package = genanki.Package([self.my_deck, self.new_deck])

    def add_note(self, word, sentence, meaning, pt_word, pt_sentence):
        audio = f"[sound:{word}.mp3]"
        note = genanki.Note(
            model=self.new_model,
            fields=[word, sentence, meaning, audio, pt_word, pt_sentence],
        )

        self.my_package.media_files.append(f"audio/{word}.mp3")
        self.new_deck.add_note(note)

    def save_file(self, filename="output.apkg"):
        self.my_package.write_to_file(filename)
