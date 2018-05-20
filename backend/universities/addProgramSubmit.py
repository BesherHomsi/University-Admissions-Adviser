#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import http.cookies as Cookie  
import random
import cgi
import os
import mysql.connector

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
  
printHeader()
form = cgi.FieldStorage()


try:
	data = (cgi.escape(form['programName'].value ), cgi.escape(form['programType'].value ), cgi.escape(form['universityId'].value ), cgi.escape(form['fees'].value ), cgi.escape(form['programLenght'].value ), cgi.escape(form['programDescription'].value ), cgi.escape(form['studyLang'].value ))
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
	c = conn.cursor()
	c.execute('''INSERT INTO university_program(ProgramName, ProgramType, UniversityID, TuitionFees, ProgramLength, ProgramDescription, StudyLanguage) VALUES(%s,%s,%s,%s,%s,%s,%s)''',data)
	conn.commit()
	print ("<script>")	
	print ("alert(\"Added succsessfully\");")
	print ("window.location = '../uniMenu.py';")
	print ("</script>")
except Exception as e:
	print(e)