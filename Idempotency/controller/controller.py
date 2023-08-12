import json
from controller.redis_DB import *

from flask import Flask, request

app = Flask(__name__)
red = Redis_DB()


@app.route('/')
def home():
    return 'Welcome to Idempotency'

@app.route('/movies/', methods=['GET'])
def request_movies():
    uid = request.args.get('uid')
    response = red.main(uid)

    if not response:
        response = []
        with open('database/movies.json','r') as f:
            movie = json.loads(f.read())
        
        for i in movie:
            response.append(i['Movie'])
        red.insert(uid,response)
    else:
        return json.dumps(response)

    return json.dumps(response)