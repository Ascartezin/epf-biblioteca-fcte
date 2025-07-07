import json
from pathlib import Path
from typing import List, Optional
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self, filepath='data/emprestimos.json'):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.emprestimos: List[Emprestimo] = self.load()

    def load(self) -> List[Emprestimo]:
        if not self.filepath.exists():
            return []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Emprestimo.from_dict(e) for e in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.emprestimos], f, indent=4, ensure_ascii=False)

    def gerar_id(self) -> int:
        if not self.emprestimos:
            return 1
        return max(e.id for e in self.emprestimos) + 1

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        emprestimo.id = self.gerar_id()
        self.emprestimos.append(emprestimo)
        self.save()

    def devolver_livro(self, emprestimo_id: int, data_devolucao: str) -> bool:
        emprestimo = self.find_emprestimo_by_id(emprestimo_id)
        if emprestimo:
            emprestimo.data_devolucao = data_devolucao
            self.save()
            return True
        return False

    def find_emprestimo_by_id(self, emprestimo_id: int) -> Optional[Emprestimo]:
        for e in self.emprestimos:
            if e.id == emprestimo_id:
                return e
        return None

    def get_emprestimos_usuario(self, usuario_id: int) -> List[Emprestimo]:
        return [e for e in self.emprestimos if e.usuario_id == usuario_id and e.data_devolucao is None]

    def get_emprestimos_ativos(self) -> List[Emprestimo]:
        return [e for e in self.emprestimos if e.data_devolucao is None]

emprestimo_service = EmprestimoService()