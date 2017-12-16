# https://www.tutorialspoint.com/python3/python_database_access.htm
import pymysql
# pymysql.install_as_MySQLdb()
import MySQLdb
db = MySQLdb.connect("localhost" , "root" , "venu", "users")
cursor = db.cursor()
qu = "select * from users"

try:
    cursor.execute(qu)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        print(fname, lname)
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()

# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)
# # disconnect from server
# db.close()
