
from flask_mail import Mail, Message
from flask import render_template
import os



def send_message(data):

    try:
        from app import app
        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = os.environ.get('USER_NAME')
        app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True

        sender = os.environ.get('USER_NAME')
        reciever1 = os.environ.get('REC_MAIL_1')
        reciever2 = os.environ.get('REC_MAIL_2')

        mail = Mail(app)

        html_message  = render_template('email_message.html', name = data["name"], email = data["email"], message = data["message"])

    
        msg = Message(subject = "Mail from Mathsveda", sender = sender, recipients = [reciever1, reciever2])
        msg.html = html_message
        mail.send(msg)
        print("sent successfully !")
        return 1
    
    except Exception as e:
        print(e)
        return -1