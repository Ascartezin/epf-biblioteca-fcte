import json
from pathlib import Path
from typing import List, Optional
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self, filepath='data/emprestimos.json'):
        self.filepath = Path(filepath)
        self.emprestimos: List[Emprestimo] = []
        self.load()

    def load(self):
        if not self.filepath.exists():
            self.emprestimos = []
            return
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.emprestimos = [Emprestimo.from_dict(e) for e in data]

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.emprestimos], f, indent=4, ensure_ascii=False)

    def gerar_id(self):
        return max([e.id for e in self.emprestimos], default=0) + 1

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        self.emprestimos.append(emprestimo)
        self.save()

    def devolver_livro(self, emprestimo_id: int, data_devolucao: str) -> bool:
        for e in self.emprestimos:
            if e.id == emprestimo_id:
                e.data_devolucao = data_devolucao
                self.save()
                return True
        return False

    def get_emprestimos_usuario(self, usuario_id: int) -> List[Emprestimo]:
        return [e for e in self.emprestimos if e.usuario_id == usuario_id]

    def get_emprestimos_ativos(self) -> List[Emprestimo]:
        return [e for e in self.emprestimos if e.data_devolucao is None]
