from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name':'My store1',
        'items':[
            {
                'name':"My item1",
                'price':15
            }
        ]
    }
]
@app.route('/')  #htto://www.google.com/  TO HOMEPAGE
def home():
 return render_template('index.html')


#POST - receive data  (CREATE A STORE)
#GET - used to send data back (RETURN STORE)

#POST /store data {name:}   create store
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
        }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : "store not found"})

#GET /Store/
@app.route('/store')
def get_stores():
    return  jsonify({'stores':stores})

#POST /store/<string:name> / item create store
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {
            'name': request_data['name'],
            'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "store not found"})
#
#GET /store/<string:name > / item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': "store not found"})



app.run(port = 5009)
