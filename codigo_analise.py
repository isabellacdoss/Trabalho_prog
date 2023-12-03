# Análise 1 - Média de unidades habitacionais financiadas por ano (2009 a 2023)

def media_uni_habitacionais (base, ano):  

    import numpy as np

    lista = []
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == ano:
            lista.append (base.at[i, 'Quantidade'])
            media_de_unid = np.mean(lista)

    return (media_de_unid) 

# Análise 2 - Montante total do valor subsidiano por ano pelo governo 

def montante_ano (base, ano):

    somatorio = 0 
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == ano:
            a = (base.at[i, 'Valor_subsidiado'])
            somatorio += a

    return (somatorio) 

# Análise 3 - Determinação dos montante total por região do valor do financiamento (2009 a 2023)

def montante_regiao (base, regiao):  

    somatorio = 0 
    for i in range (len(base["Região"])):
        if (base.at[i, 'Região']) == regiao:
            a = (base.at[i, 'Valor_financiamento'])
            somatorio += a

    return (somatorio) 

# Análise 4 - Média dos montantes da análise anterior (3)

#Identificação do estado que mais solicitou o financiamento de unidades habitacionais e o que menos solicitou durante o período de 2009 a 2023;


#def estado (base):
     
    #estados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
    #for i in range(len(base["Município"])):

                   

    

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
    ano = int(input("Digite o ano: \n "))
    # regiao = input("Digite o nome da região: \n")

    n = media_uni_habitacionais (dados,ano)

    por_ano = montante_ano (dados, ano)
    por_regiao = montante_regiao

    print ("Média de unidades habitacionais no ano de", ano, ":" , n)

main()


            
                       
