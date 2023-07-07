
from flask_mail import Mail, Message






def send_message(data):
    from app import app
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'ankitgupta.imp21@gmail.com'
    app.config['MAIL_PASSWORD'] = '9315689723'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    