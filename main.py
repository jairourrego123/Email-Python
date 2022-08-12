

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username= 'emailconfirmacionsalidasugc@gmail.com'
password= 'jbygynriouvgucxt'
destinatario= 'jairourrego123@gmail.com'
asunto = 'Salida N00004'



mensaje = MIMEMultipart('alternative')
mensaje['Subject'] =asunto
mensaje['From'] = username
mensaje['To'] = destinatario

html = f""" 
<html>
<body>

Hola espero estes bien <br>
<br>

Este mensaje te notifica que se te han entregado los siguientes productos  el dia 2020/02/05 con el codigo de Salida <b>SN00004</b>
<br>
<br>
<div style="text-align:center;">
<table class="default" style="border: 1px solid black; width:100%; ">

  <tr  >

    <th scope="row">Codigo</th>
    <th>Producto</th>

    <th>Cantidad</th>



  </tr>
  

  <tr>


    <th >SN00001</th>
    <td style=" padding: 0.5%;">Taladro de punta muy muy pero muyyy larga extremadamente larga </td>

    <td style="text-align:center;">2</td>



  </tr>


  </tr>


</table>

</div
<br>
<br>

Este mensaje ha sido generado de manera <b>Automatica</b> por favor no responder.
<br>
<br>
<br>

<i> 

  Universidad La Gran Colombia <br>
  Dependencia de PLanta Fisica <br>
  Carrera 6 Nª 12B - 40 <br>
  Teléfono: (601) 3276999  <br>



</i>


<body>

"""

# el contenido del mensaje como html
parte_html = MIMEText(html,"html") 

# agregar el cnotenido al mensaje

mensaje.attach(parte_html)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(username,password)
    print("Inicio sesion")  
    server.sendmail(username,destinatario,mensaje.as_string())
    print("mensaje enviado")
    server.quit()






# *https://es.stackoverflow.com/questions/539447/envio-autom%C3%A1tico-de-correos-con-python-y-smtp-actualizaci%C3%B3n-junio-2022