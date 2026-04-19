# ejercicio 1
for numero in range(101):
    print(numero)

# ejercicio 2
for numero in range(2, 501, 2):
    print(numero)

# ejercicio 3
for numero in range(1, 101):
    if numero % 10 == 0:
        print("baby")
    elif numero % 5 == 0:
        print("ice ice")
    else:
        print(numero)

    #ejercicio 4
    suma = 0

for numero in range(0, 500001, 2):
    suma += numero

print(suma)

# ejercicio 5
for numero in range(2024, 0, -3):
    print(numero)

    #ejercicio 6
    numInicial = 3
numFinal = 10
multiplo = 2

for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)