import json
from difflib import *

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    wordCap = word.capitalize()
    wordUpper = word.upper()
    match = get_close_matches(word, data.keys(), n=1) # this is a list
    if word in data:
        return data[word]
    elif wordCap in data:
        return data[wordCap]
    elif wordUpper in data:
        return data[wordUpper]
    elif len(match) == 1:
        error = input("Did you mean: '" + match[0] + "'?\nIf you mean " + match[0] + "? Y/N\n")
        error = error.lower()
        if error == "y":
            return translate(match[0])
        else:
            newTry = input("Sorry, want to try again? Y/N\n")
            newTry = newTry.lower()
            if newTry == "y":
                main()
            else:
                return "Application finished"
    else:
        return "Word '" + word + "' not found"

def main():
    word = input("Enter a word: ")
    result = translate(word)
    if type(result) == list:
        for i in result:
            print(i)
    elif result == None:
        print("")
    else:
        print(result)

main()
