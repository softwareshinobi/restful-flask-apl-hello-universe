from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello, Universe! With ❤️ from Software Shinobi (www.softwareshinobi.com)'

@app.route('/<int:num1>/<int:num2>')
def multiply(num1, num2):

    result = num1 * num2
    return result
##    return jsonify({'result': result})

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()
    string = data['string']
    num1 = data['num1']
    num2 = data['num2']

    reversed_string = string[::-1]
    sum_of_nums = num1 + num2

    result = reversed_string + str(sum_of_nums)
    return jsonify({'result': result})
