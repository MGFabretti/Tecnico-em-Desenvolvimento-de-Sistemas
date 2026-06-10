print("----- menu de opção -----")
print("1 - círculo")
print("2 - triângulo")
print("3 - quadrado")
opcao = int(input("digite uma opção: "))

match opcao:
    case 1:
        print("⭕")
    case 2:
        print("🔺")
    case 3:
        print("🟥")
    case _:
        print("opção inválida❌ ")