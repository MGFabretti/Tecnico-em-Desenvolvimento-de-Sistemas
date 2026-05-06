saltos = []

for i in range(7):
    saltos.append(int(input("digite o valor do salto: ")))

# todos os saltos na orden que foram digitalizados
print(saltos)

# maior
maior = saltos[0]

for salto in saltos:
    if(salto > maior):
        maior = salto

print("o maior salto é: ", maior)

# menor
menor = saltos[0]

for salto in saltos:
    if(salto < menor):
        menor = salto

print("o maior salto é: ", menor)

# média sem maior e menor
soma = 0

for salto in saltos:
    if(salto != maior and salto != menor):
        soma = soma + salto
media = soma / 5
print("a média sem maior e menor é: ", media)

# media
soma = 0

for salto in saltos:
    soma = soma + salto
media_geral = soma / 7
print("a media é: ",media_geral)