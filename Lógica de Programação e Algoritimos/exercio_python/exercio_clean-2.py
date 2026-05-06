idade = int(input("digite sua idade"))

if(idade >= 18):
    print("você é maior de idade")

elif(idade >=0 and idade < 18):
    print("você é menor de idade")
    
else:
    print("idade digitada invalida")