from fastapi import FastAPI, HTTPException, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import requests

app = FastAPI()

# Добавляем middleware для поддержки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CallbackPayload(BaseModel):
    type: str
    auth: int
    user: dict
    token: str
    ttl: int
    uuid: str
    hash: str
    loadExternalUsers: bool

@app.post("/callback")
async def authorization(request: Request, payload: str = Body(...)):
    # Декодируем payload из JSON в объект
    payload_dict = json.loads(payload)
    
    # Проводим валидацию с использованием Pydantic
    callback_payload = CallbackPayload(**payload_dict)

    # Получаем Silent token из payload
    silent_token = payload_dict.get("token")

    # service_token = "your_service_token"
    service_token = "e920735be920735be920735bceea36b2d9ee920e920735b8cad3f590c7b819bd3bebbbc"

     # Выполняем обмен Silent token на Access token
    exchange_url = "https://api.vk.com/method/auth.exchangeSilentAuthToken"
    params = {
        "v": "5.199",
        "token": silent_token,
        "access_token": service_token,
        "uuid": payload_dict.get("uuid")
    }

    response = requests.post(exchange_url, data=params)
    exchange_result = response.json()

    # Получаем Access token
    access_response = exchange_result.get("response")
    access_token = access_response.get("access_token")

    user_info_url = "https://api.vk.com/method/users.get"
    user_info_params = {
        "v": "5.199",
        "access_token": access_token,
        "fields": "sex, status" 
    }
    
    user_info_response = requests.post(user_info_url, data=user_info_params)
    user_info = user_info_response.json()


    # Возвращаем подтверждение
    return {"response": user_info}
