from app.database.sqlalchemy_extension import db
from app.database.models.category_section import category_section

class CategoryModel(db.Model):

    # Specifying table
    __tablename__ = "category"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    section = db.relationship('SectionModel', secondary=category_section, backref=db.backref('category', lazy = 'dynamic'))
    
    def save_to_db(self) -> None:
        '''Add category to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes category from the database.'''
        db.session.delete(self)
        db.session.commit()
