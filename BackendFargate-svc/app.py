from flask import Flask
import json

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def healthcheck():
    return "ok"


@app.route('/', methods=['GET'])
def inc():
    data = {"response": "Hello from BackendFargate-svc"}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
