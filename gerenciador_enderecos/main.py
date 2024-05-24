import os

def menu():
    print('''
    \t=-=-=-=-=-=-=-=-=-=-=-=-=-= MENU =-=-=-=-=-=-=-=-=-=-=-=-=
    \tDigite 0 - Para ver todas as pessoas e endereços informados
    \tDigite 1 - Para editar um endereço
    \tDigite 2 - Para editar um nome
    \tDigite 3 - Para procurar uma pessoa
    \tDigite 4 - Para sair
    \t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    ''')

def valida_resposta(resposta):
    if resposta not in ["s", "n", "0", "1", "2", "3", "4"]:
        return False
    return True

def mostra_dados(enderecos):
    os.system('cls')
    for k, v in enderecos.items():
        print(f"\tNome: {k}\tEndereço: {v}")

def edita_endereco(enderecos):
    os.system('cls')
    mostra_dados(enderecos)
    nome_endereco = input("Endereço que deseja alterar: ").strip().title()
    if nome_endereco in enderecos.values():
        for k, v in enderecos.items():
            if v  == nome_endereco:
                novo_endereco = input("Informe um novo nome para o endereço: ")
                enderecos[k] = novo_endereco
                print("\nAlteração de endereço concluída com sucesso!\n")
                break
    else:
        print(f"{nome_endereco} não faz parte da lista")
       
    
def edita_nome(enderecos):
    os.system('cls')
    mostra_dados(enderecos)
    nome = input("Nome que deseja alterar: ").strip().title()
    for k in enderecos:
        if nome == k:
            novo_nome = input("Informe o novo nome: ").strip().title()
            enderecos[novo_nome] = enderecos.pop(k)
            print("\nAlteração de nome concluída com sucesso!\n")
            break
    if nome not in enderecos:
        print(f"{nome} não está na lista")


def procura_pessoa(enderecos):
    os.system('cls')
    mostra_dados(enderecos)
    nome = input("Informe o nome da pessoa procurada: ").strip().title()
    for k, v in enderecos.items():
        if k == nome:
            print(f"Nome: {k}\tEndereço: {v}")

    if nome not in enderecos:
        print(f"{nome} não está na lista")
        
enderecos = {}

while True:
    nome = input("Nome: ").strip().title()
    endereco = input(f"Endereço de {nome}: ").strip().title()
    enderecos[nome] = endereco
    while True:
        resposta = input("Deseja informar mais um endereço? [S/N]: ").strip().lower()
        if valida_resposta(resposta):
            break
        print("Resposta inválida, digite apenas 's' ou 'n'")
        continue
    if resposta == "s":
        continue
    break

while True:
    while True:
        menu()
        resposta = input("Informe sua escolha: ")
        if valida_resposta(resposta):
            break
        print("Resposta inválida")
        continue
    if resposta == "0":
        mostra_dados(enderecos)
    elif resposta == "1":
        edita_endereco(enderecos)
    elif resposta == "2":
        edita_nome(enderecos)
    elif resposta == "3":
        procura_pessoa(enderecos)
    else:
        print("Encerrando o programa...")
        break
