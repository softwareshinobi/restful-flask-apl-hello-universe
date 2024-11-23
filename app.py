from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello, Universe! With ❤️ from Software Shinobi (www.softwareshinobi.com)'

@app.route('/<int:num1>/<int:num2>')
def multiply(num1, num2):

    result = num1 * num2

    return jsonify({'result': result})

