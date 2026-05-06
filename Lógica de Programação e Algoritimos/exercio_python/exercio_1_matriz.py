matriz1 = []
matriz2 = [] 
matriz_soma = []

#PREENCHER MATRIZ
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz1[{i}][{j}] = ")))
    matriz1.append(linha)

#PREENCHER MATRIZ
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz2[{i}][{j}] = ")))
    matriz2.append(linha)

#PREENCHER MATRIZ
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j]+matriz2[i][j])
    matriz_soma.append(linha)

#EXIBIR MATRIZ PREENCHIDA
print("matriz soma: ")
for linha in matriz_soma:
    print(linha)