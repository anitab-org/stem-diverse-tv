from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace
from app.database.models.author import AuthorModel
from app.database.models.videos import VideoModel
from app.database.sqlalchemy_extension import db

api = Namespace('video', description='Video Library')

@api.route('/latest')
class VideoLibrary(Resource):
    def get(self):
        with open('./content/latests.json') as f:
            return json.loads(f.read())
        return jsonify({'message': 'File does not exist.'})

@api.route('/')
class VideoAuthor(Resource):
    def get(self):
        ''' To test the video and author association, you can visit this route and after running this code, 
        open database local file to view the association table. '''
        author1 = AuthorModel(name="Jill")
        author2 = AuthorModel(name="John")
        author3 = AuthorModel(name="Tom")
        author1.save_to_db()
        author2.save_to_db()
        author3.save_to_db()
        video1 = VideoModel(name="play football")
        video2 = VideoModel(name="play badminton")
        video3 = VideoModel(name="play cricket")
        video1.save_to_db()
        video2.save_to_db()
        video3.save_to_db()
        video1.authors.append(author1)
        db.session.commit()
        video3.authors.append(author3)
        db.session.commit()
        video1.authors.append(author3)
        db.session.commit()
        
        return {"message": "Videos and authors added to database"}, 200