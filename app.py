from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/latest')
def latest():
    with open('./content/latests.json') as f:
        return jsonify(json.loads(f.read()))
    return jsonify({'message': 'File does not exist.'})


app.run(port=5000)
