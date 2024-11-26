from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

class Blog(BaseModel):
    id: Optional[str] = Field(None, alias="_id") # CouchDB compatibility
    rev: Optional[str] = Field(None, alias="_rev") # CouchDB compatibility
    title: str
    content: str
    author: str
    published: bool
    tags: Optional[List[str]] = []
    created: Optional[datetime.datetime] = None # Make it optional
    updated: Optional[datetime.datetime] = None

    def __init__(self, **data):
        super().__init__(**data)
        now = datetime.datetime.now(datetime.timezone.utc) # UTC timestamp
        self.created = now
        self.updated = now



class UpdateBlog(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    updated: Optional[datetime.datetime] = None

