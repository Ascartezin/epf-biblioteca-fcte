import json
from pathlib import Path
from models.livro import Livro

class LivroService:
    def __init__(self, filepath='data/livros.json'):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.livros = self.load()

    def get_all_livros(self):
        return self.livros

    def load(self):
        if not self.filepath.exists():
            return []
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
    def gerar_id(self):
        if not self.livros:
            return 1
        return max(livro.id for livro in self.livros) + 1

    def add_livro(self, livro):
        livro.id = self.gerar_id()
        self.livros.append(livro)
        self.save()

    def update_livro(self, livro_id, titulo, autor):
        livro = self.find_livro_by_id(livro_id)
        if livro:
            livro.titulo = titulo
            livro.autor = autor
            self.save()
            return True
        return False

    def delete_livro(self, livro_id):
        self.livros = [livro for livro in self.livros if livro.id != livro_id]
        self.save()

livro_service = LivroService()