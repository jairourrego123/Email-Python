# importing libraries
from flask import Flask
from flask_mail import Mail, Message

username= 'emailconfirmacionsalidasugc@gmail.com'
password= 'jbygynriouvgucxt'
destinatario= 'jairourrego123@gmail.com'
asunto = 'Salida N00004'
   
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
mail.init_app(app)
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")

def index():
   
   msg = Message(
                'Hello',
                sender =username,
                recipients = destinatario
               )
   msg.body = 'Hello Flask message sent from Flask-Mail'
   mail.send(msg)
   return 'Sent'
   
if __name__ == '__main__':
   app.run(debug = True)