from flask import Flask, abort
from flask import request
import json
import synonyms

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def hello_world():
    return {
        "status": "ok",
    }

@app.route("/nearby",methods=['POST'])
def nearby():
    data = request.get_json()
    if not data.get('word'):
        abort(406)
    r = synonyms.nearby(data['word'])
    score = []
    for i in r[1]:
        score.append(float(i))
    return {
        "words": r[0],
        "score": score,
    }

@app.route("/seg",methods=['POST'])
def seg():
    data = request.get_json()
    if not data.get('sentence'):
        abort(406)

    r = synonyms.seg(data['sentence'])
    if len(r) != 2: 
        abort(500)
    return{
        "words": r[0],
        "score": r[1],
    }
    
@app.route("/compare",methods=['POST'])
def compare():
    data = request.get_json()
    if (not data.get('sentence1')) or (not data.get('sentence2')):
        abort(406)
    r = synonyms.compare(data['sentence1'], data['sentence2'], seg=True)
    return {
        "score": r,
    }

@app.route("/v",methods=['POST'])
def v():
    data = request.get_json()
    if not data.get('word'):
        abort(406)
    r = synonyms.v(data['word'])
    score = []
    for i in r:
        score.append(float(i))
    return {
        "score": score,
    }

@app.route("/keyword",methods=['POST'])
def keyword():
    data = request.get_json()
    if not data.get('sentence'):
        abort(406)
    r = synonyms.keywords(data['sentence'])
    return {
        "words": r,
    }

if __name__=='__main__':
    app.run()