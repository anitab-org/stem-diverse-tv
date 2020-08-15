from app.database.sqlalchemy_extension import db



class VideoModel(db.Model):

    # Specifying table
    __tablename__ = "videos"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    url = db.Column(db.Text())
    preview_url = db.Column(db.Text())
    title = db.Column(db.String(200))
    published = db.Column(db.Integer)
    source = db.Column(db.String(50))
    channel = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    archived = db.Column(db.Boolean)
    free_to_reuse = db.Column(db.Boolean)
    authorised_to_reuse = db.Column(db.Boolean)
    
    def json(self):
            '''Returns VideoModel object in json format.'''
            return {
                "id": self.id,
                "name": self.name,
                "url": self.url,
                "preview_url": self.preview_url,
                "title": self.title,
                "published": self.published,
                "source": self.source,
                "channel": self.channel,
                "duration": self.duration,
                "archived": self.archived,
                "free_to_reuse": self.free_to_reuse,
                "authorised_to_reuse": self.authorised_to_reuse
            }
            
    def find_by_id(cls, _id: int) -> 'VideoModel':
        '''Returns a particular video of given id.'''
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self) -> None:
        '''Add video to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes video from the database.'''
        db.session.delete(self)
        db.session.commit()

