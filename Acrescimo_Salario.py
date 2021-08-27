#LEITOR DE SALARIO E AUMENTO DE ACORDO COM PORCENTAGEM


salario_atual = float(input('Digite seu salario atual: '))
acrescimo = float(input('Digite a % a acrescentar no salario: '))

novo_salario = (acrescimo / 100 + 1 ) * salario_atual

print('Seu Salario era: {:.2f}R$ e com acrescimo de {:.2f}% passou a a ser {:.2f}R$'.format(salario_atual,acrescimo,novo_salario))
