import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    if len(get_close_matches(w, data.keys())) > 0:
        response = input("Did you mean %s: " % get_close_matches(w, data.keys())[0])
        if response == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif response == 'N':
            return "This word does'nt exist"
        else:
            return "We did'nt understand your query"
    else:
        return "This word does'nt exist"


word = input("Please enter the word: ")
result = translate(word)

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
