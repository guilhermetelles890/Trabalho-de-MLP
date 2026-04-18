from models.pessoa import Pessoa
from models.livro import Livro
from models.usuario import Usuario
from models.funcionario import Funcionario
from models.emprestimo import Emprestimo

def cadastrar_pessoa():
        nome = input("Digite um nome: ")
            
        while True:
            try:
                idade = int(input("Digite a idade: "))
                cpf = int(input("Digite o CPF: "))

                return Pessoa(
                    nome = nome,
                    idade = idade,
                    cpf = cpf
                )
                
            except ValueError as error:
                print(f"Error:{error}")
                print("Digite valores válidos")

def cadastrar_livro():
    
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        while True:
            try:
                quantidade_total = int(input("Digite a quantidade total: "))
                quantidade_disponivel = int(input("Digite a quantidade disponível: "))

                return Livro(
                    titulo=titulo,
                    autor=autor,
                    quantidade_total=quantidade_total,
                    quantidade_disponivel=quantidade_disponivel
                )

            except ValueError as erro:
                print(f"Erro: {erro}")
                print("Digite valores válidos.")

def cadastrar_usuario():
    while True:
        try:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            email = input("Digite o email: ")
            identidade_leitor = int(input("Digite a identidade do leitor: "))
            limite_emprestimos = int(input("Digite o limite de empréstimos: "))
            emprestimos_ativos = int(input("Digite a quantidade de empréstimos ativos: "))

            return Usuario(
                nome=nome,
                cpf=cpf,
                email=email,
                identidade_leitor=identidade_leitor,
                limite_emprestimos=limite_emprestimos,
                emprestimos_ativos=emprestimos_ativos
            )

        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Digite valores válidos.")

def cadastrar_funcionario():
    while True:
        try:
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            email = input("Digite o email: ")
            cargo = input("Digite o cargo: ")
            salario = float(input("Digite o salário: "))
            
            data_texto = input("Digite a data de admissão (AAAA-MM-DD): ")
            data_admissao = datetime.strptime(data_texto, "%Y-%m-%d").date()

            return Funcionario(
                nome=nome,
                cpf=cpf,
                email=email,
                cargo=cargo,
                salario=salario,
                data_admissao=data_admissao
            )

        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Digite valores válidos.")

def cadastrar_emprestimo(usuario, livro):
    while True:
        try:
            data_texto = input("Digite a data do empréstimo (AAAA-MM-DD): ")
            data_emprestimo = datetime.strptime(data_texto, "%Y-%m-%d").date()

            data_devolucao_texto = input(
                "Digite a data de devolução (AAAA-MM-DD) ou deixe vazio: "
            )

            if data_devolucao_texto.strip() == "":
                data_devolucao = None
            else:
                data_devolucao = datetime.strptime(
                    data_devolucao_texto,
                    "%Y-%m-%d"
                ).date()

            return Emprestimo(
                usuario=usuario,
                livro=livro,
                data_emprestimo=data_emprestimo,
                data_devolucao=data_devolucao
            )

        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Digite valores válidos.")