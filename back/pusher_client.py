import os
from dotenv import load_dotenv

import pusher
from pusher.aiohttp import AsyncIOBackend

load_dotenv()

pusher_client = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True,
    backend=AsyncIOBackend,
    encryption_master_key_base64=os.getenv('PUSHER_MASTER_KEY'),
)
