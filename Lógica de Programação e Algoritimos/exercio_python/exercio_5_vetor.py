vetor = []
numero = 0

for i in range(8):
    num = int(input("digite um numero: "))
    vetor.append(num)

numero = int(input("digite outro numero: "))

for i in range(8):
    if(vetor[i] == numero):
        print("seu numero digitado tem no vetor")