import json
from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"name": "iphone", "category": "phone", "price": "20.5","instock": "200"},
    {"name": "iphone1", "category": "phone1", "price": "30.5","instock": "300"},
    {"name": "iphone2", "category": "phone2", "price": "40.5","instock": "400"},
    {"name": "iphone3", "category": "phone3", "price": "50.5","instock": "500"},
    {"name": "iphone4", "category": "phone4", "price": "60.5","instock": "600"},
]
def _find_next_name(name):
    data = [x for x in items if x['name'] == name]
    return data

@app.route('/items', methods=["GET"])
def get_items():
    return jsonify(items)

@app.route('/items/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    return jsonify(data)

@app.route('/items', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock": instock,       
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request"}, name
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/items/delete/<name>', methods=["DELETE"])
def delete_items(name: str):

    data= _find_next_name(name)
    if not data:
        return {"error": "items not found"}, 404
    else:
        items.remove(data[0])
        return {'message': 'items deleated'}, 200

@app.route('/items/put/<c_name>', methods=["PUT"])
def update_items(c_name):

    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    for items in items:
        if c_name == items["name"]:
            items["category"] = (category)
            items["price"] = (price)
            items["instock"] = (instock)
            return jsonify(items)
        
    else:
        return "error", 404

    #return jsonify({'message': 'items not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)