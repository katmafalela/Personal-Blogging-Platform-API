import couchdb
import models.blogModel as blogModel
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url:
    couch = couchdb.Server(database_url)
else:
    raise ValueError("DATABASE_URL not found in environment variables")

database_name = os.getenv("DATABASE_NAME")

import couchdb
# ... other imports

# ... (rest of your code)

def get_db():
    try:
        print("Attempting to connect to CouchDB...")  # Add logging
        if database_name not in couch:
            print(f"Creating database '{database_name}'...")
            db = couch.create(database_name)
        else:
            print(f"Database '{database_name}' already exists.")
            db = couch[database_name]
        print("Database connection established.")
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}") # Log the exception
        raise  # Re-raise the exception

