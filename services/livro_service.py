# services/livro_service.py
import json
from models.livro import Livro

class LivroService:
    def __init__(self, filepath='data/livros.json'):
        self.filepath = filepath
        self.livros = self.load()

    def load(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Livro.from_dict(livro) for livro in data]
        except (IOError, json.JSONDecodeError):
            return []

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4, ensure_ascii=False)

    def find_livro_by_id(self, livro_id):
        for livro in self.livros:
            if livro.id == livro_id:
                return livro
        return None

    def get_livros_disponiveis(self):
        return [livro for livro in self.livros if livro.disponivel]

    def marcar_como_disponivel(self, livro_id):
        livro = self.find_livro_by_id(livro_id)
        if livro:
            livro.disponivel = True
            self.save()
            return True
        return False

    def marcar_como_indisponivel(self, livro_id):
        livro = self.find_livro_by_id(livro_id)
        if livro:
            livro.disponivel = False
            self.save()
            return True
        return False

livro_service = LivroService()