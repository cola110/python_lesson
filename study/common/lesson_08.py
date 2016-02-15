import os
print "Content-type:text/html\r\n\r\n"

print os.environ


import MySQLdb

db = MySQLdb.connect("localhost", "root", "cola", "testdb")
cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print data

db.close()
