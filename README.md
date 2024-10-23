# API de Correo Electrónico

Esta API permite el envío de correos electrónicos mediante un servicio SMTP utilizando Flask y Flask-Mail. Además, permite adjuntar archivos y validar las credenciales de un servidor SMTP.

## Características:
- Envío de correos electrónicos en formato HTML o texto plano.
- Adjunto de archivos de forma dinámica.
- Creación de tablas y firmas personalizadas en el cuerpo del correo.
- Validación de credenciales de correo.


## Requisitos

- Python 3.x
- Flask
- Flask-Mail
- Werkzeug

### Instalación de dependencias:

```bash
pip install Flask Flask-Mail Werkzeug


### 3. **Variables de entorno**
Muestra la importancia de proteger las credenciales y cómo configurarlas mediante variables de entorno:

```markdown
## Configuración de credenciales

Para proteger la seguridad, debes configurar tus credenciales de correo electrónico en variables de entorno. Ejemplo:

```python
export MAIL_USERNAME='tu_correo@gmail.com'
export MAIL_PASSWORD='tu_password'



### 4. **Estructura del Código**

## Uso de la API

### Enviar un correo
- **Ruta:** `/`
- **Método:** `POST`
- **Body:**

```json
{
  "destinatario": ["correo@ejemplo.com"],
  "asunto": "Asunto del correo",
  "nombre_servicio": "Nombre del Servicio",
  "mensaje": {
    "saludo": "Hola,",
    "encabezado": "Este es un mensaje de prueba.",
    "cuerpo": "Aquí va el contenido del mensaje.",
    "despedida": "Saludos cordiales.",
    "firma": {
      "style": "color: #b2aaaa;",
      "firma": ["Nombre de la empresa", "Teléfono", "Dirección"]
    }
  },
  "tipo_mensaje": "html",
  "adjunto": "archivo.pdf"
}

