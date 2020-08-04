from app.database.sqlalchemy_extension import db
from app.database.models.video_author import video_author


class AuthorModel(db.Model):

    # Specifying table
    __tablename__ = "author"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    profile_image = db.Column(db.Text())
    videos = db.relationship('VideoModel', secondary=video_author, backref=db.backref('authors', lazy = 'dynamic'))
    
    def save_to_db(self) -> None:
        '''Add author to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes author from the database.'''
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_by_name(cls, name: str) -> 'AuthorModel':
        return cls.query.filter_by(name=name).first()
