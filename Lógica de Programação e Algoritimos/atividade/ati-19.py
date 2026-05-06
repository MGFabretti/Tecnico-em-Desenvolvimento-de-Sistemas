numeros = []

for i in range(4):
    num = float(input(f"Digite os número: "))
    numeros.append(num)

numeros.sort() #ordena os elementos de uma lista diretamente, modificando a lista original em ordem crescente (menor para o maior).

print(f"Números em ordem crescente: ",numeros)