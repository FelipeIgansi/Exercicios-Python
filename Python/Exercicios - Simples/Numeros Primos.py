# Inicia a variavel dos divisores 
divisores = 0

#Array onde será armazenado os primos
listaPrimos = []


for numero in range(1, 100):
    for divisor in range(1, ((numero) // 2) + 1):
        if ((numero % divisor) == 0):
            divisores += 1
            
        
    if (divisores == 1):        
        listaPrimos.append(numero)

        
    divisores = 0 # Zera a quantidade de divisores

print(listaPrimos)
