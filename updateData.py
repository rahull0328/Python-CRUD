import mysql.connector as m

db = m.connect(host="localhost",user="root",password="",database="python")
cursor = db.cursor()

sql = "UPDATE crud SET password = '123abc' WHERE id= 1 "
cursor.execute(sql)
db.commit()

print("DATA UPDATED")
