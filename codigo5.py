

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