from modelos import Aluno, listar_alunos

def exibir_menu():
    print("===================================")
    print("DIÁRIO DE CLASSE")
    print("0 - Sair")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno por ID")
    print("===================================")

def cadastrar_aluno():
    nome_aluno = input("Digite o nome: ")
    sobrenome_aluno = input("Digite o sobrenome do aluno: ")
    media_aluno = input("Digite a média do aluno: ")

    aluno = Aluno(nome_aluno, sobrenome_aluno, media_aluno)
    aluno.salvar()

def mostrar_alunos():
    for aluno in listar_alunos():
        aluno.exibir()
    

while True:
    exibir_menu()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao =="1":
        cadastrar_aluno()
    elif opcao =="2":
        mostrar_alunos()
    elif opcao =="3":
        filtrar_aluno()
    else:
        print("Opção inválida! Tente novamente!")