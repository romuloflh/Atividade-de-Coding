alunos = []

def add_aluno():
    print("\nADICIONAR ALUNO")

    nome = input("Digite o nome do aluno: ").strip()

    while True:
        try:
            idade = int(input("Digite a idade do aluno: "))

            if idade > 2:
                break
            else:
                print("A idade deve ser maior que dois.")

        except ValueError:
            print("Digite uma idade válida.")

    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))

            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota válida.")

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\nLISTA DE ALUNOS")

    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Nota: {aluno['nota']:.1f}")

def buscar_aluno():
    print("\nBUSCAR ALUNO")

    nome_busca = input("Digite o nome do aluno: ").strip()

    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca.lower():
            print("\nAluno encontrado:")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']} anos")
            print(f"Nota: {aluno['nota']:.1f}")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")

def rem_aluno():
    print("\nREMOVER ALUNO")

    nome_remover = input("Digite o nome do aluno: ").strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome_remover.lower():
            alunos.remove(aluno)
            print("Aluno removido com sucesso.")
            return

    print("Aluno não encontrado.")

def media_geral():
    print("\nMÉDIA GERAL")

    if len(alunos) == 0:
        print("Não há alunos cadastrados para calcular a média.")
        return

    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    media = soma / len(alunos)

    print(f"A média geral das notas é: {media:.2f}")


# Programa principal
while True:
    print("\n")
    print("SISTEMA DE ALUNOS")
    print("\n")
    print("1 = Adicionar aluno")
    print("2 = Listar todos os alunos")
    print("3 = Buscar aluno pelo nome")
    print("4 = Remover aluno")
    print("5 = Mostrar média geral das notas")
    print("6 = Sair")
    print("\n")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        add_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        rem_aluno()

    elif opcao == "5":
        media_geral()

    elif opcao == "6":
        print("Programa será encerrado.")
        break

    else:
        print("Opção inválida. Escolha uma das opções de 1 a 6.")