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
