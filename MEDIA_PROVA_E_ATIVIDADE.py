#calculo da media da prova e atividade

prova = int(input('Digite a nota da prova: '))
atividade = int(input('Digite a nota da atividade: '))

media = (prova + atividade) / 2

if media >= 5 and 10:
    print('A sua media foi {}, Voce foi Aprovado'.format(media))

elif media < 5:
    print('Sua Nota foi {}, Voce foi reprovado, Boa Sorte na Proxima Avalicao '.format(media))


    #ABERTO A SUGESTAO, OBG