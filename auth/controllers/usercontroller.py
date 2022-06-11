


def checkPassword(password):
    if not password:
        return "blank password"
    elif len(password) < 6:
        return "password too short"
    elif len(password) > 20:
        return "password too long"
    else:
        return True

def checkUsername(username):
    if not username:
        return "blank username"
    elif len(username) < 4:
        return "username too short"
    elif len(username) > 20:
        return "username too long"
    elif not username.isalnum():
        return "username must contain only alphanumericals"
    else:
        return True

def checkCredentials(username, password):
    x = checkUsername(username)
    y = checkPassword(password)
    if x and y:
        return True
    else:
        return str(x) + " | " + str(y)
        
def loginController(username, password, hwid):
    y = checkCredentials(username, password)
    if y:
        x = login(username, password.decode(), hwid)
        return x
    else:
        ret = {"status": "failed", "message": str(y)}
        return ret