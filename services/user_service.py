import json
from models.user import User

class UserService:
    def __init__(self, filepath='users.json'):
        self.filepath = filepath
        self.users = self.load()

    def load(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [User.from_dict(u) for u in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def get_all_users(self):
        return self.users

    def add_user(self, user: User):
        if self.find_user_by_email(user.email):
            return False

        max_id = max((u.id for u in self.users), default=0)
        user.id = max_id + 1

        self.users.append(user)
        self.save()
        return True

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, **kwargs):
        user = self.find_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.save()
            return True
        return False

    def delete_user(self, user_id):
        user_to_delete = self.find_user_by_id(user_id)
        if not user_to_delete:
            return False

        self.users = [user for user in self.users if user.id != user_id]
        self.save()
        return True

user_service = UserService()