valorCompra = float(input("digite o valor da compra:"))
cupomDesconto = input("possui cupom de desconto? ")

if(valorCompra >= 200 or cupomDesconto == "sim"):
    print("voce ganhou um desconto de 15%")
else:
    print("voce nao tem direito de desconto no momento!")