from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return 'Hello, Universe! With ❤️ from Software Shinobi (www.softwareshinobi.com)'
