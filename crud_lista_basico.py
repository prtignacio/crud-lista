try:
    with open("arquivo_crud.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Dados recuperados")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

alunos = []

while True:
    print("Selecione uma opção:")
    print("1. Criar aluno")
    print("2. Ler alunos")
    print("3. Buscar aluno por ID")
    print("4. Atualizar aluno")
    print("5. Excluir aluno")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        if len(alunos) == 0:
            id_aluno = 1
        else:
            id_aluno = alunos[-1][0] + 1
        dados_aluno = [id_aluno, nome, idade]
        alunos.append(dados_aluno)
        print("Aluno criado com sucesso.")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Não há alunos cadastrados.")
        else:
            for aluno in alunos:
                print("ID:", aluno[0])
                print("Nome:", aluno[1])
                print("Idade:", aluno[2])
                print("-----")

    elif opcao == "3":
        id_busca = int(input("Digite o ID do aluno que deseja buscar: "))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                print("ID:", aluno[0])
                print("Nome:", aluno[1])
                print("Idade:", aluno[2])
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "4":
        id_busca = int(input("Digite o ID do aluno que deseja atualizar: "))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                novo_nome = input("Digite o novo nome do aluno: ")
                nova_idade = int(input("Digite a nova idade do aluno: "))
                aluno[1] = novo_nome
                aluno[2] = nova_idade
                print("Aluno atualizado com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "5":
        id_busca = int(input("Digite o ID do aluno que deseja excluir: "))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                alunos.remove(aluno)
                print("Aluno excluído com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "0":
        # Gravar os valores da lista alunos no arquivo
        with open("arquivo_crud.txt", "w") as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno[0]},{aluno[1]},{aluno[2]}\n")
        print("Dados salvos no arquivo.")
        break

    else:
        print("Opção inválida. Por favor, digite novamente.")