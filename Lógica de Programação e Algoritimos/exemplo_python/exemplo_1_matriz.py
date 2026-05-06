matriz = [
    ["laranja","roma","maça-verde","limão","caqui"],
    ["beringela","batata","pimentão","pimenta","pepino"]
]
print(matriz[0]) #imprime 1 linha (fruta)
print(matriz[1]) #imprime 2 linha (legume)

print(matriz[0][2]) #imprime maçã-verde
print(matriz[1][3]) #imprime pimenta

print("frutas: ")
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[0][3])
print(matriz[0][4])

print("legumes: ")
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[1][3])
print(matriz[1][4])

print("matriz completa: ")
for i in range(2): #linhas
    for j in range(5): #colunas
        print(matriz[i][j])