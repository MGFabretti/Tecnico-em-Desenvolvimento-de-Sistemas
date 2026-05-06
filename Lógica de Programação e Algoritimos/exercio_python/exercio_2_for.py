numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
soma = 0

for i in range(numero1, numero2+1):
    if(i%2 == 0):
        soma = soma +i
print("os numeros par é: ",soma)