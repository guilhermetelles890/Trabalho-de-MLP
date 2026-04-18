from dataclasses import dataclass
from datetime import date
from models.usuario import Usuario
from models.livro import Livro

@dataclass
class Emprestimo:
    usuario: Usuario
    livro: Livro
    data_emprestimo: date
    data_devolucao: date | None = None

    def esta_ativo(self) -> bool:
        return self.data_devolucao is None