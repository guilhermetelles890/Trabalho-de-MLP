from datetime import datetime

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
            cpf = str (input("Digite o CPF: "))

            return Pessoa(
                nome=nome,
                idade=idade,
                cpf=cpf
            )

        except ValueError as error:
            print(f"Erro: {error}")
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
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o CPF: ")
            identidade_leitor = int(input("Digite a identidade do leitor: "))

            return Usuario(
                nome=nome,
                idade=idade,
                cpf=cpf,
                identidade_leitor=identidade_leitor
            )

        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Digite valores válidos.")


def cadastrar_funcionario():
    while True:
        try:
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o CPF: ")
            cargo = input("Digite o cargo: ")
            salario = float(input("Digite o salário: "))

            data_texto = input("Digite a data de admissão (AAAA-MM-DD): ")
            data_admissao = datetime.strptime(data_texto, "%Y-%m-%d").date()

            return Funcionario(
                nome=nome,
                idade=idade,
                cpf=cpf,
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

def menu():
    pessoas = []
    usuarios = []
    funcionarios = []
    livros = []

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar Pessoa")
        print("2 - Cadastrar Usuário")
        print("3 - Cadastrar Funcionário")
        print("4 - Cadastrar Livro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pessoa = cadastrar_pessoa()
                pessoas.append(pessoa)
                print("Pessoa cadastrada!")

            case "0":
                break