import json
import os
from models.livro import Livro

CAMINHO_ARQUIVO = 'data/livros.json'

# Lê todos os livros do arquivo JSON
def carregar_livros():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        return [Livro.from_dict(d) for d in dados]

# Salva a lista de livros no arquivo JSON
def salvar_livros(lista):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump([livro.to_dict() for livro in lista], f, indent=4)

# Retorna todos os livros
def get_all():
    return carregar_livros()

# Busca um livro pelo ID
def get_by_id(id):
    livros = carregar_livros()
    for livro in livros:
        if str(livro.id) == str(id):
            return livro
    return None

# Adiciona um novo livro
def add_livro(livro):
    livros = carregar_livros()
    livros.append(livro)
    salvar_livros(livros)

# Atualiza os dados de um livro existente
def update_livro(id, novos_dados):
    livros = carregar_livros()
    for i, livro in enumerate(livros):
        if str(livro.id) == str(id):
            livros[i] = Livro(
                id=livro.id,
                titulo=novos_dados['titulo'],
                autor=novos_dados['autor'],
                disponivel=novos_dados.get('disponivel', True)
            )
            salvar_livros(livros)
            return

# Remove um livro por ID
def delete_livro(id):
    livros = carregar_livros()
    livros = [livro for livro in livros if str(livro.id) != str(id)]
    salvar_livros(livros)
