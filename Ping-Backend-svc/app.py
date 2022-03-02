from flask import Flask
import os
import urllib.request
import json

app = Flask(__name__)
BACKEND_URL = "http://{}".format(os.getenv("BACKEND_URL"))


@app.route('/ping', methods=['GET'])
def healthcheck():
    return "ok"


@app.route('/', methods=['GET'])
def inc():
    data = {}
    # backend_response = json.loads(urllib.request.urlopen(BACKEND_URL).read())
    # data['backend_response'] = backend_response['response']
    data = {"Hello from APP1"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
