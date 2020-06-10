from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from pusher_client import pusher_client


class PusherAuth(BaseModel):
    channel_name: str
    socket_id: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)


@app.post("/pusher/auth")
async def pusher_auth(*, channel_name: str = Form(...), socket_id: str = Form(...)):
    auth = pusher_client.authenticate(
      channel=channel_name,
      socket_id=socket_id,
    )
    return auth
