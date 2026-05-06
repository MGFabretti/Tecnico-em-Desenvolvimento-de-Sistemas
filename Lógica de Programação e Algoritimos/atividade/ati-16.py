numeros = []

for i in range(6):
    valor = float(input("Digite os número: "))
    
    if valor < 0:
        valor = 1
        
    numeros.append(valor)

print("Lista resultante:", numeros)