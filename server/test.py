import couchdb
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
url = os.getenv("DATABASE_URL")

try:
    couch = couchdb.Server(url)
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
