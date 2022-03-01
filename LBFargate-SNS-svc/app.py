from flask import Flask, request, jsonify, make_response
import boto3
import os
import json
import random, string
import time

def generate_random(char_length):
   characters = string.ascii_lowercase
   return ''.join(random.choice(characters) for i in range(char_length))

TOPIC_ARNS = json.loads(os.getenv("SNS_TOPIC_ARN"))
client = boto3.client('sns')
app = Flask(__name__)

@app.route('/')
def hello_world():
    ping_message = "Hello! Message {} sent from LBFargate at time {}".format(generate_random(5),time.strftime('%A, %B %d %Y, %H:%M:%S'))
    response = client.publish(
        TopicArn=TOPIC_ARNS["ping"],
        Message=ping_message
            )
    message = jsonify(message=ping_message)
    return make_response(message, 200)

@app.route('/ping')
def pong():
    message = jsonify(message="Pong")
    return make_response(message, 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
