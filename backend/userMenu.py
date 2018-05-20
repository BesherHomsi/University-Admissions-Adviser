#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import mysql.connector
import http.cookies as Cookie 
import random
import cgi
import os

def printHeader():
   print ("""Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?
<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.0 Strict//EN"
	"DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Raleway:100,600" rel="stylesheet" type="text/css">

        <!-- Styles -->
        <link href="css/main.css" rel="stylesheet" type="text/css">
        <link href="../css/navBar.css" rel="stylesheet" type="text/css">
    <title>Uaa</title>

</head>
<body>""")

def navBar(email):
	print("""<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Uaa</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Menu</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>

        </ul>
			<a class="my-2 my-sm-0 loginButton" type="nav-link" href="#">%s</a>
			<a class="btn btn-outline-success my-2 my-sm-0" type="nav-link" href="http://localhost/db/backend/logout.py">Log out</a>
      </div>
  </nav> """% email)


def userMenu():
	print("""<ul class="">
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/editProfileStudent.py" style="margin:10px;">Edit Profile</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/AddUniversityForm.py" style="margin:10px;">Add University</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="universities/displayUniversities.py" style="margin:10px;">Add More Details for a University</a>
          </li>

        </ul>""")
		
def aUserMenu():
	print("""<ul class="">
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/editProfileA.py" style="margin:10px;">Edit Profile</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/AddUniversityForm.py" style="margin:10px;">Add University</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="universities/displayUniversities.py" style="margin:10px;">Add More Details for a University</a>
          </li>

        </ul>""")	

def uUserMenu():
	print("""<ul class="">
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/editProfileU.py" style="margin:10px;">Edit Profile</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="http://localhost/db/backend/AddUniversityForm.py" style="margin:10px;">Add University</a>
          </li>
          <li class="">
            <a class="btn btn-outline-success" href="universities/displayUniversities.py" style="margin:10px;">Add More Details for a University</a>
          </li>

        </ul>""")	

printHeader()
#form = cgi.FieldStorage()

try:
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
	c = conn.cursor()
	if "HTTP_COOKIE" in os.environ:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		#print("<p>cookie: %s</p>"% cookie["session"].value)
		c.execute('SELECT * FROM members WHERE sessionID = %s ',(cookie["session"].value,))
		row = c.fetchone()
		if row:
			navBar(row[5])
			if(row[7] == "s"):
				userMenu()	
			if(row[7] == "u"):
				UuniMenu()
			if(row[7] == "a"):
				aUserMenu()
			
		else:
			print("<p>email: Not Found!!</p>")	
except Exception as e:
	print(e)
	
	
print ("</body></html>") 
