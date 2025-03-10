import tkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox
# from tkinter import PhotoImage
from addbook import *
from deletebook import *
from Viewbook import *
from Issubook import *
from Returnbook import *


#Add your own database name and password here to reflect in the code
# mypass = "root"
mydatabase = "db"

con = mysql.connector.connect(host="localhost", user="root",  database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("700x600")


# Take n greater than 0.25 and less than 5







headingFrame1 = Frame(root, bg="#FFBB00", bd=10)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n LNCTU Library", bg="blue", fg='white',
                     font=('ArialBold', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
