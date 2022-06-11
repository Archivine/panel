from auth.core.database import getInvitesCollection, getUsersCollection
from auth.utils.utility import createInviteTemplate

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
    
  


def login(username, password, hwid):
    if usernameCheck(username):
        x = valueQuery(f"select * from users WHERE username = %s", [username])
        row = x[0]
        hashed_pass = bytes(row[2])
        passw = password.encode("utf8")
        print(hashed_pass)
        if row[3] == "null" or row[3] == "None" or row[3] is None:
            db.valueQueryNoReturn(
                f"UPDATE `users` SET `hwid` = ? WHERE `username` = %s",
                [hwid, username],
            )
        if bcrypt.checkpw(passw, hashed_pass):
            ret = {
                "status": "success",
                "message": f"Successfully logged in as {decodeBytearray(row[1])}",
                "uid": row[0],
                "username": decodeBytearray(row[1]),
                "hwid": decodeBytearray(row[3]),
                "isadmin": row[4],
                "isBanned": row[5],
                "joinedAt": str(row[7]),
            }

            return ret

        else:

            ret = {"status": "failed", "message": "Invalid password"}
            return ret
    else:

        ret = {"status": "failed", "message": "Invalid username"}
        return ret


def register(username, password, invite):
    if invCheck(invite):

        inviter = getInviter(invite)

        if inviter:

            valueQueryNoReturn(
                "INSERT INTO `users` (`username`, `password`, `invitedBy`) VALUES (%s, %s, %s)",
                [username, password, inviter],
            )

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