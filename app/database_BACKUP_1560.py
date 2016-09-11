from sqlalchemy import Column, Boolean, BigInteger, DateTime, ForeignKey,
Integer, Numeric, String, Table, Text
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.expression import func

import itertools
import math
import random

engine = create_engine('sqlite:///.db/database.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.creat_all(bind = engine)

import models

def userSignUp(first_name, last_name, email, password):
    exists = User.query.filter(User.email == email).first()
    if not exists:
        user = User(first_name, last_name, email, password)
        db_session.add(user)
        db_session.commit(user)
        return (user.id, '')
    else:
        return (False, 'This email has already been taken.')

def authenticateLogin(email, password):
    user = User.query.filter(User.email == email).first()
    if user:
        if user.password == password
            clone = User(user.first_name, user.last_name, user.email)
            return clone
    return (False, 'The email or password is incorrect.')

# candidates - a list of strings containing the names of the candidates
# user_id - the id of the user that created the election
# description - a string describing the election
def createElection(user_id, description, candidates):
    try:
        election = Election(user_id, description)
        db_session.add(election)
        db_session.commit(election)
        for c in candidates:
            candidate = Candidates(c, election.id, False)
            db_session.add(candidate)
            db_session.commit(candidate)
        return election.id
    except Exception, e:
        print e
        return False

def getElection(election_id):
<<<<<<< HEAD
    return None
=======
    election = Election.query.filter(Election.id == election_id).first()
    return election
>>>>>>> 51c3a6328c25a18c54d5e5f1e497febc3758ee3e

def getCandidates(election_id):
    try:
        candidates = Candidates.query.filter(Candidates.election_id == election_id)
        candidate_list = []
        for candidate in candidates:
            candidate_list.append(candidate)
        return candidate_list
    except Exception, e:
        print e
        return False

def userVotes(user_id, election_id, first, second, third):
    vote = Votes(user_id, election_id, first, second, third)
    return vote

def getElectionResults(election_id):
    return None
