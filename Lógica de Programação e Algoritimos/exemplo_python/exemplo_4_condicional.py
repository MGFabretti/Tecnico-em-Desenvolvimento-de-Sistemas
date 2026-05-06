num1 = int(input("digite um numero : "))
num2 = int(input("digite outro numero: "))
operacao = input("digite a operação (+,-,*,/): ")

if(operacao == "+"):
    resultado = num1+num2
elif(operacao == "-"):
    resultado = num1-num2
elif(operacao == "*"):
    resultao = num1*num2
elif(operacao == "/" and num2 != 0):
    rsultado = num1/num2
else:
    resultado = "ERRO"
print("resultado é: ",resultado)