from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin
from uuid import uuid4
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)



class Whatsit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())


class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
   
    def __init__(self, username, email, password, first_name='', last_name= ''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)


class Animal(db.Model):
    id =db.Column(db.String(50), primary_key=True)
    species = db.Column(db.String(50), nullable=False)
    latin_name= db.Column(db.String(200), default=None)
    size_cm = db.Column(db.Integer)
    diet = db.Column(db.String(255))
    lifespan = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable =False)
    image = db.Column(db.String(100), default=None)
    price = db.Column(db.Float(2), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __init__(self, dict):
        self.id= str(uuid4())
        self.species = dict['species'].title()
        self.description = dict['description']
        self.price = dict['price']
        #optional values
        self.image = dict.get('image') #if there is no image, the value is automatically set to NONE (due to get method)
        self.size_cm = dict.get('size_cm', 0) #second parameter sets default size to 0
        self.latin_name = dict.get('latin_name')
        self.diet = dict.get('diet', 'unknown')
        self.lifespan = dict.get('lifespan', 0)

    #write a function to translate this object to a dictionary for jsonification
    def to_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'latin_name': self.latin_name,
            'image': self.image,
            'description': self.description,
            'price': self.price,
            'size_cm': self.size_cm,
            'diet': self.diet,
            'lifespan': self.lifespan,
            'created_on': self.created_on
        }
    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(300), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
 