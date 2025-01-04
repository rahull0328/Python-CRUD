import mysql.connector as m

db = m.connect(host="localhost",user="root",password="",database="python")
cursor = db.cursor()

sql = "CREATE TABLE crud (id int, name varchar(255), password varchar(255))"
cursor.execute(sql)

print("Table Created")
