
#Análise 1



def media_comum (lista):
    somatorio = 0
    for i in range (len(lista)):
        n = lista[i]
        somatorio = 

        




def media_anos (base):
    lista_2009 = []
    lista_2010 = []
    lista_2011 = []
    lista_2012 = []
    lista_2013 = []
    lista_2014 = []
    lista_2015 = []
    lista_2016 = []
    lista_2017 = []
    lista_2018 = []
    lista_2019 = []
    lista_2020 = []
    lista_2021 = []
    lista_2022 = []
    lista_2023 = []
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == 2009:
            lista_2009.append (base.at[i, 'Quantidade'])
            media_2009 = base.

    

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

    media (dados)

main()


            
                       
