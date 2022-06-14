import pymongo
import bcrypt
from auth.core.config import getClusterUrl
from pymongo import MongoClient



def getDatabase():

    m_client = MongoClient(getClusterUrl())  

    return m_client["mvc_test"]

db = getDatabase()

def getUsersCollection():

    users = db["users"]

    return users

def getIncrementCollection():

    increment = db["increment"]

    return increment

def getInvitesCollection():

   
    invites = db["invites"]

    return invites

def getNextSequenceValue():

    seq = getIncrementCollection().find_one_and_update({"_id": "user-id"}, {"$inc":{"sequence_value":1}})

    return seq["sequence_value"]




