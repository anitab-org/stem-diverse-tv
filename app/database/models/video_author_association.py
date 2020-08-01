from app.database.sqlalchemy_extension import db

owns = db.Table('owns',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('video_id', db.Integer, db.ForeignKey('videos.id'))
    )
