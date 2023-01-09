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



@app.post("/")
async def root(Body: str = Form(), From: str = Form(...), db: Session = Depends(get_db)):
    message = Message(message=Body.lower(), number=From)
    response = bot_engine(message, db)
    return {
        'response': response
    }

