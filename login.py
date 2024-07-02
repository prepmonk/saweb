import logging
import os
from dotenv import load_dotenv
from fastapi import FastAPI

from logger import get_logger
from metadb import get_supabase_client
from security.cors import add_app_cors

load_dotenv()
logger = get_logger(__name__)

app = FastAPI()
add_app_cors(app)


@app.post("/login")
async def login(email: str, password: str):
    db = get_supabase_client()
    user = db.auth.sign_in_with_password({"email": email, "password": password})
    return {"token": user.session.access_token}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="login:app", host='0.0.0.0', port=5056, access_log=False, log_level="info")
                # ,workers=1, reload=True)
