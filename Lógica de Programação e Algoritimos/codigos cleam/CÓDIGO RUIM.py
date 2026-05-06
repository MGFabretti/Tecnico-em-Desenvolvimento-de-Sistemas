# código ruim
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a + b + c + d) / 4

if x >= 7:
    print("OK")
elif x >= 5:
    print("REC")
else:
    print("NO")

# CLEAM CODE

nota1 = float(input("digite as notas: "))
nota2 = float(input("digite as notas: "))
nota3 = float(input("digite as notas: "))
nota4 = float(input("digite as notas: "))
media = (nota1 + nota2 + nota3 + nota4)/4

print("sua media é",media)

if(media >= 7):
    print("Aprovado")
elif(media >= 5):
    print("recuperação")
elif(media < 5):
    print("reprovado")
else:
    print("notas digitadas invalidas")

#CLEAN CODE

notas = []

for i in range(4):
    notas.append(float(input(f"digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

print("sua media é",media)

if(media >= 7):
    print("Aprovado")
elif(media >= 5):
    print("recuperação")
elif(media < 5):
    print("reprovado")
else:
    print("notas digitadas invalidas")