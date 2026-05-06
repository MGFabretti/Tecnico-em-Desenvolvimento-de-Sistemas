# importar as bibliotecas
import pandas as pd
import os

dados = {
    "nome":  [],
    "idade": [],
    "cidade":[]
}
desseja_continuar = ""

while(desseja_continuar != "n"):
    print("\n digite os dados: ")
    nome = input("nome: ")
    idade = int(input("idade: "))
    cidade = input("cidade: ")

    dados["nome"].append(nome)
    dados["idade"].append(idade)
    dados["cidade"].append(cidade)

    desseja_continuar = input("deseja continuar? (s/n)").strip().lower()
    # strip() = tirar espaços em branco
    # lower() = dexia tudo minusculo 

df = pd.DataFrame(dados)
print(df)

print("\n escolha com quer salvar os dados")
print("1 - CSV \n 2 - JSON \n 3 - TXT")
escolha_arquivo = input("digite o formato desejado: ")

#definir o camhinho onde será salvo o arquivo 
os.chdir("C:\\Users\\46189103804\\Documents\\gravação_leitura_arquivos_python\\")

if(escolha_arquivo == "1"):
    df.to_csv("dados.csv", index=False)
    print(" dados salvos em 'dados.csv' !")
elif(escolha_arquivo == "2"):
    df.to_json("dados.json", orient="records", indent=4)
    print("dados salvos em 'dados.json'! ")
elif(escolha_arquivo == "3"):
    df.to_csv("dados.txt", sep="\t", index=False)
    print("dados salvos em 'dados.txt' !")
else:
    print("escolha invalida")

# leitura dos arquivos
ler_arquivo = input("\n deseja carregar os dados? (s/n):").strip().lower()
if(ler_arquivo == "s"):
    print("\n escolha o formato para ler o arquivo")
    print("1 - CSV \n 2 - JSON \n 3 - TXT")
    escolha_formato = input("digite o formato desejado: ")
    #tenta executar esse bloco
    try:
        if(escolha_formato == "1"):
            df_lido = pd.read_csv("dados.csv")
        elif(escolha_formato == "2"):
            df_lido = pd.read_json("dados.json")
        elif(escolha_formato == "3"):
            df_lido = pd.read_csv("dados.txt", sep="\t")
        else:
            print("formato invalido!")
            df_lido = None
        
        if(df_lido is not None):
            print("\n dados carregados")
            print(df_lido)
    except FileNotFoundError:
        print("\n arquivo não encontrado! ")