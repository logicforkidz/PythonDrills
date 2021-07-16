**How to send and receive email in your gmail account account using Python**

***Table of Contents***
* Pre-requisite
* Setup 
* The structure of your Python Program

***Pre-requisite***
* Username and password of your Gmail account
* A cell phone that can receive text messages

***Setup***

* In order to access your Gmail via Python you will need to You will need to enable
**2-Step Verification** in your Google Account. You can access your google account from
https://myaccount.google.com. Once you login into your account, navigate to the **Security** 
option and turn on 2-Step Verification. 


* After that you will need to create a special password called **APP Password** in your Gmail. 
Follow the instructions at this link (https://support.google.com/accounts/answer/185839)
  to create the APP Password. Note down your app password and save it in a secure location. 
  Do not share your App password with anyone.

***The structure of your Python Program***

In Python you can ue the **SMTP** (Simple Mail Transfer Protocol) module to access your gmail. You can access the
documentation of this module at https://docs.python.org/3/library/smtplib.html

**Sendmail**

At a high level in order to send an email via Google, you have to follow the following steps:

*1. Create a SMTP instance and initialize it as below.*

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
output = smtp_object.ehlo()

*2. Connect to Google via a TLS session*

smtp_object.starttls()

*3. Ask user for the from email address, to-email address and app password.*

from_email = input("Enter from email address: ")
to_email = input ("Who do you want to send email to? ")
password = getpass("Enter your app password: ")

*4. Login into your gmail*

smtp_object.login(from_email, password)

*5. Ask the user for the subject of the email*

subject=input("Enter the subject of your email: ")

*6. Ask the user for the msg to send*

msg=input("Enter the message to send in email: ")

*7. Finally send the message. Note the subject and message have to be specially formatted.*
smtp_object.sendmail(from_email, to_email, "Subject:" + subject + "\r\n" + msg)