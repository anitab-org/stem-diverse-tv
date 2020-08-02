from app.database.models.section_video import section_video
from app.database.sqlalchemy_extension import db

class SectionModel(db.Model):

    # Specifying table
    __tablename__ = "section"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    videos = db.relationship('VideoModel', secondary=section_video, backref=db.backref('sections', lazy = 'dynamic'))
    
    def save_to_db(self) -> None:
        '''Add section to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes section from the database.'''
        db.session.delete(self)
        db.session.commit()
