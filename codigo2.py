

numero = int(input("Ingrese un número entero: "))

if numero <= 0:
    print("ERROR. El número debe ser mayor que cero.")
else:
    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()