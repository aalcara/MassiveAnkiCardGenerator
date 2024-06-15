from deep_translator import GoogleTranslator


def get_translation(string, lang="en"):
    try:
        translator = GoogleTranslator(source=lang, target="pt")
        translation = translator.translate(string)
        return translation
    except Exception as e:
        raise ValueError(f"Failed to get translation: {str(e)}")
