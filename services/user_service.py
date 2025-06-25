import json
from pathlib import Path
from typing import List, Optional
from models.user import User 

class UserService:
    def __init__(self, filepath='users.json'):
        self.filepath = Path(filepath)
        self.users: List[User] = []
        self.load()  # Carrega os dados automaticamente ao iniciar

    def load(self):
        """Carrega os usuários do arquivo JSON."""
        if not self.filepath.exists():
            self.users = []
            return
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.users = [User.from_dict(user_dict) for user_dict in data]

    def save(self):
        """Salva a lista de usuários no arquivo JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4, ensure_ascii=False)

    def add_user(self, user: User) -> bool:
        """Adiciona um usuário se o ID ainda não existir."""
        if self.find_user_by_id(user.id) is not None:
            return False  # Já existe um usuário com esse ID
        self.users.append(user)
        self.save()
        return True

    def find_user_by_id(self, user_id: int) -> Optional[User]:
        """Busca um usuário pelo ID."""
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id: int, **kwargs) -> bool:
        """Atualiza os dados de um usuário com base no ID."""
        user = self.find_user_by_id(user_id)
        if user is None:
            return False

        # Atualiza os atributos se estiverem presentes em kwargs
        user.name = kwargs.get('name', user.name)
        user.email = kwargs.get('email', user.email)
        user.birthdate = kwargs.get('birthdate', user.birthdate)
        
        self.save()
        return True

    def delete_user(self, user_id: int) -> bool:
        """Remove o usuário com o ID informado."""
        user = self.find_user_by_id(user_id)
        if user is None:
            return False
        self.users = [u for u in self.users if u.id != user_id]
        self.save()
        return True

    def get_all_users(self) -> List[User]:
        """Retorna a lista de todos os usuários."""
        return self.users
