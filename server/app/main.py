from fastapi import FastAPI
from routes.blogRoutes import blog_router  # Import the router defined in blogRoutes.py

# Initialize FastAPI application
app = FastAPI()

# Include the blog routes
app.include_router(blog_router)

# Health check endpoint
@app.get("/")
def index():
    return {"status": "Blog server is running"}
