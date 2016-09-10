#sqlalchemy import 
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

#authentication shit 
from Crypto.Hash import SHA256

import itertools
import math
import random


engine = create_engine('sqlite:///./db/database_2.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def userSignup (first_Name, last_Name, email, password):
    exists = User.query.filter(User.email == email).first()
    if not exists:
        phash = SHA256.new(password).hexdigest()
        print (password, phash)
        u = User(first_name, last_name, email, phash)
        db_session.add(u)
        db_session.commit()
        return (u.id, '')
    else:
        return (False, 'This email is already in use.')

def validateLogin(email, password):
    u = User.query.filter(User.email == email).first()
    if u:
        phash = SHA256.new(password).hexdigest()
        print (password, phash)
        print u.password_hash
        if phash == u.password_hash:
            clone = User(u.first_name, u.last_name, u.email, '')
            return clone
    return False
