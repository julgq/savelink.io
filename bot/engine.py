from bot.twilio_services import send_message_twilio
from sqlalchemy.orm import Session
from schemas import Message
import models
from bot.answers import get_answers
from bot.short_link import short_link
import validators



def bot_engine(message: Message, db: Session):
    # get the whatsapp number
    number = message.number.replace('whatsapp:', '')
    # validate if number exists
    user = db.query(models.Users).filter(models.Users.whatsapp == number).first()
    if not user:
        # create new account
        user = models.Users(whatsapp=number)
        db.add(user)
        db.commit()
        send_message_twilio(message.number, get_answers('welcome', 'es') % number)


    # validate if message is a url
    if validators.url(message.message, public=True):
        link = short_link(message.message, user, db)
        send_message_twilio(message.number, get_answers('save_link', 'es') % link)

    else:
        # no is url, then search links using the text.

        """
        Escenarios:
            1 - No tiene cuenta, se da mensaje de bienvenida y se crea la cuenta, se valida el mensaje
            2.- Si tiene cuenta y se valida el mensaje que envio.
            3.- Sí el mensaje enviado es un link entonces el link se, valida y se guarda y se informa sobre lo guardado
            4.- si escribe menu, se le muestra un menu de opciones.
        """
    return {'ok': 1}
