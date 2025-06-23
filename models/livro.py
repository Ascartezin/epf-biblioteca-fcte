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

    @staticmethod
    def from_dict(dados):
        return Livro(
            id=dados['id'],
            titulo=dados['titulo'],
            autor=dados['autor'],
            disponivel=dados.get('disponivel', True)
        )
