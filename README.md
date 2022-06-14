
<p align="center">
 <img src="https://files.hyper.pics/hyper/axjsDGPljm.png">
 <h2 align="center">User management panel</h2>
 <p align="center">w/ love by vaul</p>
</p>
  <p align="center">
    <a href="https://github.com/Archivine/panel/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/Archivine/panel?color=0088ff" />
    </a>
    <a href="https://github.com/Archivine/panel/pulls">
      <img alt="Pull requests" src="https://img.shields.io/github/issues-pr/Archivine/panel" />
    </a>
  </p>
 
<h2 align ="center"> Features </h2>

##### USES
* HTML5 for frontend
* Flask for backend
* MongoDB (PyMongo[srv]) for data storage

##### AUTH
* Login
* Invite only register

##### ADMIN
* Ban / unban users
* Generate invites

##### FUNCTIONALITY

* User Controller <ins>**__[auth/controllers/usercontroller.py]__** </ins>
  * Checks passed credentials, then passes them over to the usermodel.

* Admin Controller <ins>**__[auth/controllers/admincontroller.py]__** </ins>
  * Calls admin model functions, literally kept only for "proper" mvc design.
  
* User Model <ins>**__[auth/models/usermodel.py]__** </ins>
  * Basic auth functionality. All the magic happens here.
  
* Admin Model <ins>**__[auth/models/adminmodel.py]__** </ins>
  * Admin panel stuff and functions.
 
 
<h2 align ="center"> Installation </h2>
 
#### Start off by setting up a mongodb cluster
https://www.mongodb.com/basics/clusters/mongodb-cluster-setup  
 
» Create a new database, call it whatever you want.

<br>

#### Clone the repo
» Go to **__[auth/core/database.py]__**  
» Replace the last line of getDatabase() with your collection name  

```python
 return m_client["database_name_here"]
```

<br>

#### Import all of the collections included in the <ins>**[db]**</ins> folder using mongoimport.
» Admin password is `shashmuga` by default.

<br>

#### Install required python dependencies
* Flask
* PyMongo[srv]

<br>

#### Run server.py

**[Optional]** Open <ins>**__[auth/core/config.py]__**</ins>  
Edit it to your liking.


<h3> Made for educational purposes only. Do not, under any circumstances, use it in production. It's terribly coded and lacks a lot. </h3>

*Heavily inspired by znix's php panel.*   
*[Check it out](https://github.com/znixbtw/php-panel-v2)*
