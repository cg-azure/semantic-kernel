import asyncio
from flask import Flask, render_template, request, jsonify
from intent_detection import process_user_input

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/send", methods=['POST'])
def send():
    user_input = request.json['message']

    response = asyncio.run(process_user_input(user_input))
   
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
