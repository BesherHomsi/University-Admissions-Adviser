#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import http.cookies as Cookie  
import random
import cgi
import os
import mysql.connector

def printHeader( ):
   print ("""Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?
<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.0 Strict//EN"
	"DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>Uaa</title></head>
<body>""")


printHeader()
form = cgi.FieldStorage()


try:

	data = (cgi.escape(form['uniName'].value ), cgi.escape(form['uniCity'].value ), cgi.escape(form['uniCountry'].value ), cgi.escape(form['uniAddress'].value ), cgi.escape(form['uniWebsite'].value ), cgi.escape(form['uniRanking'].value ))
	conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='uaa')
	c = conn.cursor()
	c.execute('''INSERT INTO university(UniversityName, City, Country, Address, UniversityWebsite, UniversityRanking) VALUES(%s,%s,%s,%s,%s,%s)''',data)
	conn.commit()
	print ("<script>")
	print ("alert(\"Added succsessfully\");")
	print ("window.location = 'uniMenu.py';")
	print ("</script>")
except Exception as e:
	print(e)