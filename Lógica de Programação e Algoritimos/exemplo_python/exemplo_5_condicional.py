idade = int(input("digite sua idade"))
carteira=input("voce tem cnh? ")

if(idade >= 18 and carteira == "sim"):
    print("voce pode dirigir! ")
elif(idade >= 18 and carteira == "não"):
    print("voce nao pode dirigir! ")
elif(idade < 18):
    print("voce nao pode tirar cnh")
else:
    print("erro")