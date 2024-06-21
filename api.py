from fastapi import FastAPI
from pydantic import BaseModel


class Chat(BaseModel):
    message: str
    
    
app = FastAPI()

# @app.post("/chats")
# def  create_chat(chat: Chat):
#     s = ['Message']
#     text = Message(s)