#PRODUTO E O DESCONTO ATRIBUIDO (ESCREVA O VALOR DO PRODUTO E O DESCONTO DADO PARA O CLIENTE)

produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o quantidade de desconto: '))

desconto_add = (desconto / 100  + 1 ) * produto - produto
desconto_a = produto - desconto_add


print('Valor do seu produto: {:.2f}R$'.format(produto))
print('Desconto oferecido e {:.2f}%, valor do produto com desconto: {:.2f}R$'.format(desconto,desconto_a))
