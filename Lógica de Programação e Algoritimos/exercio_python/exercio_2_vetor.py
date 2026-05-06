numeros = []
soma = 0
media =0

for i in range(6):
    num = int(input("digite um numero: "))
    numeros.append(num) 
for numero in numeros: 
    soma = soma + numero    
media = soma/6
print("a media é: ", media)