'''altere o exercício anterior para permitir
achar o nome de um aluno na lista'''

alu = int(input("Quantos alunos tem na sala? "))
sala = [0]*alu

for x in range (alu):
    nome = input(f"Digite seu nome: ")
    sala[x] = nome

achou = 0
perg = input("Você quer saber a posição de que aluno? ")
for i in range (alu):
    if perg == sala [i]:
        achou += 1    #flag = bandeira (sinalizadora para avisar se algo foi encontrado)
        print(f"{perg} esta na {i}º posição.")

if achou == 0:
    print("Nome não estã na lista.")
