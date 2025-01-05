import mysql.connector as m

db = m.connect(host="localhost",user="root",password="",database="python")
cursor = db.cursor()

def printOnly():
    print("------CRUD THROUGH CLI------")
    print("/n WHAT DO YOU WANT TO PERFORM ?")
    print("1)Insert \n 2)Update \n 3)Delete \n 4)View Particular Data \n 5)View All \n 6)Exit")

def InsertFun(perName,perClass):
    sql = "INSERT INTO person(name,class) VALUES(%s,%s)"
    val = (perName,perClass)
    cursor.execute(sql,val)
    db.commit()
    if(cursor.rowcount>0):
        print(cursor.rowcount,"Record(s) Inserted")
    else:
        print("Something Went Wrong !!")

def DeleteFun(perName):
    sql = "DELETE FROM person WHERE name='{}'".format(perName)
    cursor.execute(sql)
    db.commit()
    if(cursor.rowcount>0):
        print(cursor.rowcount,"Record Deleted")
    else:
        print("Something Went Wrong !!")

def UpdateFun(perName,perClass):
    sql = "UPDATE person SET class='{}' WHERE name='{}'".format(perClass,perName)
    cursor.execute(sql)
    db.commit()
    if(cursor.rowcount>0):
        print(cursor.rowcount,"Record Updated")
    else:
        print("Something Went Wrong !!")

def ViewClassWiseFun(perClass):
    sql = "SELECT * FROM person WHERE class='{}'".format(perClass)
    cursor.execute(sql)
    results = cursor.fetchall()
    if(cursor.rowcount>0):
        print("Students of "+perClass+" are as follows :")
        for rows in results:
            print(rows)
    else:
        print("No Record Found in "+perClass+" !!")

def SelectAllFun():
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    results = cursor.fetchall()
    if(cursor.rowcount>0):
        for rows in results:
            print(rows)
    else:
        print("Something Went Wrong !!")
    
def Menu():
    printOnly()
    choice = int(input("Enter Your Choice: "))
    while True:
        if(choice == 1):
            perName = input("Enter Student's Name: ")
            perClass = input("Enter Student's Class: ")
            InsertFun(perName,perClass)
            choice = int(input("\n Enter Next Choice"))
        elif(choice == 2):
            perName = input("Enter Student's Name: ")
            perClass = input("Enter Student's Class To Be Updated: ")
            UpdateFun(perName,perClass)
            choice = int(input("\n Enter Next Choice"))
        elif(choice == 3):
            perName = input("Enter Student's Name: ")
            DeleteFun(perName)
            choice = int(input("\n Enter Next Choice"))
        elif(choice == 4):
            perClass = input("Enter Class To Search It's Student's: ")
            ViewClassWiseFun(perClass)
            choice = int(input("\n Enter Next Choice"))
        elif(choice == 5):
            SelectAllFun()
            choice = int(input("\n Enter Next Choice"))
        elif(choice == 6):
            print("Leaving The Program !")
            break
        else:
            print("Invalid Choice")
            choice = int(input("\n Enter Next Choice"))

Menu()            
