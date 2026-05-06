qtd_num = 0
num = 0
soma = 0

while (num != -1):
    num = int(input("digite um numero: "))
    if(num != -1):
        qtd_num +=1
        soma = soma + num

media = soma / qtd_num
print("a mdeia é",media)
