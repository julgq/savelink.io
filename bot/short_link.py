from sqlalchemy.orm import Session
import models
import random
import string

def generate_short():
    source = string.ascii_letters + string.digits
    result_short = ''.join((random.choice(source) for i in range(7)))
    return result_short
def short_link(link, user, db: Session):
    link_query = db.query(models.Links).filter(models.Links.link == link).filter(models.Links.user_id == user.id).first()
    print('imprimir link query', link_query)
    if link_query:
        return 'https://savelink.io/'+link_query.short
    else:
        code = ''
        short = True
        while short:
            code = generate_short()
            print('generando código: ', code)
            short = db.query(models.Links).filter(models.Links.short == code).first()

        link = models.Links(link=link, short=code, user_id=user.id)
        db.add(link)
        db.commit()
        return 'https://savelink.io/'+link.short
