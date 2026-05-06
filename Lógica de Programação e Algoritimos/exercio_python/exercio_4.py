posicao_inicial = float (input("digite a posicao inicial: "))
posicao_final = float (input("digite a posicao final: "))
tempo_inicial = float (input("digite o tempo inicial: "))
tempo_final = float (input("digite o tempo final: "))

vm = (posicao_inicial-posicao_final)/(tempo_inicial-tempo_final)

print("Sua velocidade média é: ", vm)