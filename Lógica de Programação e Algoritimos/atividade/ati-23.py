matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o elementos: "))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento

print(f"A soma de todos os elementos é: ",soma)