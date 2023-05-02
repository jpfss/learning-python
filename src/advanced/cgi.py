# -*- coding: utf-8 -*-

# =============================================================================
# First CGI Program
# =============================================================================
# Import modules for CGI handling
from os import environ
import cgitb
import cgi
import os
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! This is my first CGI program</h2>')
print('</body>')
print('</html>')
# =============================================================================
# CGI Environment Variables
# =============================================================================

print("Content-type: text/html\r\n\r\n")
print("<font size=+1>Environment</font><\br>")
for param in os.environ.keys():
    print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))
# =============================================================================
# Simple URL Example:Get Method
# =============================================================================


# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")
# =============================================================================
# Passing Information Using POST Method
# =============================================================================
# =============================================================================
# <form action = "/cgi-bin/hello_get.py" method = "post" >
# First Name: < input type = "text" name = "first_name" > <br / >
# Last Name: < input type = "text" name = "last_name" / >
#
# <input type = "submit" value = "Submit" / >
# </form >
# =============================================================================
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")
# =============================================================================
# Passing Checkbox Data to CGI Program
# =============================================================================
# =============================================================================
# <form action = "/cgi-bin/checkbox.cgi" method = "POST" target = "_blank" >
# <input type = "checkbox" name = "maths" value = "on" / > Maths
# <input type = "checkbox" name = "physics" value = "on" / > Physics
# <input type = "submit" value = "Select Subject" / >
# </form >
# =============================================================================
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('maths'):
    math_flag = "ON"
else:
    math_flag = "OFF"

if form.getvalue('physics'):
    physics_flag = "ON"
else:
    physics_flag = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> CheckBox Maths is : %s</h2>" % math_flag)
print("<h2> CheckBox Physics is : %s</h2>" % physics_flag)
print("</body>")
print("</html>")
# =============================================================================
# Passing Radio Button Data to CGI Program
# =============================================================================
# =============================================================================
# <form action = "/cgi-bin/radiobutton.py" method = "post" target = "_blank" >
# <input type = "radio" name = "subject" value = "maths" / > Maths
# <input type = "radio" name = "subject" value = "physics" / > Physics
# <input type = "submit" value = "Select Subject" / >
# </form >
# =============================================================================
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('subject'):
    subject = form.getvalue('subject')
else:
    subject = "Not set"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Radio - Fourth CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> Selected Subject is %s</h2>" % subject)
print("</body>")
print("</html>")
# =============================================================================
# Passing Text Area Data to CGI Program
# =============================================================================
# =============================================================================
# <form action = "/cgi-bin/textarea.py" method = "post" target = "_blank">
#    <textarea name = "textcontent" cols = "40" rows = "4">
#       Type your text here...
#    </textarea>
#    <input type = "submit" value = "Submit" />
# </form>
# =============================================================================
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Text Area - Fifth CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> Entered Text Content is %s</h2>" % text_content)
print("</body>")
# =============================================================================
# Passing Drop Down Box Data to CGI Program
# =============================================================================
# =============================================================================
# <form action = "/cgi-bin/dropdown.py" method = "post" target = "_blank">
#    <select name = "dropdown">
#       <option value = "Maths" selected>Maths</option>
#       <option value = "Physics">Physics</option>
#    </select>
#    <input type = "submit" value = "Submit"/>
# </form>
# =============================================================================
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('dropdown'):
    subject = form.getvalue('dropdown')
else:
    subject = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Dropdown Box - Sixth CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> Selected Subject is %s</h2>" % subject)
print("</body>")
print("</html>")
# =============================================================================
# Setting up Cookies
# =============================================================================
print("Set-Cookie:UserID = XYZ;\r\n")
print("Set-Cookie:Password = XYZ123;\r\n")
print("Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n")
print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
print("Set-Cookie:Path = /perl;\n")
print("Content-type:text/html\r\n\r\n")
# =============================================================================
# Retrieving Cookies
# =============================================================================
# Import modules for CGI handling

if environ.has_key('HTTP_COOKIE'):
    for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
        (key, value) = split(cookie, '=')
        if key == "UserID":
            user_id = value

        if key == "Password":
            password = value

print("User ID  = %s" % user_id)
print("Password = %s" % password)
# =============================================================================
# File Upload Example
# =============================================================================
# =============================================================================
# <html>
#    <body>
#       <form enctype = "multipart/form-data" action = "save_file.py" method = "post">
#       <p>File: <input type = "file" name = "filename" /></p>
#       <p><input type = "submit" value = "Upload" /></p>
#       </form>
#    </body>
# </html>
# =============================================================================
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print("""\
Content-Type: text/html\n
<html>
   <body>
      <p>%s</p>
   </body>
</html>
""" % (message,))
# =============================================================================
# How To Raise a "File Download" Dialog Box?
# =============================================================================
# HTTP Header
print "Content-Type:application/octet-stream; name = \"FileName\"\r\n"
print "Content-Disposition: attachment; filename = \"FileName\"\r\n\n"

# Actual File Content will go here.
fo = open("foo.txt", "rb")

str = fo.read()
print str

# Close opend file
fo.close()
