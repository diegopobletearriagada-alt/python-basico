# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431


# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        texto = ""
        for llave in diccionario:
            texto += llave + " - " + str(diccionario[llave]) + ", "
        print(texto[:-2])


cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes2)


# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])

iterarDiccionario2("nombre", cantantes2)
iterarDiccionario2("pais", cantantes2)


# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for llave in diccionario:
        print(str(len(diccionario[llave])) + " " + llave.upper())
        for valor in diccionario[llave]:
            print(valor)
        print("")

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)
