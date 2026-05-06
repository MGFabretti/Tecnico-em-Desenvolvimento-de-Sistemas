notas = []

for i in range(4):
    try:
        nota = float(input(f"digite a {i+1}ª nota: "))

        if nota < 0 and nota > 10:
            print("digite uma nota valida")
            exit()

        else:
            notas.append(nota)

    except ValueError:
        ("insira valores validos")

media = sum(notas)/len(notas)
print(f"a media é ",media)