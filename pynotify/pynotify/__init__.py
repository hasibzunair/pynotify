import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# How did you get in?
# Look behind you!

# Initialize sender credentials
source = "neuralert1994@gmail.com"
password = "neuralert1994HZ"


def send_email(destinaiton, subject=" ", msg=" "):
    '''
    Arguements:
        destination: Takes in destionation email of type string
        subject(optional arguement): Takes in a string as an input (default arg: None)
        msg(optional arguement): Takes in a message of type string as input (default arg: None)
        destination: Takes in destionation email of type string
    '''
    try:     
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(source, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(source, destinaiton, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")



def send_email_with_attachment(destination, files, sub="Subject", text= "No text"):
    '''
    Arguements:
        destination: Takes in destionation email of type string
        files: Take in a list of strings as input
        sub(optional arguement): Takes in a string as an input (default arg empty)
        text(optional arguement): Takes in a message of type string as input (default arg empty)
    '''

    dest = destination
    msg = MIMEMultipart()

    msg['From'] = source
    msg['To'] = dest
    msg['Subject'] = sub

    body = text

    msg.attach(MIMEText(body, 'plain'))

    for f in files:
        attachment = open(f, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % f)
        msg.attach(part)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(source, password)
        text = msg.as_string()

        server.sendmail(source, dest, text)
        server.quit()
        print("Email with attachments sent!")
    except:
        print("Failed! :(")
