numeros = []
cont_pares = 0

for i in range(10):
    num = int(input("digite um numero: "))
    numeros.append(num) 
for numero in numeros: 
    if(numero%2 == 0):
        cont_pares = cont_pares + 1
print("a quantiade de pares é: ",cont_pares)