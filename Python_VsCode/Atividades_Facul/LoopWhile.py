#Loop while
# letra = input('Digite uma letra: ')

#Cria um Loop em que caso a letra seja igual a P, repete a pergunta e retorna a pergunta a cada p respondido
# while(letra == 'p'):
#     print('Loop do P')
#     letra = input('Digite uma letra: ')

# print('Saí do Loop')

#Loop que vai somando o count até ser 10
# count = 0

# while(count <= 10):
#     print(count)
#     count += 1


#Joguinho de adivinhação

#Biblioteca que gera números aleatórios
import random

#Definindo atributos do jogo:

#Gerando um número aleatório de 1 a 10
numerosecreto =  random.randint(1, 10) 
#Loopando o jogo
jogar = True
#vidas do jogador
vidas = 3

#Loopando o Jogo
while(jogar):

    #Introdução do jogo
    print('Seja bem-vindo ao jogo, tente adivinhar um número de 1 a 10')
    print('Lembrando que você tem 3 vidas, então cuidado')
    tentativa = int(input('Insira seu número: '))

    #Conferindo se o número citado é maior que 0 ou menor que 10
    while(tentativa >= 10 or tentativa <= 0):
        tentativa = int(input('Valor inserido inválido, escolha um número de 1 a 10: '))
        
    #Loop para continuar tentando adivinhar
    while(numerosecreto != tentativa):
        if(tentativa > numerosecreto ):
            tentativa = int(input("Mais pra baixo, tente outro:"))
            vidas -= 1
        else:
            tentativa = int(input("Mais alto, tente outro: "))
            vidas -= 1
        
        if(vidas == 0):
            print('Sua vida chegou ao fim, Game Over')
            jogar = False
            SystemExit

    #resultado do jogo
    print(f'Parabéns você acertou! O número Secreto era: {numerosecreto}')
    
    #Verificação se o Loop jogo continua
    opc = input('Deseja continuar? S/N')
    if(opc == 's'):
        print('----------------------------------')
    else:
        print('Obrigado por Jogar!')
        jogar = False