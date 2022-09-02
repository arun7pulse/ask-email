from email.message import EmailMessage
from secret import password
import ssl
import smtplib

email_sender = "arun7pulse@gmail.com"
email_password = password

email_receiver = 'arun7pulse@icloud.com'
email_subject = "This is test email from ask-email"
email_body = """
this is body from the test email ask-email project. 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

#temp-mail.org