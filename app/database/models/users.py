from app.database.sqlalchemy_extension import db

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, timedelta


class UserModel(db.Model):

    # Specifying table
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(30))
    email = db.Column(db.String(100))
    firebase_id = db.Column(db.String(50))
    password_hash = db.Column(db.String(100))
    registration_date = db.Column(db.Integer)
    terms_and_conditions_checked = db.Column(db.Boolean)
    access_rights = db.Column(db.Integer)
    is_email_verified = db.Column(db.Boolean)
    email_verification_date = db.Column(db.Integer)


    def __init__(self, name, firebase_id, username, email, password, terms_and_conditions_checked):
        self.name = name
        self.username = username
        self.email = email
        self.set_password(password)
        self.registration_date = str(date.today())
        self.terms_and_conditions_checked = terms_and_conditions_checked
        self.access_rights = 0
        self.firebase_id = firebase_id
        
        
    def json(self):
            '''Returns UserModel object in json format.'''
            return {
                "id": self.id,
                "name": self.name,
                "username": self.username,
                "email": self.email,
                "firebase_id": self.firebase_id,
                "password_hash": self.password_hash,
                "registration_date": self.registration_date,
                "terms_and_conditions_checked": self.terms_and_conditions_checked,
                "access_rights": 0, # access_rights will have to be given by admin
                "is_email_verified": is_email_verified,
                "email_verification_date": email_verification_date,
            }
            
    
    @classmethod
    def find_by_id(cls, _id: int) -> 'UserModel':
        '''Returns a particular user of given id.'''
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_username(cls, username: str) -> 'UserModel':
        '''Returns a particular user of given username.'''
        return cls.query.filter_by(username=username).first()
    
    @classmethod        
    def find_by_firebase_id(cls, firebase_id: str) -> 'UserModel':
        '''Returns user of given firebase_id.'''
        return cls.query.filter_by(firebase_id=firebase_id).first()
    
    @classmethod        
    def find_by_email(cls, email: str) -> 'UserModel':
        '''Returns user of given email.'''
        return cls.query.filter_by(email=email).first()
    
    def set_password(self, password_plain_text: str) -> None:
        """Sets user password"""
        self.password_hash = generate_password_hash(password_plain_text)

    def save_to_db(self) -> None:
        '''Add user to database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        '''Deletes user from the database.'''
        db.session.delete(self)
        db.session.commit()

