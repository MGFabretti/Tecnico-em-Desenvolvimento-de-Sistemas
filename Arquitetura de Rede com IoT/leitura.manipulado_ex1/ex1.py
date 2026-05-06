# importar as bibliotecas
import pandas as pd
import os

dados = {
    "nome":  [],
    "diciplina": [],
    "nota":[]
}
desseja_continuar = ""

while(desseja_continuar != "n"):
    print("\n digite os dados: ")
    nome = input("nome: ")
    diciplina = input("diciplina: ")
    nota = input("nota: ")

    dados["nome"].append(nome)
    dados["diciplina"].append(diciplina)
    dados["nota"].append(nota)

    desseja_continuar = input("deseja continuar? (s/n)").strip().lower()
    # strip() = tirar espaços em branco
    # lower() = dexia tudo minusculo 

df = pd.DataFrame(dados)
print(df)

#definir o camhinho onde será salvo o arquivo 
os.chdir("C:\\Users\\46189103804\\Documents\leitura.manipulado_ex1\\")

df.to_csv("dados.txt", sep="\t", index=False)
print("dados salvos em 'dados.txt' !")

try:
    
        df_lido = pd.read_csv("dados.txt", sep="\t")
    
except FileNotFoundError:
    print("\n arquivo não encontrado! ")