# FastAPI SMS Automation (Twilio)

A FastAPI-based SMS automation API using Twilio, featuring batch sending and duplicate prevention.

## Features

* Send SMS via Twilio API
* Batch sending endpoint
* Duplicate prevention logic (each customer receives SMS only once)

## Tech Stack

* FastAPI
* Twilio API
* Python
* Docker

## Setup

### 1. Create a Twilio account

Get your Account SID, Auth Token, and Twilio phone number.

### 2. Create a `.env` file

```
ACCOUNT_SID=your_sid
AUTH_TOKEN=your_token
FROM_NUMBER=your_twilio_number
```

---

## Run (Local)

### Install dependencies

```
pip install fastapi uvicorn python-dotenv twilio
```

### Start server

```
uvicorn main:app --reload
```

---

## Run (Docker)

### Build image

```
docker build -t fastapi-sms .
```

### Run container

```
docker run -p 8000:8000 --env-file .env fastapi-sms
```

---

## Endpoints

### Send single SMS

```
POST /send-sms
```

### Send batch SMS (no duplicate)

```
GET /send-pending-sms
```

---

## Notes

* Each customer will receive SMS only once due to duplicate prevention logic
* Trial accounts require verified phone numbers
* `.env` file is required and must not be committed

---

## Example Use Cases

* Appointment reminders
* OTP / verification codes
* Notification systems
