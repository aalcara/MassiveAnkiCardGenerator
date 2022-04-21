# MassiveAnkiCardGenerator

Application to turn a list of words and phrases in Anki Cards.

I made this to avoid the painful job of clipping and pasting meaning and translation of the words/sentences that I want to memorize, because I know that I will forgot the that meaning ir i don't review it soon.

The program will get automatically:
- the meaning of the word;
- the audio (Text to Speech) of the phrase;  
- the translation of the prase to Portuguese.

With this elements it will save the output in `output.apkg` file, that can be imported by Anki.

## How to use

Until now, I have to put in each line of the file `input.csv` the word and the phrase (that must contain the word), separated by an `;` character, as follow:

```
word;phrase with the word
example;this is an example
lorem;lorem ipsum
bigger example;this is an bigger example
```

Then run:

``` bash
python3 main.py
```

For the words that for some reason can't be created the card will be added to `error.log` file.


## To Do

[] handle idioms or slangs that can't be find in PyDictionary
[] Create an config file to choose another type of card
[] accept another template of input file, based on config file
