
from flask_mail import Mail, Message
from flask import render_template





def send_message(data):
    from app import app
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'contact.mathsveda.mail@gmail.com'
    app.config['MAIL_PASSWORD'] = 'rypgvbfhglwucaik'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    html_message  = render_template('email_message.html', name = data["name"], email = data["email"], message = data["message"])

    
    msg = Message(subject = "Mail from Mathsveda", sender = 'contact.mathsveda.mail@gmail.com', recipients = ['ankitgupta.imp21@gmail.com', 'query.mathsveda@gmail.com'])
    msg.html = html_message
    mail.send(msg)
    print("sent successfully !")