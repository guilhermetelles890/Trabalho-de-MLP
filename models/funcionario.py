from dataclasses import dataclass
from datetime import date
from models.pessoa import Pessoa

@dataclass
class Funcionario(Pessoa):
    cargo: str
    salario: float
    data_admissao: date

    def __post_init__(self):
        super().__post_init__()  # chama validação da Pessoa

        if self.salario < 0:
            raise ValueError("Salário não pode ser negativo")