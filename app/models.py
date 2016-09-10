
# from app import db

# class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    nickname = db.Column(db.String(64), index=True, unique=True)
#    email = db.Column(db.String(120), index=True, unique=True)

#    def __repr__(self):
#        return '<User %r>' % (self.nickname)

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r %r>' % (self.first_name, self.last_name)

class Candidates(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Candidate %r>' % (self.name)

class Votes(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, primary_key = True)
    rank =
