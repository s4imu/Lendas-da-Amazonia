from mongo.client import db
import user.schemas as schemas
from bson.objectid import ObjectId

class Users:
    def __init__(self):
        self.collection = db["user"]

    def get_all(self):
        user_list = [schemas.UserDTO(**user) for user in self.collection.find()]
        return {"total": len(user_list), "users": user_list}

    def get_by_id(self, user_id: str):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return schemas.UserDTO(**user)

    def create(self, user: schemas.User):
        self.collection.insert_one(user.dict())
        return {"message": "Usuário Criado!"}
    
    def delete(self, user_id: int):
        self.collection.delete_one({"_id": ObjectId(user_id)})
        return {"message": "Usuário Deletado!"}
    
    