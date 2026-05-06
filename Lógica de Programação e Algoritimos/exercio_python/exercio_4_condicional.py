lado1 = float(input("digite um lado: "))
lado2 = float(input("digite um lado: "))
lado3 = float(input("digite um lado: "))

if((lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3)>lado1):
    if(lado1 == lado2 and lado2 == lado3 and lado3 == lado1):
        print("equilatero")
    elif(lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print("escaleno")
    else: 
        print("isósceles")
else: 
    print("o triangulo não existe")