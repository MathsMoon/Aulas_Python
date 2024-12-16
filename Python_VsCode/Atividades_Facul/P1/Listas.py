#Criação de uma Lista
nums = [10, 20, 30, 40, 50, 60, 70]

#Funcionalidades com a Lista:
#Para mostrar as funcionalidades utilizar o print(paramêtro) que você quer mostrar.


type(nums) #Mostra o tipo da lista
len(nums) #Mostra o tamanho da Lista


print(nums[0]) #Mostra o terceiro elemento da Lista começando pelo index 0
print(nums[-1]) #Mostra o último elemento da lista, começa pelo -1
print(nums[:3]) #O : serve para mostrar não a posição do index, mas relativo a ordem dos fatores na lista.
print(nums[:-3]) #Processo inverso que mostra os últimos 3 da lista


#Para modificar os itens dentro da Lista:
nums[2] = 40
print(nums)

#Para adicionar mais itens a lista
nums.append(80) #Insere os itens ao final da lista (como uma fila)
print(nums)

nums.insert(6, 5) #Insere os itens em index específicados pelo programador. No exemplo eu coloquei o 5 como o sétimo elemento
print(nums)

#nums.sort() ver como usar essa funcionalidade
#print(nums.reverse()) ver como usar essa funcionalidade


#Buscando itens na Lista
# if 20 in nums:
#     printf("Existe sim, na posição: ")