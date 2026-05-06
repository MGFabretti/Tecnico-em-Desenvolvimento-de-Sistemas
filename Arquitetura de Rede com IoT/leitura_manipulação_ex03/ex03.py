# importar as bibliotecas
import pandas as pd
import os

dados = {
    "descricao":  [],
    "id": [],
    "status":[],
}
desseja_continuar = ""

while(desseja_continuar != "n"):
    print("\n digite os dados: ")
    descricao = input("descricao: ")
    id = input("id: ")
    status = input("status: ")

    dados["descricao"].append(descricao)
    dados["id"].append(id)
    dados["status"].append(status)

    desseja_continuar = input("deseja continuar? (s/n)").strip().lower()
    # strip() = tirar espaços em branco
    # lower() = dexia tudo minusculo 

df = pd.DataFrame(dados)
print(df)

#definir o camhinho onde será salvo o arquivo 
os.chdir("C:\\Users\\46189103804\\Documents\\leitura_manipulação_ex03")

df.to_json("dados.json", index=False, indent=4)
print("dados salvos em 'dados.json' !")

try:
    
        df_lido = pd.read_json("dados.json",indent=4)
        print(df_lido)
except FileNotFoundError:
    print("\n arquivo não encontrado! ")