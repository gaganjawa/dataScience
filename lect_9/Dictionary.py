from flask import Flask, jsonify, request
import json
from difflib import get_close_matches

app = Flask(__name__)

data = json.load(open("data.json"))

@app.route('/findword', methods = ['POST'])
def findMeaning():
	req_dict = request.get_json()
	word = req_dict['word'].lower()

	if word in data.keys():
		return jsonify({word:data[word]})

	suggested_word = get_close_matches(word, data.keys(), n=1)

	if len(suggested_word)>0:
		return jsonify({"showing meaning for " + (suggested_word[0]): data[suggested_word[0]] })
	else:
		return jsonify({"message":"Word dosn't exist"})
		
		
app.run(port=5000)