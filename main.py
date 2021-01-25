import json
from os import path

def VisualizarClientes():
    
    if path.isfile('clientes.json') == False:
        NaoExiste()

    with open('clientes.json') as f:
        data = json.load(f)
    f.close()

    if len(data['clientes']) == 0:
        print("Arquivo vazio")
    
    for cliente in data['clientes']:
        print("Nome:", cliente['nome'])
        print("CPF:", cliente['cpf'])
        print("Data de nascimento:", cliente['data de nascimento'])
        print("E-mail:", cliente['email'])
        print("Telefone:", cliente['tel'])
        print("\n---------------**---------------\n")



def AdicionarCliente(name, cpf, birth, email, tele):
    newCliente = {"nome" : name, "cpf" : cpf, "data de nascimento" : birth, "email" : email, "tel" : tele}
    
    if path.isfile('clientes.json') == False:
        NaoExiste()

    try:
        with open('clientes.json') as f:
            data = json.load(f)
        f.close()
    except:
        NaoExiste()
        with open('clientes.json') as f:
            data = json.load(f)
        f.close()

    jaExiste = 0
    for clientes in data['clientes']:
        if cpf == clientes['cpf']:
            jaExiste = 1

    if jaExiste:
        print("CPF ja cadastrado")
    else:
        with open('clientes.json', 'w') as f:
            data['clientes'].append(newCliente)
            json.dump(data, f, indent=2)
        print("Cliente Adicionado com sucesso")
    
    f.close()

def NaoExiste():
    with open('clientes.json', 'w') as f:
        clientes = {"clientes" : []}
        json.dump(clientes, f, indent=2)
    
    f.close()


def RemoverCliente(cpf):
    removido = 0
    nome = ''
    with open('clientes.json') as f:
            data = json.load(f)
    f.close()

    newData = {"clientes" : []}
    for clientes in data["clientes"]:
        if(clientes["cpf"] == cpf):
            removido = 1
            nome = clientes['nome']
        else:
            newData['clientes'].append(clientes)

    with open('clientes.json', 'w') as f:      
        json.dump(newData, f, indent=2)        
    f.close()

    if(removido):
        print("Cliente", nome, 'removido com sucesso')
    else:
        print("CPF nao encontrado")

def EditarCliente():
    with open('clientes.json') as f:
            data = json.load(f)
    f.close()

    VisualizarClientes()    

    newData = {"clientes" : []}
    encontrado = 0

    while encontrado == 0:
        editCpf = input("Digite o CPF atual do cliente a ser editado: ")
        print()
        for clientes in data["clientes"]:
            if(clientes["cpf"] == editCpf):
                encontrado = 1
                print("Nome atual:", clientes['nome'])
                newName = input("Digite o novo nome: ")
                clientes['nome'] = newName
                print()

                print("CPF atual:", clientes['cpf'])
                newCpf = input("Digite o novo CPF: ")
                clientes['cpf'] = newCpf
                print()

                print("Data de nascimento atual:", clientes['data de nascimento'])
                newBirth = input("Digite a nova data de nascimento: ")
                clientes['data de nascimento'] = newBirth
                print()

                print("E-mail atual:", clientes['email'])
                newEmail = input("Digite o novo email: ")
                clientes['email'] = newEmail
                print()

                print("Telefone atual:", clientes['tel'])
                newTel = input("Digite o novo telefone: ")
                clientes['tel'] = newTel
                print()

                newData['clientes'].append(clientes)
            else:
                newData['clientes'].append(clientes)
        
        if encontrado == 0:
            print("CPF nao encontrado")
        else:
            print("Cliente editado com sucesso")
            
    with open('clientes.json', 'w') as f:      
        json.dump(newData, f, indent=2)        
    f.close()
    



#AdicionarCliente('Sandra Olades', '02390076629', '18/06/1977', 'sandraolades@hotmail.com', '34999130108')
#RemoverCliente('02390076629')
#EditarCliente()