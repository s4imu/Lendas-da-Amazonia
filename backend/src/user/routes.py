from fastapi import APIRouter, Depends, Request
import user.schemas as schemas
from user.service import Users

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from mongo.client import db

router = APIRouter()
user_class = Users()

templates = Jinja2Templates(directory="user/templates")

@router.get("/users/", description="Retorna todos os usuários")
def get_users():
    database = db["user"]
    user_list = [schemas.UserDTO(**user) for user in database.find()]
    return {"total": len(user_list), "users": user_list}

@router.get("/users/{user_id}", description="Retorna um usuário pelo ID")
def get_user_by_id(request: Request, user_id: str):
    return user_class.get_by_id(user_id)	

@router.post("/users/create", description="Cria um usuário")
def create_user(user: schemas.User):
    return user_class.create(user)

@router.delete("/users/delete/{user_id}", description="Deleta um usuário")
def delete_user(user_id: str):
    return user_class.delete(user_id)