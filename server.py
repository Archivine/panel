from flask import *
from flask import render_template
from auth.utils.utility import getCurrentDate, createInviteTemplate, decodeBase64
from auth.controllers.usercontroller import loginController, registerController, updatePasswordController
from auth.controllers.admincontroller import generateInviteController, listInvitesController, getTotalUsersController, getBannedUsersController, listBannedUsersController, getTotalInvitesController, listUsersController, manageUserBanStateController
from auth.core.config import getSiteInfo, getEmbedInfo

server = Flask(__name__)
server.secret_key = 'secret-key-here'

@server.route("/")
def home():

	if 'loggedIn' in session:

		if session['username'] in listBannedUsersController():
			return redirect(url_for('banned'))

		return render_template('index.html', 
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			IS_ADMIN = session['isAdmin'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)

	return redirect(url_for('login'))


@server.route("/login", methods=['GET', 'POST'])
def login():
	
	label =''

	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

		username = request.form['username']
		password = request.form['password']

		x = loginController(username, password)

		if x["status"] == "success":

			session['loggedIn'] = True
			session['uid'] = x['uid']
			session['username'] = x['username']
			session['creationDate'] = x['created_at']
			session['isAdmin'] = x['isAdmin']
			
			return redirect(url_for('home'))

		elif x["status"] == "failed":
			label = x["message"]

	return render_template('login.html', 
		LOGIN_LABEL = label,
		SITE_TITLE = getSiteInfo()["site_title"], 
		SITE_ICON = getSiteInfo()["site_icon"], 
		SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
		OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
		OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
		OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
		OG_SITE_URL = getEmbedInfo()["og_site_url"], 
		OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
	)


@server.route('/register', methods=['GET', 'POST'])
def register():

	label =''

	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'invite' in request.form:

		username = request.form['username']
		password = request.form['password']
		invite = request.form['invite']

		x = registerController(username, password, invite)

		if x["status"] == "success":
			return redirect(url_for('login'))

		elif x["status"] == "failed":
			label = x["message"]

	return render_template('register.html', 
		REGISTER_LABEL = label,
		SITE_TITLE = getSiteInfo()["site_title"], 
		SITE_ICON = getSiteInfo()["site_icon"], 
		SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
		OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
		OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
		OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
		OG_SITE_URL = getEmbedInfo()["og_site_url"], 
		OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
	)


@server.route('/user', methods=['GET', 'POST'])
def user():

	if 'loggedIn' in session:

		if session['username'] in listBannedUsersController():
			return redirect(url_for('banned'))

		label = ''
		if request.method == 'POST' and 'oldPassword' in request.form and 'newPassword' in request.form:

			oldPassword = request.form['oldPassword']
			newPassword = request.form['newPassword']

			x = updatePasswordController(session['username'], oldPassword, newPassword)

			if x["status"] == "success":
				return redirect(url_for('logout'))

			elif x["status"] == "failed":
				label = x["message"]

		return render_template('user.html', 
			RESET_LABEL = label,
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			IS_ADMIN = session['isAdmin'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)

	return redirect(url_for('login'))


@server.route('/admin')
def admin():

	if 'loggedIn' in session:

		if session['username'] in listBannedUsersController():
			return redirect(url_for('banned'))

		if session['isAdmin'] is not True:
			return redirect(url_for('home'))
		return render_template('admin.html', 
			TOTAL_USERS = getTotalUsersController(),
			TOTAL_INVITES = getTotalInvitesController(),
			TOTAL_BANS = getBannedUsersController(),
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			IS_ADMIN = session['isAdmin'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)
	return redirect(url_for('login'))


@server.route('/admin/invites', methods = ['GET', 'POST'])
def invites():

	if 'loggedIn' in session:

		if session['username'] in listBannedUsersController():
			return redirect(url_for('banned'))

		if session['isAdmin'] is not True:
			return redirect(url_for('home'))

		if request.method == 'POST':
			print(request)
			generateInviteController(session['username'])

		return render_template('invites.html', 
			INVITES = listInvitesController(),
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			IS_ADMIN = session['isAdmin'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)

	return redirect(url_for('login'))


@server.route('/admin/users', methods = ['GET', 'POST'])
def users():

	if 'loggedIn' in session:

		if session['username'] in listBannedUsersController():
			return redirect(url_for('banned'))

		if session['isAdmin'] is not True:
			return redirect(url_for('home'))

		if request.method == 'POST':
			form = request.form.to_dict()
			
			if "Ban" in form.values() or "Unban" in form.values():
				x = list(form.keys())
				print(x[0])
				manageUserBanStateController(x[0])

		return render_template('users.html', 
			USERS = listUsersController(),
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			IS_ADMIN = session['isAdmin'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)
	return redirect(url_for('login'))
	

@server.route('/banned')
def banned():

	if 'loggedIn' in session:

		state = False

		if session['username'] not in listBannedUsersController():
			return redirect(url_for('home'))
		
		return render_template('banned.html', 
			USERNAME = session['username'],
			UID = session['uid'],
			CREATION_DATE = session['creationDate'],
			SITE_TITLE = getSiteInfo()["site_title"], 
			SITE_ICON = getSiteInfo()["site_icon"], 
			SITE_THEME_COLOR = getSiteInfo()["site_theme_color"], 
			OG_SITE_TITLE = getEmbedInfo()["og_site_title"], 
			OG_SITE_DESCRIPTION = getEmbedInfo()["og_site_description"], 
			OG_SITE_IMAGE = getEmbedInfo()["og_site_image"], 
			OG_SITE_URL = getEmbedInfo()["og_site_url"], 
			OG_LARGE_SUMMARY_CARD = getEmbedInfo()["og_large_summary_card"]
		)	

	return redirect(url_for('login'))


@server.route('/logout')
def logout():

	if 'loggedIn' in session:
		session.clear()
 
	return redirect(url_for('login'))
	

if __name__ == "__main__":
	server.run(port=7777, debug=True)

	
#░░░░░░░░░░░░░▄▄▀▀▀▀▀▀▄▄
#░░░░░░░░░░▄▄▀▄▄▄█████▄▄▀▄
#░░░░░░░░▄█▀▒▀▀▀█████████▄█▄
#░░░░░░▄██▒▒▒▒▒▒▒▒▀▒▀▒▀▄▒▀▒▀▄
#░░░░▄██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄
#░░░░██▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌
#░░░▐██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐█
#░▄▄███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
#▐▒▄▀██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌
#▌▒▒▌▒▀▒▒▒▒▒▒▄▀▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒█▌
#▐▒▀▒▌▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒▀▀▀▀▄▒▐
#░█▒▒▌▒▒▒▒▒▒▒▒▀▀▒▀▒▒▐▒▄▀██▀▒▒▒▌
#░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒█
#░░░▀▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▄▀
#░░░▐▒▒▒▒▒▒▒▒▒▄▀▐▒▒▒▒▒▐▒▒▒▒▄▀
#░░▄▌▒▒▒▒▒▒▒▄▀▒▒▒▀▄▄▒▒▒▌▒▒▒▐▀▀▀▄▄▄
#▄▀░▀▄▒▒▒▒▒▒▒▒▀▀▄▄▄▒▄▄▀▌▒▒▒▌░░░░░░
#▐▌░░░▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀░░░░░░░
#░█░░░░░▀▄▄▒▒▒▒▒▒▒▒▒▒▒▒▄▀░█░░░░░░░
#░░█░░░░░░░▀▄▄▄▒▒▒▒▒▒▄▀░░░░█░░░░░░
#░░░█░░░░░░░░░▌▀▀▀▀▀▀▐░░░░░▐▌░░░░░
