import imaplib
import email
import getpass
# will use imap to map the mailbox
M = imaplib.IMAP4_SSL('imap.gmail.com')

my_email = "logicforkidz.student@gmail.com"
password = getpass.getpass("Enter your app password: ")

# login into your account
M.login(my_email, password)

# select the folder you want to operate on
M.select('"[Gmail]/All Mail"')

# search all emails with alert in subject, if typ is OK we will get a list of email-ids
typ, data = M.search(None, 'SUBJECT "alert"')

# iterate over the
if typ == 'OK':
    for email_id_list in data:
        # each email_id_list is a string of email-id numbers that we will need to fetch one at a time.
        for email_id in email_id_list.split():
            print ('email is ', email_id)
            #fetching the given email id
            result, email_data = M.fetch(email_id, '(RFC822)')
            # an email is a MIME formatted message which has multiple parts in it.
            # we will walk through all parts, decoding them but we will only print the text part of the email
            # there could be attachments, images etc in the email. We will igone them for now.
            # but you can save it to a file if you want.
            raw_email = email_data [0][1]
            raw_email_string = raw_email.decode("utf-8")
            email_msg = email.message_from_string(raw_email_string)
            for part in email_msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode = True)
                    print(body)


