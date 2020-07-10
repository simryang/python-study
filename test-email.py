# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.text import MIMEText

textfile = 'README.md'
me = 'kodico.wiznet2020@gmail.com'
you = 'joseph@wiznet.io'
HOTMAIL = 'smtp.live.com'
GMAIL = 'smtp.gmail.com'

smtpsvr = GMAIL

print('email: Connecting server...')
with smtplib.SMTP(smtpsvr, 587) as smtp:
    try:
        smtplib.SMTP()
        print(f'\tSay hello to {smtpsvr}')
        smtp.ehlo()     # say Hello
        print(f'\tStarting TLS...')
        smtp.starttls() # TLS 사용시 필요
        print('\tTries to log in...')
        smtp.login(me, '0vud0v1!')
    except smtplib.SMTPException as e:
        print (f"Error: unable to connect to email server {smtpsvr}:{e}")
        pass
    except Exception:
        print(f"Unknown error: {e}")
    print ('\tCreating email content...')
    msg = MIMEText('안녕하세요 sr 입니다. 파이썬 모듈에서 메일을 보내봅니다.'.encode('utf-8'), _charset='UTF-8')
    msg['Subject'] = 'test from python with Hangul'
    msg['To'] = you
    try:
        smtp.sendmail(me, you, msg.as_string())
    except smtplib.SMTPException as e:
        print(f"Error: failed to send message {msg.as_string()} to {smtpsvr}")
    print ('\tSending email is done!')
    smtp.quit()