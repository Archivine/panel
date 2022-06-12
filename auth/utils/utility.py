from datetime import datetime
from auth.core.database import getNextSequenceValue

def getCurrentDate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

def createUserTemplate(username, password, inviter):

    user = {
        "uid": getNextSequenceValue(),
        "username": f"{username}",
        "password": f"{password}", # <--- has to be already hashed and decoded
        "invited_by": f"{inviter}",
        "created_at": f"{getCurrentDate()}",
        "admin": False,
        "banned": False
    }

    return user

def createInviteTemplate(invite, inviter):

    invite = {
        "invite": f"{invite}",
        "inviter": f"{inviter}",
        "created_at": f"{getCurrentDate()}"
    }
    
    return invite

def decodeBytearray(param):
    x = bytes(param)
    y = x.decode("utf-8")
    return y