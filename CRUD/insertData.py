import mysql.connector as m

db = m.connect(host="localhost",user="root",password="",database="python")
cursor = db.cursor()

sql = "INSERT INTO crud VALUES(2,'abc','abc123456')"
cursor.execute(sql)
db.commit()

print("DATA INSERTED")
