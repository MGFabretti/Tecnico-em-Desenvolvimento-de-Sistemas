pares = []

for i in range(6):
    num = int(input("digite os numeros: "))
    if(num %2 == 0):
        pares.append(num)

for num in pares:
    print(num)