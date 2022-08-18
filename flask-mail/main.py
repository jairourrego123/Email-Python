# importing libraries
from tkinter.ttk import Style
from flask import Flask ,request
from flask_mail import Mail, Message

username= 'emailconfirmacionsalidasugc@gmail.com'
password= 'jbygynriouvgucxt'


   
def tabla() :

  return  """<div style="text-align:center;"> <table class="default" style=" width:100%;">  <tr  style="border: 1px solid black; width:100%; " >"""

def columnas(columnas,estilo):
  atributos = "<tr>"
  for iterator in columnas :

    atributos = atributos + f""" <th style="{estilo}" scope="row">{iterator}</th>"""
      
  atributos=atributos + "</tr>"
  return atributos


def registros(columnas,filas,estilo,):
  registro="<tr>"
  registro = registro +f"""<th style="{estilo['indice']}" >{filas[0]}</th>"""
  for iterator in range(len(columnas)-1) :

    registro = registro + f""" <td style="{estilo['total']}" >{filas[iterator + 1]}</td>"""

  registro= registro + "</tr>"    
  return registro

def firma(datos,estilo):

  pie = f"""<i style="{estilo}">"""
  for iterator in range(len(datos)) :

    pie = pie + f"""{datos[iterator]} <br>"""

  pie= pie + f"""</i>"""    
  return pie


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
  try : 
    request_data = request.get_json()

    destinatario = request_data['destinatario']
    asunto= request_data['asunto']

    msg = Message(asunto, sender = username, recipients = [destinatario])
  
    
    if request_data['tipo_mensaje']=="html":


      msg.html = f"""
      <html>
      <body>
      """
      msg.html = msg.html + request_data['mensaje']['saludo']+"<br><br>"+request_data['mensaje']['encabezado'] + "<br><br>"

      if request_data['mensaje']['cuerpo']['tabla']:
        
        atributos= request_data['mensaje']['cuerpo']['tabla']['columnas']['columnas']
        estilo_columnas =request_data['mensaje']['cuerpo']['tabla']['columnas']['style']
        filas= request_data['mensaje']['cuerpo']['tabla']['filas']['filas']
        estilo_filas =request_data['mensaje']['cuerpo']['tabla']['filas']['style']
        pie=request_data['mensaje']['firma']['firma']
        estilo_pie=request_data['mensaje']['firma']['style']
        despedida=request_data['mensaje']['despedida']
          
        msg.html = msg.html + tabla() + columnas(atributos,estilo_columnas)
        

        
        for iterator in range(len(filas)):

          msg.html = msg.html + registros(atributos,filas[iterator],estilo_filas)
    
        msg.html=msg.html + "</table> </div> <br><br>  " 
        msg.html = msg.html + despedida + "<br> <br>" + "Este es un correo electrónico generado <b> automáticamente </b> por favor no responder. <br><br><br>"

        msg.html=msg.html + firma(pie,estilo_pie)
    else :

      msg.body = request_data['mensaje']

    mail.send(msg)
    return "Sent"
  
  except :
     return "fallo"

if __name__ == '__main__':

    app.run(debug = True,port=5001)