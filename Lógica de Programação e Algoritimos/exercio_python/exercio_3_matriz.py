matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Matriz[{i}][{j}] = ")))
    matriz.append(linha)
x = int(input("digite um numero para ser procurado: "))
contador = 0
for i in range(4):
    for j in range(4):
        if(matriz[i][j] == x):
            print("X esta na matriz")
            print("posiçao i: ",i)
            print("posiçao j: ",j )
            contador+=1

if(contador == 0):
    print("X nao esta matriz")