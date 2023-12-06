# Análise 1 - Média de unidades habitacionais financiadas por ano (2009 a 2023)

def media_uni_habitacionais (base, ano):     # mostra a média anual 

    import numpy as np

    lista = []
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == ano:
            lista.append (base.at[i, 'Quantidade'])
            media_de_unid = np.mean(lista)

    print ("A média e uni. habitacionais financiadas durante o ano de", ano, "foi de:", media_de_unid) 

# Análise 2 - Montante total do valor subsidiano por ano pelo governo 

def montante_ano (base):       # mostra o valor total subsidiado pelo governo durante o ano
    
    ano = 2009
    lista = []    #aqui vai ser guardado o somatório de cada ano, variando entre 2009 e 2023, respectivamente

    while ano < 2024: 
        for i in range (len(base["Ano"])):
            somatorio = 0
            if (base.at[i, 'Ano']) == ano:
                a = (base.at[i, 'Valor_subsidiado'])
                somatorio += a
                lista.append(somatorio)
            ano +=1

    print (lista)

# Análise 3 - Determinação dos montante total por região do valor do financiamento (2009 a 2023)

def montante_regiao (base, regiao):  ##### MODIFICAR print #######

    somatorio = 0 
    for i in range (len(base["Região"])):
        if (base.at[i, 'Região']) == regiao:
            a = (base.at[i, 'Valor_financiado'])
            somatorio += a

    print ("O valor financiado ")

# Análise 4 - Identificação do estado que mais solicitou o financiamento de unidades habitacionais e o que menos solicitou durante o período de 2009 a 2023

def estado (base):

    lista1 = []    #27 listas, 1 para cada estado + Distrito Federal
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []
    lista9 = []
    lista10 = []
    lista11 = []
    lista12 = []
    lista13 = []
    lista14 = []
    lista15 = []
    lista16 = []  
    lista17 = []
    lista18 = []
    lista19 = []
    lista20 = []
    lista21 = []
    lista22 = []
    lista23 = []
    lista24 = []
    lista25 = []
    lista26 = []
    lista27 = []    
    
    for i in range (len(base["Estado"])):
            
        if (base.at[i, "Estado"]) == "Acre":
            lista1.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Alagoas":
            lista2.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Amapï¿½":      # As letras que possuiam acento no nome dos estados, houve um erro, onde aparece "�" no lugar da letra, resolvemos o problema substituindo a letra correta por "ï¿½"
            lista3.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Amazonas":
            lista4.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Bahia":
            lista5.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Cearï¿½":
            lista6.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Espï¿½rito Santo":
            lista7.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Goiï¿½s":
            lista8.append (base.at[i, 'Quantidade'])
      
        elif (base.at[i, "Estado"]) == "Maranhï¿½o":
            lista9.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Mato Grosso":
            lista10.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Mato Grosso do Sul":
            lista11.append (base.at[i, 'Quantidade'])
    
        elif (base.at[i, "Estado"]) == "Minas Gerais":
            lista12.append (base.at[i, 'Quantidade'])
                 
        elif (base.at[i, "Estado"]) == "Parï¿½":
            lista13.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Paraï¿½ba":
            lista14.append (base.at[i, 'Quantidade'])
                
        elif (base.at[i, "Estado"]) == "Paranï¿½":
            lista15.append (base.at[i, 'Quantidade'])
                 
        elif (base.at[i, "Estado"]) == "Pernambuco":
            lista16.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Piauï¿½":
            lista17.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Rio de Janeiro":
            lista18.append (base.at[i, 'Quantidade'])
    
        elif (base.at[i, "Estado"]) == "Rio Grande do Norte":
            lista19.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Rio Grande do Sul":
            lista20.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Rondï¿½nia":
            lista21.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Roraima":
            lista22.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Santa Catarina":
            lista23.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Estado"]) == "Sï¿½o Paulo":
            lista24.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Sergipe":
            lista25.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Estado"]) == "Distrito Federal":
            lista27.append (base.at[i, 'Quantidade'])
                    
        else: 
            lista26.append (base.at[i, 'Quantidade'])

    estados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']
    lista = [sum(lista1), sum(lista2), sum(lista3), sum(lista4), sum(lista5), sum(lista6), sum(lista7), sum(lista8),sum(lista9), sum(lista10),sum(lista11),sum(lista12),sum(lista13), sum(lista14),sum(lista15),sum(lista16), sum(lista17),sum(lista18),sum(lista19),sum(lista20),sum(lista21),sum(lista22), sum(lista23), sum(lista24),sum(lista25),sum(lista26), sum(lista27)]
    minimo = (min(lista))
    maximo = (max(lista))

    print ("A soma dos valores por estado é:", lista, "seguindo a ordem da lista dos estados", estados,". \n")
    print ()

    for i in range (len(lista)):
        if (lista[i]== (minimo)):
            print ("O estado que menos solicitou financiamentos foi:", estados[i],", com", minimo, "financiamentos.")

    for i in range (len(lista)):
        if (lista[i]== (maximo)):
            print ("O estado que mais solicitou financiamentos foi:", estados[i],", com", maximo, "financiamentos.")

