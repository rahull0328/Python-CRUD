import mysql.connector as m
db = m.connect(host="localhost",user="root",password="",database="python")
cursor=db.cursor()
sql="DELETE FROM crud where id = 1"
cursor.execute(sql)
db.commit()
print("data deleted")

