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
        
    @classmethod
    def cadastrar_livro(cls):
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        while True:
            try:
                quantidade_total = int(input("Digite a quantidade total: "))
                quantidade_disponivel = int(input("Digite a quantidade disponível: "))

                return cls(
                    titulo=titulo,
                    autor=autor,
                    quantidade_total=quantidade_total,
                    quantidade_disponivel=quantidade_disponivel
                )

            except ValueError as erro:
                print(f"Erro: {erro}")
                print("Digite valores válidos.")