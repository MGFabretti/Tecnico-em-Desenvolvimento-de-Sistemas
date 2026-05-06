matriz = []
n = int(input("digite um numero"))

for i in range(n):
    linha = []
    for j in range(n):
        if(i == j):
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

print("matriz identidade: ")
for linha in matriz:
    print(linha)