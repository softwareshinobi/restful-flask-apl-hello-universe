from flask import Flask, request, jsonify
import datetime
import uuid

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello, Universe! With ❤️ from Software Shinobi (www.softwareshinobi.com)'

@app.route('/<int:num1>/<int:num2>')
def multiply(num1, num2):

    result = num1 * num2

    return jsonify({'product': result})

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

@app.route('/complex_process', methods=['POST'])
def complex_process():
    data = request.get_json()
    string = data['string']
    num1 = data['num1']
    num2 = data['num2']

    reversed_string = string[::-1]
    addition = num1 + num2
    multiplication = num1 * num2
    division = num1 / num2  # Handle division by zero if needed
    
    current_time = datetime.datetime.now()
    current_timezone = current_time.tzname()
    random_id = str(uuid.uuid4())

    response = {
        'original_string': string,
        'reversed_string': reversed_string,
        'addition': addition,
        'multiplication': multiplication,
        'division': division,
        'current_time': str(current_time),
        'current_timezone': current_timezone,
        'random_id': random_id,
        'random_uuid': str(uuid.uuid4())
    }

    return jsonify(response)
