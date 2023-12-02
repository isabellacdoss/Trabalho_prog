#Análise 1

def media (base, ano):
    lista = []
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == ano:
            lista.append (base.at[i, 'Quantidade'])
    return lista
    

#def media_anos (base, ano):
    

    

def main():

    import os
    import pandas as pd

    print(os.listdir(os.getcwd()))

    dados = pd.read_csv("mcmv_financiado_fgts.csv", sep=";", encoding="ISO-8859-1")
    dados.head()
    dados.rename (columns = {'txt_municipio':'Município','txt_uf':'Estado','txt_regiao':'Região','num_ano_financiamento':'Ano', 'qtd_uh_financiadas':'Quantidade','vlr_financiamento':'Valor_financiado','vlr_subsidio':'Valor_subsidiado'}, inplace = True)

    #modificando para string os dados da coluna de "Valor_financiado" e "Valor_subsidiado" e depois para float, para retirar a "," 

    dados['Valor_financiado'].to_string()
    dados['Valor_subsidiado'].to_string()

    dados = dados.assign(Valor_financiado = dados['Valor_financiado'].str.replace(',','.').astype(float))
    dados = dados.assign(Valor_subsidiado = dados['Valor_subsidiado'].str.replace(',','.').astype(float))

    print(dados)

    ano = int(input("Digite o ano:"))
    media (dados, ano)

main()


            
                       
