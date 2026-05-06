numeros = []
media = 0
soma = 0
for i in range(4):
    num = int(input("digite um numero: "))
    numeros.append(num) 
for numero in numeros: 
    soma = soma + numero  
media = soma/4
if(media < 4):
    print("reprovado")
elif(media >= 4 and media <=7):
    print("recuperação")
else:
    print("aprovado")