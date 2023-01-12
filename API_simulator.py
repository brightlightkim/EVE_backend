# TO LAUNCH THE FLASK SERVER...
# ...execute the following on the command line:
# export FLASK_APP=API_simulator
# flask run --host=0.0.0.0

import sys
import json
import random

from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

# Load the pre-created Eve responses
f = open('json_samples.txt','r')
responses=[]
for line in f:
    responses.append(json.loads(line.strip('\n')))

@app.route('/')
@app.route('/index')
def response():

    if request.args.get('start')==True:
        pass
    else:
        return random.choice(responses)
