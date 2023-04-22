

numero = int(input("Ingresa un número entero: "))
factorial = 1

if numero < 0:
    print("ERROR. El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial = factorial * i
    print("El factorial de", numero, "es", factorial)







numero = int(input("Ingrese un número entero: "))

if numero <= 0:
    print("ERROR. El número debe ser mayor que cero.")
else:
    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()




primero = input("Ingrese la primera palabra: ")
segundo = input("Ingrese la segunda palabra: ")

if len(primero) != len(segundo):
    print("ERROR. Las palabras deben tener la misma longitud.")
else:
    intercalada = ""
    for i in range(len(primero)):
        intercalada += primero[i] + segundo[i]
    print("La palabra intercalada es:", intercalada)



numeros = [3, 7, 1, 8, 5] 
print("La lista de números aleatorios es:", numeros)

cubos = []
for numero in numeros:
    cubos.append(numero ** 3)

print("La lista de cubos de los números es:", cubos)





sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80,
"math": 90
},
}
}
}

nombre = sampleDict["class"]["student"]["name"]
notas = list(sampleDict["class"]["student"]["marks"].values())
promedio = sum(notas) / len(notas)

resultado = {"nombre": nombre, "nota": promedio}
print(resultado)




mi_lista = [1, 2, 2, 8, 1, 10, 900, 1, 5, 4,]

no_repetidos = []
for num in mi_lista:
    if num not in no_repetidos:
        no_repetidos.append(num)

print("Lista:", mi_lista)
print("Lista sin números repetidos:", no_repetidos)
