#alternativa 1
print("------------------------")
numeros = []

for i in range(5):
    num = int(input("digite um numero: "))
    numeros.append(num)  

maior = -9999999999999999999999999999999

for numero in numeros:
    if(numero > maior):
        maior = numero
print("o maior numero é: ", maior)

#alternativa 2
print("---------------------------------")
maior = numeros[0]
for numero in numeros:
    if(numero > maior):
        maior = numero
print("o maior numero é: ", maior)