#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python
# Demonstrates get method with an XHTML form.

import http.cookies as Cookie
import random
import cgi
import os
import mysql.connector


def printHeader():
    print("""Content-type: text/html

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
  </nav> """ % email)


def displayApplicatoins(name, id, applications, sholarships):
    print("""
	<div class="container">
        <div class="row">
			<h2>%s</h2>
		</div>
	</div>
	<div class="container">
        <div class="row">
            <div class="col-sm-6 col-sm-offset-3 col-xs-12">
                <form name="addprogram" action="addDocumentsForm.py" method="POST"> 
                    <hr />
                    <div class="row">
                        <div class="col-xs-12 col-sm-6 col-md-6">
                            <div class="form-group">  
                                <select class="form-control" name ="startDate" id="startDate">""" % name)
    for i in applications:
        print("""<option value=%s>%s</option>""" % (i[0], i[0]))
    print("""
								</select>
                            </div>
                        </div>
                        <div class="col-xs-12 col-sm-6 col-md-6">
                            <div class="form-group">  
                                <select class="form-control" name ="programName" id="programName">""")
    for i in application:
            print("""<option value=%s>%s</option>""" % (i[2], i[2]))
    print("""
								</select>
                            </div>
                        </div>
                        <div class="col-xs-12 col-sm-6 col-md-6">
                            <div class="form-group">  
                                <select class="form-control" name ="programType" id="programType">""")
    for i in application:
        print("""<option value=%s>%s</option>""" % (i[3], i[3]))
    print("""</select>
                            </div>
                        </div>
                    </div> 
                    <div class="row">
                        <div class="col-xs-12 col-sm-6 col-md-6">
                            <div class="form-group">  
                                <select class="form-control" name ="scholarshipName" id="scholarshipName">""")
    for i in scholarships:
        print("""<option value=%s>%s</option>""" % (i[0], i[0]))
    print("""
                    <hr />
					<input type="text" name="universityId" id="universityId" class="form-control" value=%s placeholder="universityId" style="visibility: hidden;">
                    <div class="row">
                        <div class="col-xs-12"><input type="submit" value="Add Document" class="btn btn-primary btn-block btn-lg">
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>	""" % id)


printHeader()

try:
    query = os.environ['QUERY_STRING']
    if len(query) == 0:
        print("no suggestion")
    else:
        pairs = cgi.parse_qs(query)
        if "q" in pairs.keys():
            q = pairs["q"][0]
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='uaa')
    c = conn.cursor()
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        # print("<p>cookie: %s</p>"% cookie["session"].value)
        c.execute('SELECT * FROM members WHERE sessionID = %s ', (cookie["session"].value,))
        row = c.fetchone()
        if row:
            c.execute('''SELECT * FROM university WHERE UniversityID = %s''' % (q,))
            uni = c.fetchone()
            c.execute('''SELECT * FROM program_application WHERE ProgramApplicationID = %s''' % (q,))
            application = c.fetchall()
            c.execute('''SELECT * FROM tuition_fee_scholarship WHERE offeredat = %s''' % (q,))
        scholarships = c.fetchall()

        navBar(row[5])
        if application:
            displayApplicatoins(uni[1], q, application, scholarships)
except Exception as e:
    print(e)