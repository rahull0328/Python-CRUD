import mysql.connector as m

db = m.connect(host="localhost",name="root",password="",database="python")
cursor=db.cursor()

name = input("ENTER NAME")
password = input("ENTER PASSWORD")

sql = "INSERT INTO CRUD(name,password) values('"+name+"','"+password+"')"
cursror.execute(sql)

print("DATA INSERTED")
