import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()    #what ever the 'word' user types in input , it is rendered in lowercase,
                           #because in our json file we have all the entries in lowercase
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exists."
        else:
            return "I did not get you, Sorry!"

    else:
        return "No such word"



word = input("Enter word: ")  #word is a global variable here

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
