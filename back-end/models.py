from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

from config import db


class Lamborghini(db.Model, SerializerMixin):
    __tablename__ = 'Lamborghinis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError('Name must be at least 1 character long')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 1:
            raise ValueError('Description must be at least 1 character long')
        return description

    @validates('image_url')
    def validate_image_url(self, key, image_url):
        if len(image_url) < 1:
            raise ValueError('Image URL must be at least 1 character long')
        return image_url
    
    def __repr__(self):
        return f'<Lamborghini {self.name}>'

class Ferrari(db.Model, SerializerMixin):
    __tablename__ = 'Ferraris'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError('Name must be at least 1 character long')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 1:
            raise ValueError('Description must be at least 1 character long')
        return description

    @validates('image_url')
    def validate_image_url(self, key, image_url):
        if len(image_url) < 1:
            raise ValueError('Image URL must be at least 1 character long')
        return image_url
    def __repr__(self):
        return f'Ferrari {self.name}>'

class Mercedes(db.Model, SerializerMixin):
    __tablename__ = 'Mercedes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError('Name must be at least 1 character long')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 1:
            raise ValueError('Description must be at least 1 character long')
        return description

    @validates('image_url')
    def validate_image_url(self, key, image_url):
        if len(image_url) < 1:
            raise ValueError('Image URL must be at least 1 character long')
        return image_url
    def __repr__(self):
        return f'Mercedes {self.name}>'

class Porsche(db.Model, SerializerMixin):
    __tablename__ = 'Porsches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    image_url = db.Column(db.String(500))
    price = db.Column(db.Float)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError('Name must be at least 1 character long')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 1:
            raise ValueError('Description must be at least 1 character long')
        return description

    @validates('image_url')
    def validate_image_url(self, key, image_url):
        if len(image_url) < 1:
            raise ValueError('Image URL must be at least 1 character long')
        return image_url
    def __repr__(self):
        return f'Porsche {self.name}>'
      
class BMW(db.Model, SerializerMixin):
      __tablename__ = 'BMWS'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    image_url = db.Column(db.String(500))
    price = db.Column(db.Float)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 1:
            raise ValueError('Name must be at least 1 character long')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 1:
            raise ValueError('Description must be at least 1 character long')
        return description

    @validates('image_url')
    def validate_image_url(self, key, image_url):
        if len(image_url) < 1:
            raise ValueError('Image URL must be at least 1 character long')
        return image_url
    def __repr__(self):
        return f'BMW {self.name}>'