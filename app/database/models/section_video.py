from app.database.sqlalchemy_extension import db

section_video = db.Table('section_video',
    db.Column('video_id', db.Integer, db.ForeignKey('videos.id')),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'))
    )
