from fastapi import FastAPI, Form
from twilio.rest import Client
import os

app = FastAPI()


@app.post("/")
async def root(Body: str = Form(), From: str = Form(...)):
    # obtener mensaje de whatsapp
    input_message = Body.lower()
    # numero de whatsapp
    input_number = From.replace('whatsapp:', '')
    # detectar si el número existe en la base de datos.

    send_message_twilio(From, 'esto es un mensaje para ti: '+From)

    return {
        'input_message': input_message,
        'input_number': input_number
    }

def send_message_twilio(to_number, message):
    twilio_config = {
        'sdi': os.environ['TWILIO_ACCOUNT_SID'],
        'token': os.environ['TWILIO_TOKEN'],
        'number': 'whatsapp:+14155238886'
    }
    twilio_client = Client(twilio_config['sdi'], twilio_config['token'])
    try:
        twilio_client.messages.create(body=message, from_=twilio_config['number'], to=to_number)
        return 'mensaje enviado a '+to_number+':, '+message
    except Exception as e:
        return 'error al enviar el mensaje: '+e
