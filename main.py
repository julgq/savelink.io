from fastapi import FastAPI, Form
from twilio.rest import Client

app = FastAPI()
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

@app.post("/")
async def root(Body: str = Form(), From: str = Form(...)):
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    from_whatsapp_number = 'whatsapp:+14155238886'
    twilio_client.messages.create(body='Your {{1}} code is {{2}}', from_=from_whatsapp_number, to=From)
    message = Body.lower()
    phone_no = From.replace('whatsapp:', '')
    print(message, phone_no)
    return {'resp':'hi'}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
