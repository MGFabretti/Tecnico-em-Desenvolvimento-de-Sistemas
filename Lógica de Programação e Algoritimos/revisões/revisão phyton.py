# criando uma variavel numerica
numero = 0
#criando uma variavel texto
nome = "gabriel"
# iserir um texto
nome_completo = input("digite seu nome")
#iserir um numero inteiro
idade = int(input("digite sua idade: "))
#usuario ensiri numro decimal
salario = float(input("digite seu salario"))
#estruturas condicionais_IF
if(salario > 1500 and idade >= 18):
    print("vc pode tirar carta")
elif(salrio < 1500 or idade <18):
    print("vc n pode tirar a carta")
else:
    print("invalido")
#edtrutura condicional 2
turno = input("digite seu turno (M/V/N)")
if(turno == "M"):
    print("Bom dia")
elif(turno == "V"):
    print("Boa tarde")
elif(turno == "N"):
    print("boa noite")
else:
    print("turno inválido")
#estrutura de repetição_FOR
# 0 -> 10
for i in range(11): #+1
    print(i)
# 1 -> 15
for i in range(1,16): #até 15
    print(i)
#5 -> 65 aumenta 5 em 5
for i in  range(5,66,+5):
    print(i)
#122 -> 0 diminui 2 em 2
for i in range(122,-1,-2):
    print(i)
#usuario escolhe iniio e o fim
# inicio e fim
inicio = int(input("inicio: "))
fim = int(input("fim: "))

for i in range(inicio,fim+1):
    print(i)
#vetores
nomes = []
# sempre para preencher vetor
for i in range(5)
nomes.append(input("digite os nomes"))
#exibir vetor
for nome in nomes:
    print(nome)