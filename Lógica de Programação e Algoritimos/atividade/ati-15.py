numeros = []

for i in range(8):
    num = float(input("Digite os número: "))
    numeros.append(num)

media = sum(numeros) / len(numeros)
print("\nMédia: ",media)

print("Números maiores que a média:")
for n in numeros:
    if n > media:
        print(n)