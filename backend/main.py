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
    payload_dict = json.loads(payload)

    silent_token = payload_dict.get("token")
    access_token = get_access_token(silent_token, payload_dict.get("uuid"))


    user_info = get_user_info(access_token)
    wall_info = get_wall(access_token)

    return {"user": user_info, "wall": wall_info}

def get_access_token(silent_token: str, uuid: str) -> str:
    # service_token = "your_service_token"
    service_token = "e920735be920735be920735bceea36b2d9ee920e920735b8cad3f590c7b819bd3bebbbc"

    exchange_url = "https://api.vk.com/method/auth.exchangeSilentAuthToken"
    params = {
        "v": "5.199",
        "token": silent_token,
        "access_token": service_token,
        "uuid": uuid
    }

    response = requests.post(exchange_url, data=params)
    exchange_result = response.json()

    access_response = exchange_result.get("response")
    access_token = access_response.get("access_token")

    return access_token

def get_user_info(access_token: str) -> dict:
    user_info_url = "https://api.vk.com/method/users.get"
    user_info_params = {
        "v": "5.199",
        "access_token": access_token,
        "fields": "sex, status" 
    }

    user_info_response = requests.post(user_info_url, data=user_info_params)
    user_info = user_info_response.json()

    return user_info

def get_wall(access_token: str) -> dict:
    wall_url = "https://api.vk.com/method/wall.get"
    wall_params = {
        "v": "5.199",
        "access_token": access_token,
        "count": 10 
    }

    wall_response = requests.post(wall_url, data=wall_params)
    wall_info = wall_response.json()

    return wall_info
