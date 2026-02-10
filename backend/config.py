import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY  = os.getenv("GOOGLE_API_KEY")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
