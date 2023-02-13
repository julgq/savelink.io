from fastapi import FastAPI, Form
from sqlalchemy.orm import Session
from fastapi import Depends
from bot.engine import bot_engine
from database import SessionLocal, engine
from schemas import Message
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# bot management
@app.post("/bot")
async def root(Body: str = Form(), From: str = Form(...), db: Session = Depends(get_db)):
    message = Message(message=Body.lower(), number=From)
    response = bot_engine(message, db)
    return {
        'response': response
    }


# get the short link and return the real url.
@app.get("/open-link")
async def open_link():
    print('hey')
    return ''

@app.post("/scraping")
async def scraping():
    print('web scrapping, get title and description')
    return 'scraping'
