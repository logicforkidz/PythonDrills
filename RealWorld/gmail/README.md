**How to send and receive email in your gmail account using Python**

***Table of Contents***
* What is in an email
* Pre-requisite
* Setup 
* Sending Email
* Receiving Email 

***What is in an email***

An email is very much like the snail mail that you send in a paper envelop. The difference is that all the parts are 
digitially encoded and appened to each other in the MIME format so that the email can be securely sent to recepient 
with all its parts intact. You can read about MIME atg https://docs.oracle.com/cd/E19957-01/816-6028-10/asd3j.htm



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

***Sendmail***

In Python you can ue the **SMTP** (Simple Mail Transfer Protocol) module to send email. You can access the
documentation of this module at https://docs.python.org/3/library/smtplib.html

At a high level in order to send an email via Google, you have to follow the following steps:

*1. Create a SMTP instance and initialize it as below.*

    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    output = smtp_object.ehlo()

*2. Connect to Google via a TLS session*

    smtp_object.starttls()

*3. Ask user for the from email address, to-email address and app password.*

    from_email = input("Enter from email address: ")
    to_email = input ("Who do you want to send email to? ")
    password = getpass.getpass("Enter your app password: ")

*4. Login into your gmail*

    smtp_object.login(from_email, password)

*5. Ask the user for the subject of the email*

    subject=input("Enter the subject of your email: ")

*6. Ask the user for the msg to send*

    msg=input("Enter the message to send in email: ")

*7. Finally send the message. Note the subject and message have to be specially formatted.*
    smtp_object.sendmail(from_email, to_email, "Subject:" + subject + "\r\n" + msg)

***Receiving mail***

We use IMAP protocol to fetch email from your gmail account. You can access documentation of this module at 
https://docs.python.org/3/library/imaplib.html

At a high level in order to receive an email via Google, you have to follow the following steps:

*1. Create an instance of imap and point it to google's imap server*

    M = imaplib.IMAP4_SSL('imap.gmail.com')

*2. ask the user for their login credentials.*

    my_email = input ("Enter your email address: ")
    password = getpass.getpass("Enter your app password: ")

*3. login into your account*

    M.login(my_email, password)

*4. select the folder you want to operate on*

    M.select('"[Gmail]/All Mail"')

*5. search all emails according to the criteria you want. There are many search commands. You can see the whole list at
https://www.atmail.com/blog/imap-commands/*
   
    typ, data = M.search(None, 'SUBJECT "alert"')

*6. In step 5 you will get all the email ids that match your search criteria. Convert it into a list of email ids*

    for l in data:
      email_id_list.append(l.split())

*7. Finally fetch each email, decode it and see the text part of the email*  


    for email_id in email_id_list:  
        result, email_data = M.fetch(email_id, '(RFC822)')
        raw_email = email_data [0][1]
        raw_email_string = raw_email.decode("utf-8")
        email_msg = email.message_from_string(raw_email_string)
        for part in email_msg.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode = True)
                print(body)

