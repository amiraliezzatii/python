import smtplib 
from tkinter import END, Button, StringVar, mainloop
from turtle import width
from tkinter import *
from setuptools import Command
def send_message():
    addres_info = addres.get()
    email_body_info = email_body.get()
    print(addres_info , email_body_info)
    sender_email = "exmple@gmail.com"
    sender_password = "exmplepassword"
    server=smtplib.SMTP(smtp@gmail.com , 587 )
    server.starttls()
    server.login(sender_email , sender_password)
    print("login successful")
    server.sendmail(sender_email ,addres_info, email_body_info)
    print("message sent")
    addres_entry.delete(0 ,END)
    app = tk()
    app.geometry =("500x500")
    app.title("python mail send app")
    heading = label(text="python email sending app " ,bg="yellow",fg="black",font="10",width="500",height="3")
    heading.pack()
    addres_field =label(text="Recipient addres:")
    email_body_filed =label(text="message ")
    addres_field.place(x=15 ,y=140)
    addres = StringVar()
    email_body = StringVar()
    email_entry = entry(textvariable=addres,width="30")
    email_body_entry = entry(textvariable=email_body,width="30")
    addres_entry.place(x=15,y=100)
    email_body.place(x=15,y=180)
    Button = Button(app,text="Send message " , Command=send_message,width="30",height="2",bg="gresy")
    Button.place(x=15,y=220)
    mainloop()