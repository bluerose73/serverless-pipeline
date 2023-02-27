from flask import Flask, request
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def function():
    return 'Hello world'

if __name__ == '__main__':
    app.run()