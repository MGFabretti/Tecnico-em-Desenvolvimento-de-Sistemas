idade = int(input("digite sua idade: "))

if(idade >=0 and idade <= 12):
    print("voce é criança!")
elif(idade >=13 and idade <=17):
    print("voce é adolecente!")
elif(idade >=18 and idade <=59):
    print("voce é adulto")
elif(idade >=60):
    print("voce é idoso")
else:
    print("Erro")