
matriz = []

print("Digite os elementos da matriz 2x3:")
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento: "))
        linha.append(valor)
    matriz.append(linha)

print("\nSoma de cada coluna:")
for j in range(3):
    soma_coluna = 0
    for i in range(2): 
        soma_coluna += matriz[i][j]
    print(f"Coluna:",j ,soma_coluna)
