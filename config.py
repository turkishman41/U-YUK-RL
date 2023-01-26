import os
import pyrogram 
import time


botStartTime2 = time.time()

class Config:

    APP_ID = os.environ.get("APP_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    OWNER_ID = os.environ.get("OWNER_ID", 'mmagneto') 
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
    KANAL = os.environ.get("KANAL", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    