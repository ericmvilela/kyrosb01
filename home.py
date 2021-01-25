import main


option = 0

while option != 5:

    print()
    print("Digite 1 para Visualizar clientes")
    print("Digite 2 para Adicionar cliente")
    print("Digite 3 para Editar cliente")
    print("Digite 4 para Remover cliente")
    print("Digite 5 para Sair")
    option = int(input("--> "))
    print()

    if option == 1:
        main.VisualizarClientes()

    elif option == 2:

        nome = input("Digite o nome do cliente\n--> ")
        print()

        cpf = input("Digite o CPF (apenas numeros)\n--> ")
        print()

        birthDate = input("Digite a data de nascimento (dd/mm/aaaa)\n--> ")
        print()

        email = input("Digite o email\n--> ")
        print()

        tele = input("Digite o telefone (apenas numeros)\n--> ")
        print()

        main.AdicionarCliente(nome, cpf, birthDate, email, tele)
    
    elif option == 3:
        main.EditarCliente()
    
    elif option == 4:
        
        cpf = input("Digite o CPF do cliente a ser removido (apenas numeros)\n--> ")
        print()

        main.RemoverCliente(str(cpf))
    
    elif option == 5:
        exit()
    
    else:
        print("Opcao invalida")