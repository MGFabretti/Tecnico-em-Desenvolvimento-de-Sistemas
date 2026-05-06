notas = []

for i in range(4):
    # TENTA SOLICITAR AS NOTAS
    try:
        nota = float(input(f"digite a {i+1}ª nota: "))

        if(nota < 0 or nota > 10):
            print("nota invalida. insira um valor entre 0 e 10")
            exit()
        else:
            notas.append(nota)
    # se tiver algun erro de valor, retona uma mensagem
    except ValueError:
        print("Erro: insira um numero valido!")

# se a pessoa apenas digitou texto
if not notas:
    print("Erro: nenhuma nota foi inserida!")
else:
    media = sum(notas)/len(notas)

    if(media >=7):
        print(f"media = {media} - aprovado!")
    elif(media >= 5):
        print(f"media = {media} - recuperação!")
    else:
        print(f"media = {media} - reprovado!")