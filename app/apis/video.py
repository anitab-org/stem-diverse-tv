from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace

api = Namespace('video', description='Video Library')

@api.route('/latest')
class VideoLibrary(Resource):
    def get(self):
        with open('./content/latests.json') as f:
            return json.loads(f.read())
        return jsonify({'message': 'File does not exist.'})
