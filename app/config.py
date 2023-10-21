from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    BROADCAST_MAC = os.getenv("BROADCAST_MAC")
    API_URL = os.getenv("API_URL")