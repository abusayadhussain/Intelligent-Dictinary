import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif len(get_close_matches(word, data.keys())) > 0:
        yn =  input("Did you mean %s instead??, type y for yes or n for no: " % get_close_matches(word, data.keys())[0])
        if(yn.lower() == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif(yn.lower() == "n"):
            return "Word Doesn't exit in the dictionary. Please check the spell or whats wrong!"
        else:
            return "Please type y or n to get a result"

    else:
        return "Word Doesn't exit in the dictionary. Please check the spell or whats wrong!"
word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
