numeroEscolhido = int(input('Qual é o valor:   '))

for divisor in range(1, numeroEscolhido, 1):
    if (numeroEscolhido % divisor == 0):
        print("O valor {} é divisor de {}. {} / {} = {}".format(divisor, numeroEscolhido, numeroEscolhido, divisor, (numeroEscolhido/divisor)))