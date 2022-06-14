import string
import random
from auth.models.adminmodel import generateInvite, listInvites, getTotalUsers, getTotalInvites, listUsers, getBannedUsers, listBannedUsers, banUser, unbanUser

def manageUserBanStateController(user):

    if user in listBannedUsersController():
        unbanUser(user)
        
    else:
        banUser(user)


def generateInviteController(user):

    invite = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(16))
    generateInvite(user, invite)


def listUsersController():

    return listUsers()


def getTotalUsersController():

    return getTotalUsers()


def getBannedUsersController():

    return getBannedUsers()


def listBannedUsersController():

    return listBannedUsers()


def listInvitesController():

    return listInvites()


def getTotalInvitesController():

    return getTotalInvites()
