#Sistema para identificar a idade

#Inserindo a idade do usuário
idade = int(input('Escreva sua idade: '))

#Conjunto de instâncias para descobrir a idade
if (idade <= 12):
    print('Criança')
elif (idade >=13 and idade <= 17):
    print('Adolescente')
elif (idade >=18 and idade <= 64 ):
    print('adulto')
else:
    print('idoso')

# outra forma de fazer isso:
# if (idade >= 65): idoso
# elif (idade >= 18): adulto
# elif (idade >=12): adolescente
# else: criança
# Como o Python funciona por linhas existe essa lógica que é possível ser feito.