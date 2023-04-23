

mi_lista = [1, 2, 2, 8, 1, 10, 900, 1, 5, 4,]

no_repetidos = []
for num in mi_lista:
    if num not in no_repetidos:
        no_repetidos.append(num)

print("Lista:", mi_lista)
print("Lista sin números repetidos:", no_repetidos)