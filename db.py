#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="shubham123",
    db="MYGIG")

cursor = db.cursor()

name = raw_input()
passw = raw_input()

query = "SELECT *FROM `db_user`;"

cursor.execute(query.format(name))

row = cursor.fetchone()
print row[0] , row[1]