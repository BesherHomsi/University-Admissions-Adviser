#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python
# Demonstrates get method with an XHTML form.

import mysql.connector
import http.cookies as Cookie
import random
import cgi
import os


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
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='uaa')
    c = conn.cursor()
    if "HTTP_COOKIE" in os.environ:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        #print("<p>cookie: %s</p>"% cookie["session"].value)
        c.execute('SELECT * FROM members WHERE sessionID = %s ', (cookie["session"].value,))
        row = c.fetchone()
        if row:
            c.execute("""INSERT INTO member_telephones(MemberIDTelephone, ContactTelephone) VALUES(%s,%s) """,(cgi.escape(form['uId'].value), cgi.escape(form['tel'].value)))
            c.execute("""SELECT * FROM university_officials WHERE universityOfficialsID=%s""",(cgi.escape(form['uId'].value),))
            std = c.fetchone()
            if std:
                c.execute("""UPDATE university_officials SET Employedat = %s WHERE universityOfficialsID= %s""", (cgi.escape(form['uniName'].value), cgi.escape(form['uId'].value)))
            else:
                c.execute("""INSERT INTO university_officials(universityOfficialsID, Employedat) VALUES(%s,%s) """,(cgi.escape(form['uId'].value), cgi.escape(form['uniName'].value)))
            conn.commit()
            print ("<script>")
            print ("alert(\"the account has been updated\");")
            print ("window.location = 'userMenu.py';")
            print ("</script>")
        else:
            print ("<script>")
            print ("alert(\"An error occurred and could not update the info. !!\");")
            print ("window.location = '../login.html';")
            print ("</script>")
except Exception as e:
    print(e)

print("</body></html>")
