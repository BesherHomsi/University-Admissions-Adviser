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

try:
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
	c = conn.cursor()
	if "HTTP_COOKIE" in os.environ:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		c.execute('SELECT * FROM members WHERE sessionID = %s ',(cookie["session"].value,))
		row = c.fetchone()
		if row:
			data = ("0",row[5],row[1])
			c.execute("""UPDATE members SET sessionID = %s WHERE email= %s AND password=%s """,data)
			cookie["session"] = 0
			conn.commit()
		print ("<script>")
		print ("window.location = '../index.html';")
		print ("</script>")		
except Exception as e:
	print(e)
	
	
print ("</body></html>") 
