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

      msg.html=f""" 
<html>
<body>

Hola {destinatario[0:7]} espero estes bien <br>
<br>

Este mensaje te notifica que se te han entregado los siguientes productos  el dia 2020/02/05 con el codigo de Salida <b>SN00004</b>
<br>
<br>
<div style="text-align:center;">
<table class="default" style=" width:100%;">

  <tr  style="border: 1px solid black; width:100%; " >

    <th style="background-color:black; color:white;padding:1em;" scope="row">Codigo</th>
    <th style="background-color:black; color:white;" >Producto</th>

    <th style="background-color:black; color:white; padding:1em;" >Cantidad</th>



  </tr>
  

  <tr style="border: 1px solid black; width:80%; ">


    <th style="background-color:black; color:white;" >SN00001</th>
    <td >Taladro de punta muy muy pero muyyy larga extremadamente larga </td>

    <td style="text-align:center;">2</td>
    



  </tr>

  


  </tr>
<tr style="border-top: 1px solid black"; width:80%; ">


    <th style="border-top: 1px solid black; background-color:black; color:white;">SN00001</th>
    <td style="border-top: 1px solid black;">Taladro de punta muy muy pero muyyy larga extremadamente larga </td>

    <td style="text-align:center;border-top: 1px solid black;">2</td>
    



  </tr>

</table>

</div
<br>
<br>

Este mensaje ha sido generado de manera <b>automatica</b> por favor no responder.
<br>
<br>
<br>

<i> 

  Universidad La Gran Colombia <br>
  Dependencia de Planta Fisica <br>
  Carrera 6 Nª 12B - 40 <br>
  Teléfono: (601) 3276999  <br>


</i>


<body>

"""
     
      
   else : msg.body= request_data['mensaje']
   
#    msg.body=
#    msg.body = "testing" 
#    msg.html = f""" 
# <html>
# <body>

# Hola {destinatario[0:7]} espero estes bien <br>
# <br>

# Este mensaje te notifica que se te han entregado los siguientes productos  el dia 2020/02/05 con el codigo de Salida <b>SN00004</b>
# <br>
# <br>
# <div style="text-align:center;">
# <table class="default" style=" width:100%;">

#   <tr  style="border: 1px solid black; width:100%; " >

#     <th style="background-color:black; color:white;padding:1em;" scope="row">Codigo</th>
#     <th style="background-color:black; color:white;" >Producto</th>

#     <th style="background-color:black; color:white; padding:1em;" >Cantidad</th>



#   </tr>
  

#   <tr style="border: 1px solid black; width:80%; ">


#     <th style="background-color:black; color:white;" >SN00001</th>
#     <td >Taladro de punta muy muy pero muyyy larga extremadamente larga </td>

#     <td style="text-align:center;">2</td>
    



#   </tr>

  


#   </tr>
# <tr style="border-top: 1px solid black"; width:80%; ">


#     <th style="border-top: 1px solid black; background-color:black; color:white;">SN00001</th>
#     <td style="border-top: 1px solid black;">Taladro de punta muy muy pero muyyy larga extremadamente larga </td>

#     <td style="text-align:center;border-top: 1px solid black;">2</td>
    



#   </tr>

# </table>

# </div
# <br>
# <br>

# Este mensaje ha sido generado de manera <b>automatica</b> por favor no responder.
# <br>
# <br>
# <br>

# <i> 

#   Universidad La Gran Colombia <br>
#   Dependencia de Planta Fisica <br>
#   Carrera 6 Nª 12B - 40 <br>
#   Teléfono: (601) 3276999  <br>


# </i>


# <body>

# """
  
   print(request_data)
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':

    app.run(debug = True,port=5001)