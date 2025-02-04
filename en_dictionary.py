import requests
from nltk.corpus import wordnet

POS_TAGS = {
    "n": "Noun",
    "v": "Verb",
    "a": "Adjective",
    "s": "Adjective (satellite)",
    "r": "Adverb"
}

def get_meaning(word):
    
    synsets = wordnet.synsets(word)
    print (f"synsets: {synsets}")
    if synsets:
        formated_meaning = ""
        for synset in synsets:
            print (f"synset: {synset}")
            pos = POS_TAGS.get(synset.pos(), "Other")
            definition = synset.definition()
            formated_meaning += f"<i>{pos}</i><br />\t- {definition}<br /><br />"
        return formated_meaning

    url = f"https://api.urbandictionary.com/v0/define?term={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["list"]:
            formated_meaning = "<i>Urban Dictionary</i><br />"
            for entry in data["list"][:3]:
                formated_meaning += f"\t- {entry['definition']}<br /><br />"
            return formated_meaning

    return