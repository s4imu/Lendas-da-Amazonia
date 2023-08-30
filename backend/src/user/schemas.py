from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str 

class UserDTO(BaseModel):
    name: str
    email: str