from fastapi import FastAPI
from twilio.rest import Client
from dotenv import load_dotenv
import os

app = FastAPI()

customers = [
    {"phone": "+8180xxxxxxxx", "content_sent": False},
]

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_NUMBER = os.getenv("FROM_NUMBER")

if not ACCOUNT_SID or not ACCOUNT_SID or not FROM_NUMBER:
    raise ValueError("Environment variables are not set")

@app.post("/send-sms")
def send_sms():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Hello from FastAPI + Twilio!",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    return {"status": "sent", "sid": message.sid}

@app.get("/send-pending-sms")
def send_pending_sms():
    client = Client(ACCOUNT_SID,AUTH_TOKEN)

    sent_count = 0

    for customer in customers:
        if not customer["content_sent"]:
            message = client.messages.create(
                body="今回は送れたかな？",
                from_=FROM_NUMBER,
                to=customer["phone"]
            )

            customer["content_sent"] = True
            sent_count += 1

    return {"sent": sent_count}