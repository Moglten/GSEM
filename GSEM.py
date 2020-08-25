import tkinter as tk
from tkinter import *

import smtplib
import webbrowser


def SendEmail():
    try:
        sender = Sender.get()
        password = Password.get()
        receiver = Receiver.get()
        massage = MassageContent.get( '1.0', 'end' )

        #create a SMTP session using 587 port for Gmail
        s = smtplib.SMTP( 'smtp.gmail.com', 587 )
        # start TLS for security
        s.starttls()
        # Authentication
        s.login( sender, password)
        # message to be sent
        message = massage
        # sending the mail
        s.sendmail( sender, receiver, message )
        # terminating the session
        s.quit()

        tk.Label( MainWindow, text="Email sent successfully" ).grid( column=2, row=9 )

    except EXCEPTION as e:
        tk.Label( MainWindow, text=str( e ) ).grid( column=2, row=9 )


def ActivationAPPAccess(click):
    webbrowser.open_new( r"https://www.google.com/settings/security/lesssecureapps" )




# UI for program
MainWindow = tk.Tk()

# Program Name
MainWindow.title( "Email via Gmail" )

# Program Dimentions
MainWindow.geometry( "600x450" )

Sender = StringVar()
Password = StringVar()
Receiver = StringVar()
Subject = StringVar()
MassageContent = StringVar()


# Less access app Activaition Label
a = Label( MainWindow, text="To use this app turn this setting ON for your account", fg="blue", cursor="hand2" )
a.grid(  column=2, row=0)
a.bind( "<Button-1>", ActivationAPPAccess )

# ---------------Labels-----------------
SenderText = tk.Label( text="Gmail Account" )
SenderText.grid( column=0, row=1 )

PasswordText = tk.Label( text="Gmail Password" )
PasswordText.grid( column=0, row=2 )

RecieverText = tk.Label( text="recepient" )
RecieverText.grid( column=0, row=3 )

SubjectText = tk.Label( text="Subject" )
SubjectText.grid( column=0, row=4 )

RecieverText = tk.Label( text="Massage Content" )
RecieverText.grid( column=2, row=5 )

# ---------------Entrys-----------------
SenderEntry = tk.Entry( width=45 , textvariable=Sender)
SenderEntry.grid( column=2, row=1 )

senderentryPassword = tk.Entry( width=45 ,show="*" , textvariable=Password)
senderentryPassword.grid( column=2, row=2 )

RecieverEntry = tk.Entry( width=45  , textvariable=Receiver)
RecieverEntry.grid( column=2, row=3 )

SubjectEntry = tk.Entry( width=45  , textvariable=Subject)
SubjectEntry.grid( column=2, row=4 )

# ---------------texts------------------

MassageContent = tk.Text(  height=15, width=50)
MassageContent.grid( column=2, row=6 )

# ----------------Button----------------

SendButton = tk.Button( text="Send Email!", height=2, width=10, command=SendEmail )
SendButton.grid( column=2, row=7 )

MainWindow.mainloop()
