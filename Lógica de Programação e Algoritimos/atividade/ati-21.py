soma_pares = 0

for i in range(8):
    numero = int(input(f"Digite os número: "))
    
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma dos números pares é: ",soma_pares)
