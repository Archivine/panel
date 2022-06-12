import bcrypt

from auth.core.database import getInvitesCollection, getUsersCollection
from auth.utils.utility import createInviteTemplate, createUserTemplate

def usernameCheck(username):
   
    for x in getUsersCollection().find({"username": f"{username}"}):
        return True
    return False
    

def invCheck(invite):
    for x in getInvitesCollection().find({"invite": f"{invite}"}):
        return True
    return False


def getInviter(invite):
    for x in getInvitesCollection().find({"invite": f"{invite}"}):
        inviter = x["inviter"]
        return inviter
    

def login(username, password):
    if usernameCheck(username):
        for x in getUsersCollection().find({"username": f"{username}"}):
            hashedPassword = x["password"].encode("utf8")
            encodedPassword = password.encode("utf8")

            __username__ = x["username"]
            __uid__ = x["uid"]
            __isAdmin__ = x["admin"]
            __isBanned__ = x["banned"]
            __inviter__ = x["invited_by"]
            __createdAt__ = x["created_at"]
            if bcrypt.checkpw(encodedPassword, hashedPassword):
                ret = {
                    "status": "success",
                    "message": f"Successfully logged in as {__username__}",
                    "uid": __uid__,
                    "username": f"{__username__}",
                    "isAdmin": __isAdmin__,
                    "isBanned":  __isBanned__,
                    "invited_by": f"{__inviter__}",
                    "created_at": f"{__createdAt__}",
                }

                return ret

            else:

                ret = {
                    "status": "failed", 
                    "message": "Invalid password"
                }

                return ret
    else:

        ret = {
            "status": "failed", 
            "message": "Invalid username"
        
        }
        return ret


def register(username, password, invite):
    if invCheck(invite):

        inviter = getInviter(invite)

        if inviter:
            encodedPassword = password.encode("utf8")
            hashedPassword = bcrypt.hashpw(encodedPassword, bcrypt.gensalt())
            getUsersCollection().insert_one(createUserTemplate(username, hashedPassword.decode(), inviter))
            getInvitesCollection().delete_one({"invite": f"{invite}"})

            ret = {
                "status": "success",
                "message": f"Successfully registered as {username}",
            }

            return ret
    else:

        ret = {
            "status": "failed",
            "message": f"Invalid invite",
        }

        return ret