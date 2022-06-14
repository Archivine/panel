import bcrypt
from auth.models.usermodel import login, register, updatePassword

def checkPassword(password):
    
    if not password:
        return "Blank password"

    elif len(password) < 6:
        return "Password too short"

    elif len(password) > 20:
        return "Password too long"

    elif not password.isalnum():
        return "Password must contain only alphanumericals"

    else:
        return True


def checkUsername(username):

    if not username:
        return "Blank username"

    elif len(username) < 4:
        return "Username too short"

    elif len(username) > 20:
        return "Username too long"

    elif not username.isalnum():
        return "Username must contain only alphanumericals"

    else:
        return True


def checkCredentials(username, password):

    x = checkUsername(username)
    y = checkPassword(password)

    if x is True and y is True:

        return True

    else:

        if x is not True:
            return x 

        elif y is not True:
            return y
   
        
def loginController(username, password):

    y = checkPassword(password)

    if y is True:

        x = login(username, password)
        return x

    else:

        ret = {"status": "failed", "message": "Invalid password"}

        return ret


def registerController(username, password, invite):

        y = checkCredentials(username, password)
    
        if y is True:

            x = register(username, password, invite)

            return x
                
        else:

            ret = {"status": "failed", "message": f"{y}"}
            return ret
    

def updatePasswordController(username, password, newPassword):

    y = checkCredentials(username, password)
    h = checkPassword(newPassword)
   
    if y is True and h is True:
       
        x = updatePassword(username, password, newPassword)
        return x

    else:
        
        message = ""

        if y is not True:
            message = y

        elif h is not True:
            message = h

        ret = {
            "status": "failed",
            "message": f"{message}"
        }

        return ret