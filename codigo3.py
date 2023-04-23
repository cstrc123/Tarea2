

primero = input("Ingrese la primera palabra: ")
segundo = input("Ingrese la segunda palabra: ")

if len(primero) != len(segundo):
    print("ERROR. Las palabras deben tener la misma longitud.")
else:
    intercalada = ""
    for i in range(len(primero)):
        intercalada += primero[i] + segundo[i]
    print("La palabra intercalada es:", intercalada)
