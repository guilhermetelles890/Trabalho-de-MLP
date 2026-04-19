from datetime import datetime
from models.pessoa import Pessoa
from models.livro import Livro
from models.usuario import Usuario
from models.funcionario import Funcionario
from models.emprestimo import Emprestimo
from utils.cadastros import cadastrar_pessoa, cadastrar_usuario, cadastrar_funcionario, cadastrar_livro
## Menu de opções##
def menu():
    pessoas = []
    usuarios = []
    funcionarios = []
    livros = []
    emprestimos = []

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

            case "2":
                usuario = cadastrar_usuario()
                usuarios.append(usuario)
                print("Usuário cadastrado!")

            case "3":
                funcionario = cadastrar_funcionario()
                funcionarios.append(funcionario)
                print("Funcionário cadastrado!")

            case "4":
                livro = cadastrar_livro()
                livros.append(livro)
                print("Livro cadastrado!")

            case "0":
                print("Saindo...")
                break

            case _:
                print("Opção inválida!")