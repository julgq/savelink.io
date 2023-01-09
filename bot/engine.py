from bot.twilio_services import send_message_twilio
from sqlalchemy.orm import Session
from schemas import Message
from answers import get_answers
import models


def bot_engine(message: Message, db: Session):
    number = message.number.replace('whatsapp:', '')
    # validate if number exists
    user = db.query(models.Users).filter(models.Users.whatsapp == number).first()
    if not user:
        send_message_twilio(message.number, get_answers('welcome', 'es') % number)

    send_message_twilio(message.number, message.message.lower() + ', ' + message.number.replace('whatsapp:', ''))
    return True
