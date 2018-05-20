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


printHeader()
form = cgi.FieldStorage()


try:
	data = (cgi.escape(form['OptionalFlag'].value ) ,cgi.escape(form['DocumentName'].value ), cgi.escape(form['ExaminationScale'].value ), cgi.escape(form['scholarshipName'].value ), cgi.escape(form['startDate'].value ), cgi.escape(form['universityId'].value ), cgi.escape(form['programName'].value ), cgi.escape(form['programType'].value ))
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
	c = conn.cursor()
	c.execute('''INSERT INTO document_requirement(OptionalFlag, DocumentName, ExaminationScale, RequiredByScholarship, ApplicaitonStartDate, ProgramApplicationID, ProgramApplicationName, ProgramApplicationType) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',data)
	conn.commit()
	print ("<script>")	
	print ("alert(\"Added succsessfully\");")
	print ("window.location = '../uniMenu.py';")
	print ("</script>")
except Exception as e:
	print(e)