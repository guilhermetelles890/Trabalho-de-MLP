from dataclasses import dataclass
from models.pessoa import Pessoa

@dataclass
class Usuario(Pessoa):
    identidade_leitor: int
    limite_emprestimos: int = 3
    emprestimos_ativos: int = 0
    ativo: bool = True

    def __post_init__(self):
        super().__post_init__()

        if self.identidade_leitor <= 0:
            raise ValueError("Identidade de leitor deve ser positiva")

        if self.limite_emprestimos < 0:
            raise ValueError("Limite de empréstimos não pode ser negativo")

        if self.emprestimos_ativos < 0:
            raise ValueError("Empréstimos ativos não pode ser negativo")