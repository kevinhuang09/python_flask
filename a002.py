from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "connect successfully"

@app.route('/predict', methods = ['POST'])
def postInput():
    data = request.get_json()

    if not data or "id" not in data or "name" not in data:
        print("The format is not correct")
    
    user_id = data['id']
    user_name = data["name"]

    print(f"The data from the front end sent is id:{user_id}, name:{user_name}")

    result = {
        'message' : f"receive id:{user_id}, name:{user_name}",
        'status' : 'success'
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