# Análise 5 - Avaliação da disparidade na quantidade de unidades habitacionais contratadas pelas capitais dos estados brasileiros durante os anos de 2009 a 2023

def capitais (base):

    lista1 = []    # 27 listas, sendo 1 para cada capital
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []
    lista9 = []
    lista10 = []
    lista11 = []
    lista12 = []
    lista13 = []
    lista14 = []
    lista15 = []
    lista16 = []  
    lista17 = []
    lista18 = []
    lista19 = []
    lista20 = []
    lista21 = []
    lista22 = []
    lista23 = []
    lista24 = []
    lista25 = []
    lista26 = []
    lista27 = []    

    for i in range (len(base["Municípios"])):

        lista = []
            
        if (base.at[i, "Município"]) == "Rio Branco":
            lista1.append (base.at[i, 'Quantidade'])
                
        elif (base.at[i, "Município"]) == "Maceiï¿½":
            lista2.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Macapï¿½":      # As letras que possuiam acento no nome dos estados, houve um erro, onde aparece "�" no lugar da letra, resolvemos o problema substituindo a letra correta por "ï¿½"
            lista3.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Manaus":
            lista4.append (base.at[i, 'Quantidade'])

        elif (base.at[i,"Município"]) == "Salvador":
            lista5.append (base.at[i, 'Quantidade'])

        elif (base.at[i,"Município"]) == "Fortaleza":
            lista6.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Vitï¿½ria":
            lista7.append (base.at[i, 'Quantidade'])

        elif (base.at[i,"Município"]) == "Goiï¿½nia":
            lista8.append (base.at[i, 'Quantidade'])
      
        elif (base.at[i, "Município"]) == "Sï¿½o Luï¿½s":
            lista9.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i,"Município"]) == "Cuiabï¿½":
            lista10.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Campo Grande":
            lista11.append (base.at[i, 'Quantidade'])
    
        elif (base.at[i, "Município"]) == "Belo Horizonte":
            lista12.append (base.at[i, 'Quantidade'])
                 
        elif (base.at[i,"Município"]) == "Belï¿½m":
            lista13.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Município"]) == "Joï¿½o Pessoa":
            lista14.append (base.at[i, 'Quantidade'])
                
        elif (base.at[i, "Município"]) == "Curitiba":
            lista15.append (base.at[i, 'Quantidade'])
                 
        elif (base.at[i, "Município"]) == "Recife":
            lista16.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Teresina":
            lista17.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Rio de Janeiro":
            lista18.append (base.at[i, 'Quantidade'])
    
        elif (base.at[i,"Município"]) == "Natal":
            lista19.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Município"]) == "Porto Alegre":
            lista20.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Município"]) == "Porto Velho":
            lista21.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Município"]) == "Boa Vista":
            lista22.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Florianï¿½polis":
            lista23.append (base.at[i, 'Quantidade'])
                    
        elif (base.at[i, "Município"]) == "Sï¿½o Paulo":
            lista24.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Aracaju":
            lista25.append (base.at[i, 'Quantidade'])

        elif (base.at[i, "Município"]) == "Brasï¿½lia":
            lista27.append (base.at[i, 'Quantidade'])
                    
        else: 
            lista26.append (base.at[i, 'Quantidade'])

    # As capitais estão na mesma ordem dos estados da função da análise 4
    capitais = ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande','Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas', 'Brasília']
    lista = [sum(lista1), sum(lista2), sum(lista3), sum(lista4), sum(lista5), sum(lista6), sum(lista7), sum(lista8),sum(lista9), sum(lista10),sum(lista11),sum(lista12),sum(lista13), sum(lista14),sum(lista15),sum(lista16), sum(lista17),sum(lista18),sum(lista19),sum(lista20),sum(lista21),sum(lista22), sum(lista23), sum(lista24),sum(lista25),sum(lista26), sum(lista27)]
    minimo = (min(lista))
    maximo = (max(lista))

    print ("A soma dos valores por estado é:", lista, "seguindo a ordem da lista dos estados", capitais,". \n")
    print ()

    for i in range (len(lista)):
        if (lista[i]== (minimo)):
            print ("O estado que menos solicitou financiamentos foi:", capitais[i],", com", minimo, "financiamentos.")

    for i in range (len(lista)):
        if (lista[i]== (maximo)):
            print ("O estado que mais solicitou financiamentos foi:", capitais[i],", com", maximo, "financiamentos.")

# Análise 6 - Valor financiado por região e dividido por ano 

