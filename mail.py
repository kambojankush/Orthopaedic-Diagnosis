import smtplib
from configparser import ConfigParser
from email.mime.text import MIMEText

def sendmail(to, message):
    config = ConfigParser()
    config.read('credentials.ini')

    gmail_user = config.get('email', 'username')
    gmail_password = config.get('email', 'pwd')
    sent_from = gmail_user

    try:
        msg = MIMEText(message)
        msg['Subject'] = 'Medical Report for Vertebral Column Test'
        msg['From'] = gmail_user
        msg['To'] = to

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()

        print('Email sent!')
    except:
        print('Unable to process mail...')
