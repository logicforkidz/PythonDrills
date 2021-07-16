import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

output = smtp_object.ehlo()
print (output)

output = smtp_object.starttls()
print (output)

from_email = "logicforkidz.student@gmail.com"
password = "auceousckcccnwda"

smtp_object.login(from_email, password)

to_address = "angoyal@gmail.com"
msg ="Subject: test email  \r\nThis is a test abcdefghijklmnopqrstuvqxyz1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smtp_object.sendmail(from_email, to_address, msg)