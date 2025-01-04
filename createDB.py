import mysql.connector as m

db = m.connect(host="localhost",user="root",password="")
cursor = db.cursor()

sql = "CREATE DATABASE PYTHON"
cursor.execute(sql)

print("DATABASE CREATED")
