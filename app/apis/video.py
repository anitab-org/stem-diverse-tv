from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace
from app.database.models.author import AuthorModel
from app.database.models.videos import VideoModel
from app.database.models.section import SectionModel
from app.database.models.category import CategoryModel
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
        ''' To test the bidirectional and many-to-many relations of database. 
        Below is the sample code debud the proper functionality of backref and relationships.  '''
        author1 = AuthorModel(name="Jill")
        author2 = AuthorModel(name="John")
        author3 = AuthorModel(name="Tom")
        author1.save_to_db()
        author2.save_to_db()
        author3.save_to_db()
        
        video1 = VideoModel(name="play football")
        video2 = VideoModel(name="play badminton")
        video3 = VideoModel(name="play cricket")
        video4 = VideoModel(name="microsoft")
        video5 = VideoModel(name="google")
        video6 = VideoModel(name="tesla")
        video1.save_to_db()
        video2.save_to_db()
        video3.save_to_db()
        video4.save_to_db()
        video5.save_to_db()
        video6.save_to_db()
        
        section1 = SectionModel(title= "software")
        section2 = SectionModel(title= "Outdoor")
        section3 = SectionModel(title= "cars")
        category1 = CategoryModel(title= "Company")
        category2 = CategoryModel(title= "Games")
        
        
        video1.authors.append(author1)
        db.session.commit()
        video3.authors.append(author2)
        db.session.commit()
        video1.authors.append(author3)
        db.session.commit()
        video2.authors.append(author3)
        db.session.commit()
        
        video1.sections.append(section2)
        video2.sections.append(section2)
        video3.sections.append(section2)
        db.session.commit()
        
        video4.sections.append(section1)
        video5.sections.append(section1)
        video6.sections.append(section3)
        db.session.commit()
        
        section1.category.append(category1)
        section3.category.append(category1)
        section2.category.append(category2)
        db.session.commit()
        
        
        sections = category1.section
        print("Section of Category Company: \t")
        print([s.title for s in sections])
            
        sec = category2.section
        print("\nSections of category Games:\t")
        print([s.title for s in sec])
            
        vid = section1.videos
        print("\nVideos of section Software:\t")
        print([v.name for v in vid])
            
        vid = section2.videos
        print("\nVideo of section Outdoor:\t")
        print([v.name for v in vid])
        
        vid = section3.videos
        print("\nVideo of section Cars:\t")
        print([v.name for v in vid])

        
        
        return {"message": "Details are added to database"}, 200
