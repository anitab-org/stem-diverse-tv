from app.database.models.video_author_association import *

class AuthorModel(db.Model):

    # Specifying table
    __tablename__ = "author"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    profile_image = db.Column(db.Text())
    owner_of = db.relationship('VideoModel', secondary=owns, backref=db.backref('authors', lazy = 'dynamic'))
    
    def save_to_db(self) -> None:
        '''Add author to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes author from the database.'''
        db.session.delete(self)
        db.session.commit()
