## Overview
This is the PoC for SaaS Realtime notifications concept, written in async Python (3.6+).

SaaS: [Pusher Channels](https://pusher.com/channels)

API: [FastAPI](https://fastapi.tiangolo.com/)

## Testing

1. Create the Channels application in Pusher
1. Create and activate virtual environment
1. Set credentials in `crm/index.html`
```javascript
    const pusherKey = "__PUSHER_KEY__";  // smth like 08fae1e0be54746e9270
    const pusherCluster = "eu";
```
1. `cd events`
1. Install requirements `requirements.txt`
1. Create `.env` based on `.env.tpl` with credentials from your Pusher application, `PUSHER_MASTER_KEY` must be manually generated (f.e. `openssl rand -base64 32`)
1. Start HTTP server: `uvicorn api:app --reload`
1. Open `crm/index.html` in your favorite browser
1. Run events generator `python event.py`
1. Enjoy received messages in the tab of your browser!

## Troubleshooting

[MacOS SSL issues](https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450)