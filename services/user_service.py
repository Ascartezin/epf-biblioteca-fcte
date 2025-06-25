import json
from pathlib import Path
from typing import List, Optional
from models import User 

class UserModel:
    def __init__(self, filepath='users.json'):
        self.filepath = Path(filepath)
        self.users: List[User] = []

    def load(self):
        if not self.filepath.exists():
            self.users = []
            return
        
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.users = [User.from_dict(user_dict) for user_dict in data]

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4, ensure_ascii=False)

    def add_user(self, user: User) -> bool:
        if self.find_user_by_id(user.id) is not None:
            return False
        self.users.append(user)
        return True

    def find_user_by_id(self, user_id) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id, **kwargs) -> bool:
        user = self.find_user_by_id(user_id)
        if user is None:
            return False
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return True

    def delete_user(self, user_id) -> bool:
        user = self.find_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
