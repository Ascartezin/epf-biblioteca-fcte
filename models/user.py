class User:
    def __init__(self, id, name, email, birthdate):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }

    @staticmethod
    def from_dict(data):
        return User(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate']
        )
