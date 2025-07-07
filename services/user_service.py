import json
from models.user import User

class UserService:
    def __init__(self, filepath='users.json'):
        self.filepath = filepath
        self.users = self.load()

    def load(self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [User.from_dict(u) for u in data]
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)

    def get_all_users(self):
        return self.users

    def add_user(self, user: User):
        # CORREÇÃO: Gera um ID único para o novo usuário
        # Se a lista estiver vazia, o primeiro ID será 1.
        # Caso contrário, pega o ID máximo e incrementa.
        max_id = max(u.id for u in self.users) if self.users else 0
        user.id = max_id + 1

        self.users.append(user)
        self.save()

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
            return # Usuário não encontrado, não faz nada

        self.users = [user for user in self.users if user.id != user_id]
        self.save()