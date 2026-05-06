numeros = []
soma = 0

for i in range(7):
    num = int(input("digite os numeros: "))
    numeros.append(num)

for num in numeros:
    soma = soma + num
    print("a soma é",soma)