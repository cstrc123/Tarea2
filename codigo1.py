

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

