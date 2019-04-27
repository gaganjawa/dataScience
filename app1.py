from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
	"name":"my store",
	"items": [{"name":"chair","price":200}]
}]

@app.route('/abc')
def func():
	return "Hello World"
	

@app.route('/addstore', methods = ['POST'])
def addStore():
	request_dict = request.get_json();
	for i in stores:
		if request_dict['name'] == i['name']:
			return jsonify({"message":"Store already present."})
	
	if 'items' not in request_dict.keys():
		new_dict = {"name":request_dict['name'], "items":[]}
		stores.append(new_dict)
	else:
		stores.append(request_dict)
	return jsonify({"message":"Store Added", "Stores":stores})
	
@app.route('/store/<string:name>/items')
def getAllItemsForStore(name):
	for i in stores:
		if i['name'] == name:
			return jsonify({'items':i['items']})
	return jsonify({"message":"Store not found"})

@app.route('/store/<string:name>')
def getStore(name):
	for i in stores:
		if i['name']==name:
			return jsonify(i)
	return jsonify({"message":"Store not found"})
	

@app.route('/stores')
def get_stores():
	return jsonify({"all stores":stores})
	

app.run(port=5000)