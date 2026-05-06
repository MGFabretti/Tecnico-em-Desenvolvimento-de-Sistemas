vetor = []
for i in range(10):
    num = float(input(f"Digite os número: "))
    vetor.append(num)

menor_valor = vetor[0]
posicao = 0

for i in range(1, 10):
    if vetor[i] < menor_valor:
        menor_valor = vetor[i]
        posicao = i

print(f"Vetor: {vetor}")
print(f"Menor valor: , na posição: ",menor_valor, posicao)
