#atividade: Fazer um verificador de Peso de acordo com a medida IMC.

peso = int(input('Insira seu peso: '))
altura = float(input('Insira sua altura:'))

imc = peso / (altura **2)


if imc > 65:
    print('Obeso')
elif imc > 35:
    print("gordo")
elif imc > 25:
    print ("normal")
else:
    print("????")