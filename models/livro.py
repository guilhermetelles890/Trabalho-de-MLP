from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    quantidade_total: int
    quantidade_disponivel: int

    def __post_init__(self):
        if self.quantidade_total < 0:
            raise ValueError("Quantidade total não pode ser negativa")

        if self.quantidade_disponivel < 0:
            raise ValueError("Quantidade disponível não pode ser negativa")

        if self.quantidade_disponivel > self.quantidade_total:
            raise ValueError("Quantidade disponível não pode ser maior que o total")