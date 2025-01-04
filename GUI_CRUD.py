import mysql.connector as m
from tkinter import *
import io
from tkinter import messagebox

db = m.connect(host="localhost",user="root",password="",db="python")
cursor = db.cursor()

def insertFun():
    sql = "INSERT INTO person VALUES('{0}','{1}','{2}')".format(txt1.get(),txt2.get(),txt3.get())
    cursor.execute(sql)
    db.commit()
    if(cursor.rowcount > 0):
        messagebox.showinfo("SUCCESS","RECORD INSERTED")
        clearText()
    else:
        messagebox.showerror("ERROR","FAILED INSERTING RECORDS")
        clearText()

def deleteFun():
    sql = "DELETE FROM person WHERE id = "+txt1.get()
    cursor.execute(sql)
    db.commit()
    if(cursor.rowcount > 0):
        messagebox.showinfo("SUCCESS","RECORD DELETED")
        clearText()
    else:
        messagebox.showerror("ERROR","FAILED DELETING RECORDS")
        clearText()

def updateFun():
    sql = "UPDATE person SET name = '{0}',class = '{1}' WHERE id = '{2}'".format(txt2.get(),txt3.get(),txt1.get())
    cursor.execute(sql)
    db.commit()
    if(cursor.rowcount > 0):
        messagebox.showinfo("SUCCESS","RECORD UPDATED")
        clearText()
    else:
        messagebox.showerror("ERROR","FAILED MODIFYING RECORDS")
        clearText()

def viewFun():
    sql = "SELECT * FROM person WHERE id = "+txt1.get()
    cursor.execute(sql)
    results = cursor.fetchall()
    if(cursor.rowcount > 0):
        for rows in results:
            txt2.insert(0,rows[1])
            txt3.insert(0,rows[2])
    else:
        messagebox.showerror("ERROR","NO DATA FOUND")
        clearText()

def viewAllFun():
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    results = cursor.fetchall()
    buffer = io.StringIO()
    if(cursor.rowcount > 0):
        for rows in results:
            buffer.write("Id     : "+str(rows[0])+"\n")
            buffer.write("Name: "+str(rows[1])+"\n")
            buffer.write("Class: "+str(rows[2])+"\n")
            buffer.write("---------------------\n")
            messagebox.showinfo("Students: ",buffer.getvalue())
    else:
        messagebox.showerror("Error","No Such Record Found")
        clearText()

def clearText():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)

window = Tk()

lbl1 = Label(window,text = "CRUD OPERATIONS")
lbl2 = Label(window,text = "ID :- ")
txt1 = Entry(window)
lbl3 = Label(window,text = "Name :- ")
txt2 = Entry(window)
lbl4 = Label(window,text = "Class :- ")
txt3 = Entry(window)

add = Button(window,text = "ADD", command = insertFun)
remove = Button(window,text = "REMOVE", command = deleteFun)
modify = Button(window,text = "MODIFY", command = updateFun)
view = Button(window,text = "View", command = viewFun)
viewAll = Button(window,text = "View All", command = viewAllFun)

lbl1.grid(row = 0, column = 0, columnspan = 2)
lbl2.grid(row = 1, column = 0)
txt1.grid(row = 1, column = 1)
lbl3.grid(row = 2, column = 0)
txt2.grid(row = 2, column = 1)
lbl4.grid(row = 3, column = 0)
txt3.grid(row = 3, column = 1)
add.grid(row = 4, column = 0)
remove.grid(row = 4, column = 1)
modify.grid(row = 5, column = 0)
view.grid(row = 5, column = 1)
viewAll.grid(row = 6, column = 0, columnspan = 2)

window.mainloop()


