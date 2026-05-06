numeros = []

for i in range(5):
    num = int(input(f"Digite os número: "))
    numeros.append(num)

if len(numeros) != len(set(numeros)):
    print("Existem números repetidos!")
else:
    print("Não existem números repetidos.")