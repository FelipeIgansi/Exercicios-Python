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

def ObtemAmigo(possivel_numero_amigo):
    lista_divisores = ObtemDivisores(possivel_numero_amigo)

    valor_obtivo_pela_soma_dos_divisores = SomaDivisores(lista_divisores)

    return valor_obtivo_pela_soma_dos_divisores

valor = int (input("Qual valor você deseja verificar se tem um amigo:  "))

possivel_numero_amigo = ObtemAmigo(valor)
amigo = ObtemAmigo(possivel_numero_amigo)

if(amigo == valor):
    print("O valor escolhido {} é amigo de {}.".format(amigo, possivel_numero_amigo))
else:
    print("Infelizmente o valor inserido não possui um correspondente amigo. :(")