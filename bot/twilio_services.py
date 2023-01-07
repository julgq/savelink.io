from twilio.rest import Client
import os

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
