#!/Users/shamel/PycharmProjects/try5/venv/Scripts/python  
# Demonstrates get method with an XHTML form.

import cgi
import mysql.connector


def printHeader(title):
    print("""Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?
<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.0 Strict//EN"
	"DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>
<body>""" % title)


def addUniversity():


printHeader("Using 'post' with forms")

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
        # print("<p>cookie: %s</p>"% cookie["session"].value)
        c.execute('SELECT * FROM members WHERE sessionID = %s ', (cookie["session"].value,))
        row = c.fetchon()
		
		
except Exception as e:
    print(e)
	
print ("</body></html>") 