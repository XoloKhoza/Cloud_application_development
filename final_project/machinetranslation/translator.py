from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translation = translator.translate(frenchText, src='fr', dest='en')
    translation = translator.translate(frenchText, src='fr', dest='en')
    frenchText = translation.text    
    return frenchText


def frenchToEnglish(frenchText):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(frenchText, src='fr', dest='en')
    englishText = translation.text
    return englishText
