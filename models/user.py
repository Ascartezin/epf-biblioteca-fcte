import bcrypt

class User:
    def __init__(self, id, name, email, birthdate, senha_hash):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.senha_hash = senha_hash

    def verificar_senha(self, senha_texto_plano):
        if not self.senha_hash or not senha_texto_plano:
            return False
        return bcrypt.checkpw(senha_texto_plano.encode('utf-8'), self.senha_hash)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'senha_hash': self.senha_hash.decode('utf-8') if self.senha_hash else None
        }

    @classmethod
    def from_dict(cls, data):
        senha_hash_str = data.get('senha_hash')
        senha_hash_bytes = senha_hash_str.encode('utf-8') if senha_hash_str else None
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email'),
            birthdate=data.get('birthdate'),
            senha_hash=senha_hash_bytes
        )