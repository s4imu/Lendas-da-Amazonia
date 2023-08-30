from fastapi import APIRouter
from auth.schemas import Credentials

router = APIRouter()

@router.post("/login/", description="Realiza o login do usuário")
def login(credentials: Credentials):
    return {"message": "Login realizado com sucesso!"}