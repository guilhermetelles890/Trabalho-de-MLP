from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str
    def __post_init__(self):
        if not self.cpf.isdigit():
            raise ValueError("CPF deve conter apenas números")