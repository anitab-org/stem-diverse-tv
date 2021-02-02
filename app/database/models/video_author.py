from app.database.sqlalchemy_extension import db

video_author = db.Table(
    "video_author",
    db.Column("author_id", db.Integer, db.ForeignKey("author.id")),
    db.Column("video_id", db.Integer, db.ForeignKey("videos.id")),
)
