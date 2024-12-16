#Criando uma Lista de carros
carros = ['Corolla', 'Chevette', 'Brasília', 'Uno', 'Strada']
print(carros)

#Apagando um carro específico
print('----------------------------------')
pararemover = input('Insira o carro a ser removido: ')

if pararemover in carros:
    carros.remove(pararemover)
    print(f'O carro {pararemover} foi removido!')
else:
    print('Este carro não está na lista')

print('----------------------------------')
print(carros)
#Mostrando o tamanho do Array atual:
print('----------------------------------')
print(f'existem {len(carros)} carros na lista atual.')

#Adicionando ao final da Lista o Vectra
print('----------------------------------')
carros.append(input('Insira um carro: '))
print(carros)

#Pesquisando se existe um carro no Array
print('----------------------------------')
nomecar = input('Digite um nome de carro: ')

if nomecar in carros:
    print('Este carro existe na lista')
else:
    print('Este carro não existe na lista')

#Criando um for para ler todos os itens da lista
print('----------------------------------')

for carros in carros:
    print(f'A palavra {carros} tem {len(carros)} letras.')


#Lendo apenas os produtos com mais de 6 letras
print('----------------------------------')

# for carro in carros:
#     if len(carros) >=8:
#         print(carro)