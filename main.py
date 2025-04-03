# offline translator
from translate import Translator

# define language translate to
translator = Translator(to_lang="fr")
# open file
try:
    with open("translate.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open("frtranslate.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("File not found. Check the file path")
