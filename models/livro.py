

class Livro:
    def __init__(self, id, titulo, autor, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            titulo=data.get('titulo'),
            autor=data.get('autor'),
            disponivel=data.get('disponivel', True)
        )