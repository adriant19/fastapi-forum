from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import post, reply


# -- START OF CODE -------------------------------------------------------------
# launch
# uvicorn app.main:app --reload

app = FastAPI()

# CORS - allowed domans

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # wildcard to allow every domain to access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import router objects from files

app.include_router(post.router)
app.include_router(reply.router)
