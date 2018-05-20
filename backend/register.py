#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import cgi
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
	data = (cgi.escape(form['password'].value ), cgi.escape(form['first_name'].value ), cgi.escape(form['last_name'].value ), cgi.escape(form['institution_name'].value ), cgi.escape(form['email'].value ), 0, cgi.escape(form['memberType'].value ))
	c.execute('''INSERT INTO members(password, FirstName, LastName, InstitutionName, email, sessionID, memberType) VALUES(%s,%s,%s,%s,%s,%s,%s)''',data)
	conn.commit()
	conn.close()	
	print ("<script>")
	print ("window.location = '../index.html';")
	print ("alert(\"Registered successfully\");")
	print ("</script>")
except Exception as e:
	print ("<script>")
	print ("alert(\"%s\");"% e)
	print ("window.location = '../register.html';")
	print ("</script>")


	
print ("</body></html>") 
