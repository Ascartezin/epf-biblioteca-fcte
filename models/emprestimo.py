# models/emprestimo.py

class Emprestimo:
    def __init__(self, id, usuario_id, livro_id, data_retirada, data_devolucao=None):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_retirada = data_retirada
        self.data_devolucao = data_devolucao

    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'livro_id': self.livro_id,
            'data_retirada': self.data_retirada,
            'data_devolucao': self.data_devolucao
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            usuario_id=data.get('usuario_id'),
            livro_id=data.get('livro_id'),
            data_retirada=data.get('data_retirada'),
            data_devolucao=data.get('data_devolucao')
        )