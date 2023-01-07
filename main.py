from fastapi import FastAPI, Form
from database import engine
from bot.engine import bot_engine
from models import Message
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.post("/")
async def root(Body: str = Form(), From: str = Form(...)):
    message = Message(message=Body.lower(), number=From)
    response = bot_engine(message)
    return {
        'response': response
    }

