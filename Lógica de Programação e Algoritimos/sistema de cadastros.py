# sistema de cadastro de produtos
# o sistema deverá permetir:
# - cadastrar
# - listar
# - deletar

#crianção das listas
usuarios = []
produtos = []

#----------------------
# -------- Função Menu Usuario ---------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("----- Menu Usuários -------")
        print("1 - cadastrar usuario")
        print("2 - Listar Usuário")
        print("3 - Deletar Usuário")
        print("4 - voltar")
        opcao_menu_usuario = int(input("escolha uma opção: "))

        match opcao_menu_usuario:
            #  cadastrar usuario
            case 1:
                nome = input("digite o nome: ")
                telefone = input("digite o telefone: ")
                email = input("digite o email: ")

                # criação do json de usuarios (chave: valor)
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }

                # Adicionar o kson no array
                usuarios.append(usuario)
                print(f"Usuario {usuario['nome']} cadastrado cokm sucesso!")
            # listar o usuario
            case 2:
                print("\n Lista de usários: ")

                if(len(usuarios) == 0):
                    print("Nenhum Usuário cadastrado! ")
                else:
                    for usu in usuarios:
                        print("-------------")
                        print("nome: ", usu["nome"])
                        print("telefone: ", usu["telefone"])
                        print("email: ", usu["email"])
            # deletar o usuario
            case 3:
                nome_deletar = input("digite o nome do usuario que deseja deletar")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("usuario removido com sucesso")

                if(encontrado == False):
                    print("usuario não encontrado!")
            # voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break

#----------------------
# -------- Função Menu Produtos ---------
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5):
        print()
        print("----- Menu Produtos -------")
        print("1 - cadastrar produto")
        print("2 - Listar produto")
        print("3 - Deletar produto")
        print("4 - calcular produto")
        print("5 - voltar")

        opcao_menu_produto = int(input("escolha uma opção: "))

        match opcao_menu_produto:
            #  cadastrar produto
            case 1:
                nome = input("digite o nome: ")
                descricao = input("digite o descricao: ")
                quantidade = input("digite o quantidade: ")
                valor = float(input("digite o valor: "))

                # criação do json de produto (chave: valor)
                produto = {
                    "nome": nome,
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }

                # Adicionar o kson no array
                produtos.append(produto)
                print(f"Usuario {produto['nome']} cadastrado cokm sucesso!")
            # listar o produto
            case 2:
                print("\n Lista de produtos: ")

                if(len(produtos) == 0):
                    print("Nenhum produto cadastrado! ")
                else:
                    for pro in produtos:
                        print("-------------")
                        print("nome: ", pro["nome"])
                        print("descricao: ", pro["descricao"])
                        print("quantidade: ", pro["quantidade"])
                        print("valor: ", pro["valor"])
            # deletar o produto
            case 3:
                nome_deletar = input("digite o nome do produto que deseja deletar")
                encontrado = False

                for pro in produtos:
                    if(pro["nome"] == nome_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("produto removido com sucesso")

                if(encontrado == False):
                    print("produto não encontrado!")
            # voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break

#---------------------------------------
#--------- Menu Principal --------------
opcao_menu = 0 
while(opcao_menu != 3):
    print("---------- Menu - Sistema de Cadastro --------")
    print("Opções: ")
    print("1 - Usuários")
    print("2 - produtos")
    print("3 - Sair")
    opcao_menu = int(input("escolha uma opção: "))

    match opcao_menu:
        # menu usuarios
        case 1:
            menu_usuarios()
        # menu produtos
        case 2:
            menu_produtos()

        case 3:
            print("até logo!")

        case _:
            print("opção invalida")