fila = []

while True:
    escolher = input("\nEscolha uma dessas opções \n1- Adicionar Cliente | 2- Atender Cliente | 3- Mostrar fila | 4- Sair \nQual irá escolher: ")

    if escolher == "1":
        nome_cliente = input("Insira o nome do cliente: ")
        fila.append(nome_cliente)
        print(f"Você adicionou o cliente {nome_cliente}")

    elif escolher == "2":
        if fila:
            atendido = fila.pop(0)
            print(f"Atendendo: {atendido}")
        else:
            print("Fila vazia")

    elif escolher == "3":
        print(f"Fila atual: {fila}")

    elif escolher == "4":
        print("Até logo!")
        break

    else:
        print("Opção inválida")






