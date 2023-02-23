# importing libraries

from os import remove
from flask import Flask, request,Response
from flask_mail import Mail, Message
from flask_mail import *
from werkzeug.utils import secure_filename

import os
import mimetypes
import smtplib

import os
username= os.getenv("EMAIL_USER","no_contestar@ugc.edu.co")
password = os.getenv("EMAIL_PASS", 'zhuzsxaohjpeguix')


def tabla():

    return """<div style="text-align:center;"> <table class="default" style=" width:100%;">  <tr  style="border: 1px solid black; width:100%; " >"""


def columnas(columnas, estilo):
    atributos = "<tr>"
    for iterator in columnas:

        atributos = atributos + \
            f""" <th style="{estilo}" scope="row">{iterator}</th>"""

    atributos = atributos + "</tr>"
    return atributos


def registros(columnas, filas, estilo,):
    registro = "<tr>"
    registro = registro + \
        f"""<th style="{estilo['indice']}" >{filas[0]}</th>"""
    for iterator in range(len(columnas)-1):

        registro = registro + \
            f""" <td style="{estilo['total']}" >{filas[iterator + 1]}</td>"""

    registro = registro + "</tr>"
    return registro


def firma(datos, estilo="color:#b2aaaa;"):

    pie = f"""<i style="{estilo}">"""
    for iterator in range(len(datos)):

        pie = pie + f"""{datos[iterator]} <br>"""

    pie = pie + f"""</i>"""
    return pie




app = Flask(__name__)
app.config['UPLOAD_FOLDER']="./public/adjuntos"
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route('/', methods=['POST'])
def index():
  try:
   
      request_data = request.get_json()
    
      destinatario = request_data['destinatario']
      asunto = request_data['asunto']
      pie = ["Centro de Conciliación José Ignacio Talero Losada de la Universidad La Gran Colombia","Tel. (57)3276999 Ext 2606 / 2602","Cel. 3212179704 ","Calle 12 No 8-37/50 ", "<u>ccjoseignaciotalerolosada@ugc.edu.co </u>"]
      msg = Message(asunto, sender=(
          request_data['nombre_servicio'], username), recipients=destinatario)

      
      if request_data['tipo_mensaje'] == "html":

        try: 

          msg.html = f"""
                        <html>
                        <body>
                        """
          msg.html = msg.html + request_data['mensaje']['saludo'] + \
              "<br><br>"+request_data['mensaje']['encabezado'] + "<br>"
          
          if 'tabla' in request_data['mensaje']['cuerpo']: # si existe el atributo tabla 


          # if request_data['mensaje']['cuerpo']['tabla']:

              atributos = request_data['mensaje']['cuerpo']['tabla']['columnas']['columnas']
              estilo_columnas = request_data['mensaje']['cuerpo']['tabla']['columnas']['style']
              filas = request_data['mensaje']['cuerpo']['tabla']['filas']['filas']
              estilo_filas = request_data['mensaje']['cuerpo']['tabla']['filas']['style']

              msg.html = msg.html + tabla() + columnas(atributos, estilo_columnas)

              for iterator in range(len(filas)):

                  msg.html = msg.html + \
                      registros(atributos, filas[iterator], estilo_filas)

              msg.html = msg.html + "</table> </div> <br><br>  "


          msg.html = msg.html + request_data['mensaje']['cuerpo'] +"<br><br>"
          despedida = request_data['mensaje']['despedida']
          if 'firma'  in request_data['mensaje']:
        
               estilo_pie = request_data['mensaje']['firma']['style']
               pie = request_data['mensaje']['firma']['firma']
               msg.html = msg.html + firma(pie,estilo_pie)
             
         
          
      

          msg.html = msg.html + despedida + "<br> <br>" + \
              "Este es un correo electrónico generado <b> automáticamente </b> por favor no responder. <br><br><br>"

          msg.html = msg.html + firma(pie)
        
        except :
          
          return "Ocurrio un error al la informacion del cuerpo "

      else:
          
          msg.body = request_data['mensaje']                                        

      if 'adjunto'  in request_data:
      
        with app.open_resource(os.getcwd()+"/public/adjuntos/"+request_data["adjunto"]) as fp:  
          mime = mimetypes.guess_type(os.getcwd()+"/public/adjuntos/"+request_data["adjunto"])
          msg.attach(request_data["adjunto"].capitalize(), mime[0], fp.read()) 
          
        mail.send(msg)
        remove(os.getcwd()+"/public/adjuntos/"+request_data["adjunto"])
      else:

        mail.send(msg)
      
      
      return Response("Enviado con exito",200)

  except NameError :
     
      return Response("El correo no se pudo enviar",404)


  
@app.route('/adjuntar', methods=['POST'])
def adjuntar():
  try:
    print("entreee aquii")
    if 'adjunto' not in request.files:

      return Response ("El name para enviar adjuntos debe ser ""adjunto""",400)
      
      
    
    file=request.files['adjunto']
    if file.filename == '':
        return Response ("No selecciono el archivo",404)
           
  
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      
    return  Response (filename,201)

  except NameError :
    
      Response ("No se pudo guardar cargar el archivo",400)
      
@app.route('/validar', methods=['POST'])
def validar():
  try:
    server=smtplib.SMTP_SSL("smtp.gmail.com",465 )
    # server.starttls()
    server.login(username,password)
    server.quit()
    return Response ("OK",200)
  except :
    return Response ("No pudo ingresar al Correo",503)
if __name__ == '__main__':

    app.run(debug = False)
