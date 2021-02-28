def ObtemDivisores(numero):
    listaDivisores = []

    for divisor in range(1, numero, 1):
        if (numero % divisor == 0):
            listaDivisores.append(divisor)

    return listaDivisores

def SomaDivisores(lista = []):
    valor = 0
    for divisor in lista:
        valor += divisor

    return valor

def ObtermNumeroPerfeito(possivel_numero_perfeito):

    divisores = ObtemDivisores(possivel_numero_perfeito)

    possivel_numero_perfeito = SomaDivisores(divisores)

    return possivel_numero_perfeito

valor = 0

for i in range(1, 100):
    valor = ObtermNumeroPerfeito(i)
    if(i == valor):
        print("O valor {} é perfeito, ou seja, a soma dos seus divisores : {} é igual ao propio numero".format(valor, ObtemDivisores(valor)))
    