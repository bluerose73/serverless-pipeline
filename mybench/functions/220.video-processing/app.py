from flask import Flask, request
from function import handler
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def function():
    begin = datetime.datetime.now()
    ret = handler(request.get_json())
    end = datetime.datetime.now()
    print(ret)
    ret['time'] = {
        'begin': begin.strftime("%H:%M:%S.%f"),
        'end': end.strftime("%H:%M:%S.%f")
    }
    return json.dumps(ret)

if __name__ == '__main__':
    app.run()