def regiao_ano_valor_sub (base, regiao):  

    ano = 2009

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []
    lista9 = []
    lista10 = []
    lista11 = []
    lista12 = []
    lista13 = []
    lista14 = []
    lista15 = []

    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0
    soma5 = 0
    soma6 = 0
    soma7 = 0
    soma8 = 0
    soma9 = 0
    soma10 = 0
    soma11 = 0
    soma12 = 0
    soma13 = 0
    soma14= 0
    soma15= 0

    while ano <= 2023:

        for i in range (len(base["Região"])):

            a = (base.at[i, "Valor_financiado"])

            if ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2009):
                soma1 += a
                lista1.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2010):
                soma2 += a
                lista2.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2011):
                soma3 += a
                lista3.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2012):
                soma4 += a
                lista4.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2013):
                soma5 += a
                lista5.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2014):
                soma6 += a
                lista6.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2015):
                soma7 += a
                lista7.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2016):
                soma8 += a
                lista8.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2017):
                soma9 += a
                lista9.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2018):
                soma10 += a
                lista10.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2019):
                soma11 += a
                lista11.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2020):
                soma12 += a
                lista12.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2021):
                soma13 += a
                lista13.append(soma1)

            elif ((base.at[i,"Região"]) == regiao) and ((base.at[i,"Ano"]) == 2022):
                soma14 += a
                lista14.append(soma1)
            else: 
                soma15 += a
                lista15.append(soma1)
        ano += 1

    print ("O valor financiado pelo região", regiao, "durante o ano de 2009 foi de", soma1)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2010 foi de", soma2)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2011 foi de", soma3)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2012 foi de", soma4)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2013 foi de", soma5)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2014 foi de", soma6)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2015 foi de", soma7)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2016 foi de", soma8)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2017 foi de", soma9)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2018 foi de", soma10)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2019 foi de", soma11)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2020 foi de", soma12)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2021 foi de", soma13)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2022 foi de", soma14)
    print ("O valor financiado pelo região", regiao, "durante o ano de 2023 foi de", soma15)

# Análise 7 - Identificação das 10 cidades que mais receberam subsídio do governo 

def subsidio_10_cidades(base):   

    import pandas as pd

    df = pd.DataFrame(base['Município'])
    df.insert (1,'Valor', base['Valor_subsidiado'])

    df_processado = df.groupby(["Município"], as_index=False).sum()
    
    df_novo = df_processado.sort_values(by='Valor', ascending=False)
    df_impressao = df_novo.head(10)

    print(df_impressao)

# Análise 8 - Comparação entre o número de unidades habitacionais solicitadas por região por ano (2009 a 2023)

def unid_habit_regioes(base):

    import pandas as pd 

    df = pd.DataFrame(base['Região'])
    df.insert(1,'Quantidade_uni_habitacionais', base['Quantidade'])
    df.insert(2, 'Ano', base['Ano'])
    
    df_processado = df.groupby(["Região", "Ano"])["Quantidade_uni_habitacionais"].count()

    pd.set_option("display.max_row", 75)

    print (df_processado)

# Análise 9 - Identificação do município brasileiro que mais solicitou o financiamento de unidades habitacionais em 2022

def municipio_financiamento(base):

    import pandas as pd 

    df = pd.DataFrame(base['Região'])
    df.insert(1,'Quantidade_uni_habitacionais', base['Quantidade'])
    df.insert(2, 'Ano', base['Ano'])
    
    df_processado = df.groupby(["Região", "Ano"])["Quantidade_uni_habitacionais"].count()
    df_processado.head()

    pd.set_option("display.max_row", 75)

    print (df_processado)

# Análise 10 - Valor subsidiado pelo governo por região e por ano 

def regiao_subsidiado (base):

    import pandas as pd

    df = pd.DataFrame(base['Região'])
    df.insert (1,'Valor', base['Valor_subsidiado'])
    df.insert(2, 'Ano', base['Ano'])
        
    df_novo = df.groupby(["Região", "Ano"])
    df_novo.head()
    
    pd.set_option("display.max_row", 375)
    print (df_novo)

def main():

    import os
    import pandas as pd

    print(os.listdir(os.getcwd()))
    path = "mcmv_financiado_fgts.csv"

    dados = pd.read_csv("mcmv_financiado_fgts.csv", sep=";", encoding="latin_1", low_memory=False)
    dados.head()
    dados.rename (columns = {'txt_municipio':'Município','txt_uf':'Estado','txt_regiao':'Região','num_ano_financiamento':'Ano', 'qtd_uh_financiadas':'Quantidade','vlr_financiamento':'Valor_financiado','vlr_subsidio':'Valor_subsidiado'}, inplace = True)

    #modificando para string os dados da coluna de "Valor_financiado" e "Valor_subsidiado" e depois para float, para retirar a "," 

    dados['Valor_financiado'].to_string()
    dados['Valor_subsidiado'].to_string()

    dados = dados.assign(Valor_financiado = dados['Valor_financiado'].str.replace(',','.').astype(float))
    dados = dados.assign(Valor_subsidiado = dados['Valor_subsidiado'].str.replace(',','.').astype(float))

    #opcoes = int(input("Escolha uma opção:\n 1 - "))

    # ano = int(input("Digite o ano (2009 a 2023):\n"))
    #regiao = input("Digite o nome da região(Norte, Nordeste, Centro-Oeste, Sudeste ou Sul):\n")

    regiao_subsidiado(dados)

main()


            
                       
