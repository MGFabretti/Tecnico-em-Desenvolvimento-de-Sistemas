pi = 3.14
raio = float(input("digite o raio: "))
altura = float(input("digite a altura: "))

area = 2*pi*raio*(raio+altura)
volume = pi*(raio*raio)*altura

print("a area do cilindro é: ", area)
print("o volume do cilindro é: ", volume)