#Sistema de fila FIFO

fila = ['cliente1','cliente2','cliente3']
print(fila)

cliente = fila.pop(0)
print(cliente)
print(fila)

cliente = fila.pop(0)
print(cliente)
print(fila)

#Criar a fila

fila = []
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
print(fila)

#Estrutura de reposição - while

fila = ['cliente1','cliente2','cliente3']

while fila:
    cliente = fila.pop(0)
    print(cliente)

#Estrutura de reposição - for

fila = ['cliente1','cliente2','cliente3']
i = 0

for i in range(len(fila)):
    cliente = fila.pop(0)
    print(cliente)

#Sistema de fila LIFO

fila = ['chapa1','chapa2','chapa3']
chapas = fila.pop()
print(chapas)

chapas = fila.pop()
print(chapas)

#Sistema de fila LIFO
pilha = []
pilha.append('chapa1')
pilha.append('chapa2')
pilha.append('chapa3')
print(pilha)

pilha.pop(-1)
print(pilha)
pilha.pop(-1)
print(pilha)

#Sistema de fila LIFO

fila = ['chapa1','chapa2','chapa3']

i = 0
for i in range(len(pilha)):
    chapas = pilha.pop()
    print(chapas)

#Ex 1

lista_chegada = []

nome = input("digite seu nome: ")
lista_chegada.append(nome)
nome1 = input("digite seu nome1: ")
lista_chegada.append(nome1)
nome2 = input("digite seu nome2: ")
lista_chegada.append(nome2)
print(lista_chegada)








