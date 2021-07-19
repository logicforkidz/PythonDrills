import smtplib
import getpass

# we use smtp to connect to gmail, so create an instance
# this instance connects to smtp.gmail.com server at port 587.
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

# send an initial handshake.
output = smtp_object.ehlo()
print (output)

# start a secure connection
output = smtp_object.starttls()
print (output)

# these are our login password.
# you should not store them in the email.
from_email = "logicforkidz.student@gmail.com"
password = getpass.getpass("Enter your app password: ")

smtp_object.login(from_email, password)

to_address = input("Who do you want to send email to?")
subject = input("Enter subject: ")
text = input ("Enter message to send: ")
msg ="Subject: " + subject + "\r\n" + text
smtp_object.sendmail(from_email, to_address, msg)