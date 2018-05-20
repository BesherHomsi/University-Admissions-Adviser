#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import http.cookies as Cookie  
import random
import cgi
import os
import mysql.connector

def printHeader( title ):
   print ("""Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?
<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.0 Strict//EN"
	"DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>
<body>""" % title)


printHeader("Using 'post' with forms")
form = cgi.FieldStorage()

try:
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
		 
	c = conn.cursor()
	data = (cgi.escape(form['email'].value ), cgi.escape(form['password'].value ))
	c.execute('SELECT * FROM members WHERE email = %s and password= %s',data)
	row = c.fetchone()
	if row:
		cookie = Cookie.SimpleCookie()
		cookie["session"] = random.randint(1,1000000000)
		cookie["session"]["domain"] = "localhost"
		cookie["session"]["path"] = "/"
		data = (str(cookie["session"].value), cgi.escape(form['email'].value ), cgi.escape(form['password'].value ))
		c.execute("""UPDATE members SET sessionID = %s WHERE email= %s AND password=%s """, data)
		conn.commit()
		session_cookie = cookie.output().replace("Set-Cookie: ", "")
		print ("<script>")
		print ("document.cookie = '%s';" % session_cookie)
		print ("window.location = 'userMenu.py';")
		print ("</script>")
	else:
		print ("<script>")
		print ("alert(\"Incorrect user name or password\");")
		print ("window.location = '../login.html';")
		print ("</script>")
	conn.close()
except Exception as e:
	print(e)