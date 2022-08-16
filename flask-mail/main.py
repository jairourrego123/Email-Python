# importing libraries
from flask import Flask ,request
from flask_mail import Mail, Message

username= 'emailconfirmacionsalidasugc@gmail.com'
password= 'jbygynriouvgucxt'


   


app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['POST'])
def index():
  
  request_data = request.get_json()

  destinatario = request_data['destinatario']
  asunto= request_data['asunto']

  msg = Message(asunto, sender = username, recipients = [destinatario])
 
   
  if request_data['tipo_mensaje']=="html":

    
    print(request_data)
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':

    app.run(debug = True,port=5001)