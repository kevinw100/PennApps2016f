from sqlalchemy import Column, Boolean, BigInteger, DateTime, ForeignKey, Integer, Numeric, String, Table, Text
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
		if user.password == password:
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
	election = Election.query.filter(Election.id == election_id).first()
	return election

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

def addVote(user_id, election_id, candidate_id, first, second, third)
	try:
		userExists = Votes.query(Users.id == user_id and Elections.id == election_id)
		if userExists is False:
			user = Users.query.filter(Users.id == user_id).first()
			user_id = user.getId(user)
			election = Election.query.filter(Elections.id == election_id).first()
			election_id = election.getId()
			vote = Votes(user, election, first, second, third)
			db_session.add(vote)
			db_session.commit()
			return True;
		else:  
			return False
	except Exception e:
		print e;
		return False



def calculateElection(election_id)
	election = Elections.query(Elections.id == election_id).first()
	votesList = Votes.query(Votes.election_id == election_id).all()
	candidates = getCandidates(election_id)

	listSize = len(candidates)
	
	counters = []

	if listSize is 1:
		return candidates[0]


	for i in xrange(listSize):
		#Counters is an int array that corresponds to the votes of all the candidates
		#invariant: counters[idx] corresponds to candidates[idx]
		counters.append(0)
	print(counters)

	#tally the votes for each candidate
	for vote in votesList:
		v = vote.getFirst
		result = find(candidates,v)
		idx = result[0]
		#candidate = result[1]
		counters[idx] += 1

	res = maxIntList(counters)

	tgtIdx = res[0]

	loser = candidates[tgtIdx]

	#determines who voted for the round's loser and then removes their votes.
	for vote in votesList:
		v = vote.getFirst
		if v is loser.getId:
			v.shiftVotes

	#continue until there is only 1 man left standing (for alternative vote)
	return calculateElection(election_id)

def find(list, id):
	for i in xrange(len(list)):
		if list[i] == id:
			return (i, id)
	return (False, "The item was not found")

def minIntList(list):
	min = (-1, sys.maxint)
	for(i in xrange(len(list))):
		if list[i] > max[1]:
			max = (i,list[i])
	return max









