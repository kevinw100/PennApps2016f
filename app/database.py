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

def userSignUp(first_name, last_name, email):
#    exists = User.query.filter(User.email == email).first()
#    if not exists:
        user = User(first_name, last_name, email)
        db_session.add(user)
        db_session.commit(user)
        return (user.id, '')
#    else:
#        return (False, 'This email is already in use.')

def authenticateLogin(email):
    user = User.query.filter(User.email == email).first()
    if user:
        phash = SHA256.new(password).hexdigest()
        print (password, phash)
        print u.password_hash
        if phash == u.password_hash:
            clone = User(u.first_name, u.last_name, u.email, '')
            return clone
    return False

def createElection(candidates):
    return None

def getElection(election_id):
    return None

def getCandidates(candidate_ids):
    return None

def userVotes(first, second, third):
    return None

def getElectionResults(election_id):
    return None
