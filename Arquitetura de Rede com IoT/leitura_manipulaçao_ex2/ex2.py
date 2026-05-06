# importar as bibliotecas
import pandas as pd
import os

dados = {
    "nome":  [],
    "id": [],
    "quantidade":[],
    "preço":[]
}
desseja_continuar = ""

while(desseja_continuar != "n"):
    print("\n digite os dados: ")
    nome = input("nome: ")
    id = input("id: ")
    quantidade = input("quantidade: ")
    preço = float(input("preço: "))

    dados["nome"].append(nome)
    dados["quantidade"].append(quantidade)
    dados["id"].append(id)
    dados["preço"].append(preço)

    desseja_continuar = input("deseja continuar? (s/n)").strip().lower()
    # strip() = tirar espaços em branco
    # lower() = dexia tudo minusculo 

df = pd.DataFrame(dados)
print(df)

#definir o camhinho onde será salvo o arquivo 
os.chdir("C:\\Users\\46189103804\\Documents\\leitura_manipulaçao_ex2")

df.to_csv("dados.csv", index=False)
print("dados salvos em 'dados.csv' !")

try:
    
        df_lido = pd.read_csv("dados.csv")
        print(df_lido)
except FileNotFoundError:
    print("\n arquivo não encontrado! ")