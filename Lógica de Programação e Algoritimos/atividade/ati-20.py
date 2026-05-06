maiores = 0

for i in range(6):
    idade = int(input(f"Digite a idade: "))
    if idade >= 18:
        maiores += 1

print(f"Total de pessoas maiores de idade: ",maiores)
