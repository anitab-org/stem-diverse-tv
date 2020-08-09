from app.database.sqlalchemy_extension import db



class UserModel(db.Model):

    # Specifying table
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password_hash = db.Column(db.String(100))
    registration_date = db.Column(db.Integer)
    terms_and_conditions_checked = db.Column(db.Boolean)
    access_rights = db.Column(db.Integer)
    is_email_verified = db.Column(db.Boolean)
    email_verification_date = db.Column(db.Integer)

    def json(self):
            '''Returns UserModel object in json format.'''
            return {
                "id": self.id,
                "name": self.name,
                "username": self.username,
                "email": self.email,
                "password_hash": self.password_hash,
                "registration_date": self.registration_date,
                "terms_and_conditions_checked": self.terms_and_conditions_checked,
                "access_rights": 0, # access_rights will have to be given by admin
                "is_email_verified": is_email_verified,
                "email_verification_date": email_verification_date,
            }
            
    def find_by_id(cls, _id: int) -> 'UserModel':
        '''Returns a particular user of given id.'''
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self) -> None:
        '''Add user to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes user from the database.'''
        db.session.delete(self)
        db.session.commit()

