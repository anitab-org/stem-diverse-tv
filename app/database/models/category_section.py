from app.database.sqlalchemy_extension import db

category_section = db.Table('category_section',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'))
    )
