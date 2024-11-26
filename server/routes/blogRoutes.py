from fastapi import APIRouter, Depends
from models.blogModel import Blog, UpdateBlog
import controllers.blogController as blogController

blog_router = APIRouter(prefix="/blogs", tags=["Blog"])

@blog_router.get("/blog/all")
def getAllBlogs():
    return blogController.getAllBlogs()

@blog_router.get("/blog/{id}")
def getSingleBlog(id: int):
    return blogController.getSingleBlog(id)

@blog_router.post("/blog/create")
def createBlog(blog: Blog):
    return blogController.createBlog(blog)

@blog_router.put("/blog/update/{id}")
def updateBlog(id: int, update_data: UpdateBlog):
    return blogController.updateBlog(id, update_data)

@blog_router.delete("/blogs/{id}")
def deleteBlog(id: int):
    return blogController.deleteBlog(id)
