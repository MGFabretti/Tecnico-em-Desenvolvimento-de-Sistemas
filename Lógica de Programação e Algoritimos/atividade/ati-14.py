positivos = 0
negativos = 0

for i in range(10):
    num = float(input("Digite os número: "))
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Total de positivos: ",positivos)
print(f"Total de negativos: ",negativos)