
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for i in range(3):
    soma += matriz[i][2-i]

print("A matriz é:")
for linha in matriz:
    print(linha)

print(f"Soma da diagonal secundária: ",soma)
