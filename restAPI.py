from flask import Flask,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

foods = {
    "Foods": [
        {
            "Description": "Delicious Cookie",
            "item_id":"0",
            "name": "cookie"
        },
        {
            "Description": "Toast",
            "item_id":"1",
            "name": "Toast"
        }
        
    ]
}

@app.route('/')
def index():
    return "Welcome to the Food API"

@app.route("/api/food", methods=['GET'])
def get():
    return jsonify({'Foods':foods})

@app.route("/api/food/<item_id>", methods=['GET'])
def get_meal(item_id):
    return jsonify({'food': foods[item_id]})


app.run()