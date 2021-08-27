#CALCULADORA

numero = int(input('Digite seu numero: '))

for count in range(10):
    print("%d x %d = %d" % (numero, count+1, numero*(count+1)) )