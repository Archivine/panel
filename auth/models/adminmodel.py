from auth.core.database import getInvitesCollection, getUsersCollection
from auth.utils.utility import createInviteTemplate, getCount

def banUser(user):

    getUsersCollection().find_one_and_update({"username": f"{user}"},  { '$set': {"banned": True} })


def unbanUser(user):

    getUsersCollection().find_one_and_update({"username": f"{user}"},  { '$set': {"banned": False} })


def generateInvite(user, invite):

    getInvitesCollection().insert_one(createInviteTemplate(invite, user))


def listUsers():

    x = getUsersCollection().find({})

    return x


def getTotalUsers():

    return getCount(listUsers())


def getBannedUsers():

    return getCount(getUsersCollection().find({"banned": True}))


def listBannedUsers():

    banned = []

    for i in getUsersCollection().find({"banned": True}):
        banned.append(i['username'])

    return banned


def listInvites():

    x = getInvitesCollection().find({})
    return x


def getTotalInvites():

    return getCount(listInvites())