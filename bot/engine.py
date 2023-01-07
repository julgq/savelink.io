from bot.twilio_services import send_message_twilio
from models import Message


def bot_engine(message: Message):
    send_message_twilio(message.number, message.message.lower() + ', ' + message.number.replace('whatsapp:', ''))
    return True
