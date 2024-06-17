import random

# #1 - Lendo o reverso de um Array:
# n = [1 , 2 , 3, 4, 5, 6, 7, 8]

# #Fazendo uma leitura reversa de n
# for i in range(len(n)-1, -1, -1): 
#     print(n[i])

#2 - Mostrando os resultados de um Dado:
dado = [1, 2, 3, 4, 5, 6]
lado = [0, 0, 0, 0, 0, 0]

jogadas = int(input('Quantas vezes vai rolar o dado? '))

while(jogadas > 0):
    lado = random.randint(1, 6)
    
    if(lado == 1):
        lado1 +=1 
    elif(lado == 2):
        lado2 +=1
    elif(lado3 == 3):
        lado3 +=1
    elif(lado4 == 4):
        lado4 +=1
    elif(lado5 == 5):
        lado5 +=1
    else:
        lado6 +=1
    jogadas -=1

for l in dado:
    for j in lado:
        print(f'Lado:{dado[l]} vezes: {lado[j]}') 
    