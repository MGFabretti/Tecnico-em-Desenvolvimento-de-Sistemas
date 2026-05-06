linhas = int(input("quantas linhas (i): "))
colunas = int(input("quantas colunas (j): "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"M[{i}][{j}] = ")))
    matriz.append(linha)

print("matriz preenchida: ")
for linha in matriz:
    print(linha)