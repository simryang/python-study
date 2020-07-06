# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.text import MIMEText

textfile = 'README.md'
me1 = 'simryang@hotmail.com'
me = 'simryangdanieldiary@gmail.com'
you = 'joseph@wiznet.io'
HOTMAIL = 'smtp.live.com'
GMAIL = 'smtp.gmail.com'

smtpsvr = GMAIL

smtp = smtplib.SMTP(smtpsvr, 587)
smtp.ehlo()     # say Hello
smtp.starttls() # TLS 사용시 필요
smtp.login(me, 'password')

msg = MIMEText('hi sr')
msg['Subject'] = 'test from python'
msg['To'] = you

print(me, you, msg.as_string())
smtp.sendmail(me, you, msg.as_string())

smtp.quit()
'''
# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 465)
s.send_message(msg)
s.quit()
'''