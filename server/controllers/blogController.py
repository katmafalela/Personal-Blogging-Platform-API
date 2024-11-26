from fastapi import Depends, HTTPException
from db.db import get_db
from models.blogModel import Blog, UpdateBlog

def getAllBlogs(database=Depends(get_db)):
    try:
        blogs = [doc for doc in database.view("_all_docs", include_docs=True)]
        return {"blogs": blogs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching blogs: {e}")

def createBlog(blog: Blog, database=Depends(get_db)):
    try:
        new_blog = database.save(blog.dict())
        return {"message": "Blog created successfully", "blog": new_blog}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating blog: {e}")
