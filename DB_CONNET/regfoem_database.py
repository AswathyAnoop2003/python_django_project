#form validation
from tkinter import*
import re     #for validation of fields
from DB_CONNET.connection import *

root=Tk()                  #tkinter obj creation
frame=Frame(root)          # frame creation
frame.pack()
root.title("REGISTRATION FORM")  #title given
global entry1, entry2, entry3, entry4, entry5, entry6, fn, ln, pno, pw, mail
#label creation

label1=Label(frame,text="First Name:").grid(row=0,column=0)
label2=Label(frame,text="Last Name:").grid(row=1,column=0)
label3=Label(frame,text="Phone.No:").grid(row=2,column=0)
label4=Label(frame,text="mailId:").grid(row=3,column=0)
label5=Label(frame,text="Password:").grid(row=4,column=0)
label6=Label(frame,text="Retype Password:").grid(row=5,column=0)

#entry creation

entry1=Entry(frame)
entry1.grid(row=0,column=1)
entry2=Entry(frame)
entry2.grid(row=1,column=1)
entry3=Entry(frame)
entry3.grid(row=2,column=1)
entry4=Entry(frame)
entry4.grid(row=3,column=1)
# to hide password
entry5=Entry(frame,show='*')
entry5.grid(row=4,column=1)
entry6=Entry(frame,show='*')
entry6.grid(row=5,column=1)




def display():
    fn = entry1.get()
    ln = entry2.get()
    pno = entry3.get()
    mail = entry4.get()
    pw = entry5.get()
    assert all('a' <= letter <= 'z' or 'A' <= letter <= 'Z' for letter in fn)
    assert all('a' <= letter <= 'z' or 'A' <= letter <= 'Z' for letter in ln)
    x = '[6-9]{1}[0-9]{9}'
    matcher = re.fullmatch(x, pno)
    id = '[a-zA-Z0-9]*[@][a-z]*[.]com'
    matcher1 = re.fullmatch(id, mail)
    passw = '[a-zA-Z]*_[0-9]*'
    matcher2 = re.fullmatch(passw, pw)
    retype = entry6.get()
    matcher3 = re.fullmatch(pw, retype)

    if (matcher == None):
        print("Phone number is not valid")
    if (matcher1 == None):
        print("Email id is not valid")

    if (matcher2 == None):
        print("password is not valid")
    if(matcher3==None):
        print("passwords are not matching")
    # if(matcher!=None or matcher1!=None or matcher2!=None or matcher3!=None):
    #
    #     print("values entered are valid")

    print(entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + entry4.get() + " " +
          entry5.get() + " " + entry6.get())
def connectToDatabase():
    db = getconnection()
    print(db)
    cursor = db.cursor()
    fn = entry1.get()
    ln = entry2.get()
    pno = entry3.get()
    mail = entry4.get()
    pw = entry5.get()
    cursor.execute("DROP TABLE IF EXISTS FORM")
    sql1 = """create table FORM(first_name char(20),last_name char(20),phone char(10),email char(20),
                password char(20))"""

    sql2 = ("INSERT INTO FORM(FIRST_NAME,LAST_NAME,PHONE,EMAIL,PASSWORD)VALUES('%s','%s','%s','%s','%s')") % \
           (fn, ln, pno, mail, pw)
    try:
        cursor.execute(sql1)
        print("FORM Table is  created!!!")
        cursor.execute(sql2)
        print("Details are inserted successfully!!!!")
        db.commit()
        # db.close()

    except:

        db.rollback()
button1=Button(frame,text="DISPLAY",command=display)

button1.grid(row=7,column=1)
button2=Button(frame,text="SEND TO DB",command=connectToDatabase)

button2.grid(row=10,column=1)

frame.mainloop()
