from datetime import datetime
from models.pessoa import Pessoa
from models.livro import Livro
from models.usuario import Usuario
from models.funcionario import Funcionario
from models.emprestimo import Emprestimo
import os

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
            os.system("pause")
            os.system("cls")


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
            data_texto = input("\nDigite a data do empréstimo (AAAA-MM-DD): ")
            data_emprestimo = datetime.strptime(data_texto, "%Y-%m-%d").date()
            print("\n\n")
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
    Emprestimos = []

    while True:
        print("\n================== Menu ==================")
        print("1 - Cadastros no sistema")
        print("2 - Listar relatorio")
        print("0 - Sair")

        opcao1 = input("Escolha uma opção: ")
        os.system("cls")
        match opcao1:

            case "1":
                print("\n================== Cadastros ==================")
                print("1 - Cadastrar Pessoa")
                print("2 - Cadastrar Usuário")
                print("3 - Cadastrar Funcionário")
                print("4 - Cadastrar Livro")
                print("5 - Cadastrar Empréstimo")
                print("0 - Sair")
        
                opcao2 = input("Escolha uma opção: ")
                os.system("cls")
                match opcao2:

                    case "1":
                        nova_pessoa = cadastrar_pessoa()

                        for pessoa in pessoas:
                            if (
                                pessoa.nome == nova_pessoa.nome and
                                pessoa.cpf == nova_pessoa.cpf
                                ):
                                print("Essa pessoa já foi cadastrado")
                                os.system("pause")
                                os.system("cls")
                                break
                        else:
                            pessoas.append(nova_pessoa)
                            print("Pessoa cadastrado!")
                            os.system("pause")
                            os.system("cls")

                    case "2":
                        novo_usuario = cadastrar_usuario()

                        for usuario in usuarios:
                            if (
                                usuario.nome == novo_usuario.nome and
                                usuario.cpf == novo_usuario.cpf
                                ):
                                print("Este usuario já foi cadastrado")
                                os.system("pause")
                                os.system("cls")
                                break
                        else:
                            usuarios.append(novo_usuario)
                            print("Usuario cadastrado!")
                            os.system("pause")
                            os.system("cls")

                    case "3":
                        novo_funcionario = cadastrar_funcionario()

                        for funcionario in funcionarios:
                            if (
                                funcionario.nome == novo_funcionario.nome and
                                funcionario.cpf == novo_funcionario.cpf
                                ):
                                print("Este funcionario já foi cadastrado")
                                os.system("pause")
                                os.system("cls")
                                break
                        else:
                            funcionarios.append(novo_funcionario)
                            print("Funcionario cadastrado!")
                            os.system("pause")
                            os.system("cls")

                    case "4":
                        novo_livro = cadastrar_livro()
                 
                        for livro in livros:
                            if (
                                livro.titulo == novo_livro.titulo and
                                livro.autor == novo_livro.autor
                                ):
                                print("Este livro já foi cadastrado")
                                os.system("pause")
                                os.system("cls")
                                break
                        else:
                            livros.append(novo_livro)
                            print("Livro cadastrado!")
                            os.system("pause")
                            os.system("cls")     

                    case "5":
                        if not usuarios:    
                            print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
                            os.system("pause")
                            os.system("cls")
                            continue  

                        if not livros:    
                            print("Nenhum livro cadastrado. Cadastre um livro primeiro.")
                            os.system("pause")
                            os.system("cls")
                            continue

                        print("Usuários disponíveis:")
                        for i, usuario in enumerate(usuarios):
                            print(f"{i + 1} - {usuario.nome} (CPF: {usuario.cpf})")     
                        usuario_index = int(input("Escolha um usuário pelo número: ")) - 1
                        if usuario_index < 0 or usuario_index >= len(usuarios):
                            print("Opção inválida. Tente novamente.")
                            os.system("pause")
                            os.system("cls")
                        elif usuarios[usuario_index].emprestimos_ativos >= usuarios[usuario_index].limite_emprestimos:
                            print("Limite de emprestimo atingido para este usuario")
                            os.system("pause")
                            os.system("cls")
                            continue
                        os.system("pause")
                        os.system("cls")

                        usuario_selecionado = usuarios[usuario_index]
                        print("Livros disponíveis:")
                        for i, livro in enumerate(livros):
                            print(f"{i + 1} - {livro.titulo} (Autor: {livro.autor})")
                        livro_index = int(input("Escolha um livro pelo número: ")) - 1
                        if livro_index < 0 or livro_index >= len(livros):
                            print("Opção inválida. Tente novamente.")
                            os.system("pause")
                            os.system("cls")
                            continue
                        os.system("pause")
                        os.system("cls")
                        
                        livro_selecionado = livros[livro_index]

                        if livro_selecionado.quantidade_disponivel > 0:
                            novo_emprestimo = cadastrar_emprestimo(usuario_selecionado, livro_selecionado)
                            Emprestimos.append(novo_emprestimo)
                            livro_selecionado.quantidade_disponivel -= 1
                            usuario_selecionado.emprestimos_ativos += 1
                            print("Empréstimo cadastrado!")
                            os.system("pause")
                            os.system("cls")  
                        else:
                            print("Livro esgotado!")
                            os.system("pause")
                            os.system("cls")
                        
                          

                    
                    case "0":
                        print("Saindo de Cadastros...")
                        os.system("pause")
                        os.system("cls")
            
                    case _:
                        print("Opção inválida! Tente novamente.")
                        os.system("pause")
                        os.system("cls")
        
            case "2":
                print("\n================== Relatórios ==================")
                print("1 - Listar Pessoa")
                print("2 - Listar Usuário")
                print("3 - Listar Funcionário")
                print("4 - Listar Livro")
                print("5 - Listar Emprestimos")
                print("0 - Sair")
        
                opcao3 = input("Escolha uma opção: ")
                os.system("cls")
                match opcao3:
                
                    case "1":
                        for i, pessoa in enumerate(pessoas):
                            print(f"Pessoa - {i + 1}\nPessoa: {pessoa.nome}\nIdade: {pessoa.idade}\nCPF: {pessoa.cpf}\n\n")
                        os.system("pause")
                        os.system("cls")
                    case "2":
                        for i, usuario in enumerate(usuarios):
                            print(f"Usuario - {i + 1}\nUsuario: {usuario.nome}\nIdade: {usuario.idade}\nCPF: {usuario.cpf}\nID leitor: {usuario.identidade_leitor}\nLimite Emprestimo Leitor: {usuario.limite_emprestimos}\nEmprestimos Ativos: {usuario.emprestimos_ativos}\n")
                        os.system("pause")
                        os.system("cls")
                    case "3":
                        for i, funcionario in enumerate(funcionarios):
                            print(f"Funcionario - {i + 1}\nNome: {funcionario.nome}\nIdade: {funcionario.idade}\nCPF: {funcionario.cpf}\nCargo: {funcionario.cargo}\nSalario: {funcionario.salario}\nData admissao: {funcionario.data_admissao}\n\n")
                        os.system("pause")
                        os.system("cls")
                    case "4":
                        for i, livro in enumerate(livros):
                            print(f"Livro - {i + 1}\nNome: {livro.titulo}\nAutor: {livro.autor}\nQuantidade Total: {livro.quantidade_total}\nQuantidade Disponivel: {livro.quantidade_disponivel}\n\n")
                        os.system("pause")
                        os.system("cls")
                    case "5":
                        for i, Emprestimo in enumerate(Emprestimos):
                            print(f"Emprestimo - {i + 1}\nUsuario: {Emprestimo.usuario.nome}\nLivro: {Emprestimo.livro.titulo}\nData Emprestimo: {Emprestimo.data_emprestimo}\nData Devolucao: {Emprestimo.data_devolucao}\n\n")
                        os.system("pause")
                        os.system("cls")
                    case "0":
                        print("Saindo de Relatórios...")
                        os.system("pause")
                        os.system("cls")
        
        
        
            case "0":
                print("Saindo do sistema...")
                os.system("cls")
                break