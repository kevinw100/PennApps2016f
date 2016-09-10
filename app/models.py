
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
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False)
    password_hash = Column(String, nullable=False)
    def __init__(self, first_name, last_name, email, password_hash):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return '<User %r %r>' % (self.first_name, self.last_name)

class Candidates(Base):
    __tablename__ = 'Candidates'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    election_id = Column(Integer, ForeignKey('Election.id'))
    eliminated = Column(Boolean)

    def __init__(self, name, election_id, eliminated):
        self.name = name
        self.election_id = election_id
        self.eliminated = eliminated

    def __repr__(self):
        return '<Candidate %r election: %d>' % (self.name, self.election_id)

class Votes(Base):
    __tablename__ = 'Votes'
    user_id = Column(Integer, ForeignKey('User.id'), primary_key = True)
    election_id = Column(Integer, ForeignKey('Election.id'), primary_key = True)
    first = Column(Integer, ForeignKey('Candidate.id'), nullable = True)
    second = Column(Integer, ForeignKey('Candidate.id'), nullable = True)
    third = Column(Integer, ForeignKey('Candidate.id'), nullable = True)

    ForeignKeyConstraint(['user_id','election_id'], ['User.id', 'Election.id'])


    def __init__(self, user_id, election_id, first, second, third):
    	self.user_id = user_id
    	self.election_id = election_id
        self.first = first
        self.second = second
        self.third = third

    def __repr__(self):
        return '<Votes %r %r with votes : %r %r %r >' % (self.election_id, self.last_name, self.first, self.second, self.third)


#class Rank(Base):
#	__tablename__ = 'Voter Rank'
#	election_id = Column(Integer, ForeignKey('Election.id'))


class Election(Base):
	__tablename__ = 'Elections'
	id = Column(Integer, primary_key=True)
	creator_id = Column(Integer, ForeignKey('User.id'))
	description = Column(String, nullable = True)

	def __init__(self, creator_id, description):
		self.creator_id = creator_id
		self.description = description

	def __repr__(self):
		return '<Election %r %r>' % (self.creator_id, self.description)

