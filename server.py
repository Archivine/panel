from flask import *
from flask import render_template
from auth.utils.utility import getCurrentDate
from auth.core.database import getInvitesCollection
from auth.models.usermodel import register, login
import bcrypt

server = Flask(__name__)




#getInvitesCollection().insert_one({"invite": "sex", "inviter": "vaul", "created_at": f"{getCurrentDate()}"})

print(login("hi", "black"))
