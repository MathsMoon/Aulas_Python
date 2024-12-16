#Aula sobre condições no Python -- Apresentando média de aluno

#Criação de variáveis e inserção dos dados
Aluno = input('Escreva seu nome: ') #Opcional
repetente = input('Você é repetente? Sim ou Não: ').upper()
nota1 = float (input('Escreva sua primeira nota: '))
nota2 = float (input('Escreva sua segunda nota: '))
nota3 = float (input('Escreva sua terceira nota: '))
nota4 = float (input('Escreva sua quarta nota: '))

#Cálculo da Média
resultado = (nota1 + nota2 + nota3 + nota4)/4

#Condições para o {Aluno} passar, reprovar ou ir de recuperação.
if (resultado >= 7):
    print(f'{Aluno} sua média foi de: {resultado}, você passou de ano')
elif (resultado < 7 and repetente == 'NÃO'):
    print(f'{Aluno} sua média foi de: {resultado}, você foi para a recuperação')
else:
    print(f'{Aluno} sua média foi de: {resultado}. você foi reprovado')