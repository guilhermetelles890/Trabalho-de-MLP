from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str
    def __post_init__(self):
        if not self.cpf.isdigit():
            raise ValueError("CPF deve conter apenas números")
    
    @classmethod
    def cadastrar_pessoa(cls):
        nome = input("Digite um nome: ")
            
        while True:
            try:
                cpf = input("Digite o CPF: ")
                idade = input("Digite a idade: ")

                return cls(
                    nome = nome,
                    idade = idade,
                    cpf = cpf
                )
                
            except ValueError as error:
                print(f"Error:{error}")
                print("Digite valores válidos")

pessoa1 = Pessoa.cadastrar_pessoa()