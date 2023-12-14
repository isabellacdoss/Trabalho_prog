# ANÁLISES:

# Análise 1 - Média de unidades habitacionais financiadas por ano (2009 a 2023)

def media_uni_habitacionais(base):     # mostra a média anual 

    import pandas as pd

    df = pd.DataFrame(base['Ano'])    
    df.insert (1,'Média', base['Quantidade'])

    df_processado = df.groupby(['Ano'],as_index=False).mean()  #junta os anos e soma a coluna de quantidade que tem anos iguais
    
    return df_processado

# Análise 2 - Valor subsidiado pelo governo por ano

def montante_ano(base):  # mostra o valor total subsidiado pelo governo durante o ano
    
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
    
    import pandas as pd 

    n = {"Anos":[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]}
    df = pd.DataFrame(n)
    df.insert (1, 'Valor_subsidio', lista)

    n = df.head(15)

    return n 

# Análise 3 - Determinação do montante total por região do valor do financiado

def montante_regiao(base):  

    import pandas as pd

    df = pd.DataFrame(base['Região'])    
    df.insert (1,'Valor_financiado', base['Valor_financiado'])

    df_processado = df.groupby(['Região'], as_index=False).sum() #junta os anos e soma a coluna de quantidade que tem anos iguais

    return df_processado

# Análise 4 - Quantidade de unidades habitacionais financiadas pelos estados brasileiros de 2009 a 2023

def estados(base):

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

    estados ={"Estados":['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']}
    lista = [sum(lista1), sum(lista2), sum(lista3), sum(lista4), sum(lista5), sum(lista6), sum(lista7), sum(lista8),sum(lista9), sum(lista10),sum(lista11),sum(lista12),sum(lista13), sum(lista14),sum(lista15),sum(lista16), sum(lista17),sum(lista18),sum(lista19),sum(lista20),sum(lista21),sum(lista22), sum(lista23), sum(lista24),sum(lista25),sum(lista26), sum(lista27)]
    
    import pandas as pd

    df = pd.DataFrame (estados)
    df.insert(1,"Quantidade_de_financiamentos", lista)
    
    return (df)

# Análise 5 - Avaliação da disparidade na quantidade de unidades habitacionais contratadas pelas capitais dos estados brasileiros durante os anos de 2009 a 2023

def capitais(base):

    import pandas as pd 

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

    for i in range (len(base["Município"])):

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
            if (base.at[i, "Município"]) == "Palmas":
                lista26.append (base.at[i, 'Quantidade'])

    # As capitais estão na mesma ordem dos estados da função da análise 4
    capitais = {"Capitais":['Rio Branco', 'Maceiï¿½', 'Macapï¿½', 'Manaus', 'Salvador', 'Fortaleza', 'Vitï¿½ria', 'Goiï¿½nia', 'São Luï¿½s', 'Cuiabï¿½', 'Campo Grande','Belo Horizonte', 'Belï¿½m', 'Joï¿½o Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianï¿½polis', 'Sï¿½o Paulo', 'Aracaju', 'Palmas', 'Brasï¿½lia']}
    lista = [sum(lista1), sum(lista2), sum(lista3), sum(lista4), sum(lista5), sum(lista6), sum(lista7), sum(lista8),sum(lista9), sum(lista10),sum(lista11),sum(lista12),sum(lista13), sum(lista14),sum(lista15),sum(lista16), sum(lista17),sum(lista18),sum(lista19),sum(lista20),sum(lista21),sum(lista22), sum(lista23), sum(lista24),sum(lista25),sum(lista26), sum(lista27)]

    df = pd.DataFrame(capitais)
    df.insert(1,"Unidades_hab", lista)

    return (df.head(len(lista)))

# Análise 6 - Valor financiado por região e ano

def regiao_ano_valor_fin(base):  # os valores não estão corretos

    import pandas as pd

    df = pd.DataFrame (base['Região'])
    df.insert(1,"Ano", base['Ano'])
    df.insert(2,'Valor_financiado', base['Valor_financiado'])

    df_processado = df.groupby(['Região', 'Ano'])['Valor_financiado'].sum().reset_index()
    pd.set_option("display.max_row", 75)

    return (df_processado)

# Análise 7 - Identificação das 10 cidades que mais receberam subsídio do governo 

def subsidio_10_cidades(base):   

    import pandas as pd

    df = pd.DataFrame(base['Município'])
    df.insert (1,'Valor', base['Valor_subsidiado'])

    df_processado = df.groupby(["Município"], as_index=False).sum()
    
    df_novo = df_processado.sort_values(by='Valor', ascending=False)
    
    return(df_novo.head(10))

# Análise 8 - Comparação entre o número de unidades habitacionais solicitadas pela região sudeste durante os anos de 2009 a 2023

def unid_habit_regioes(base):

    import pandas as pd 

    df = pd.DataFrame({"Região":base["Região"]})
    df.insert(1,'Quantidade', base['Quantidade'])
    df.insert(2, 'Ano', base['Ano'])
    
    df_processado = df.groupby(["Região", "Ano"])["Quantidade"].sum().reset_index()

    sudeste= []
    ano = []

    for i in range (len(df_processado['Região'])):

        if df.at[i,"Região"] == "Sudeste":
            sudeste.append(df_processado.at[i,"Quantidade"])
            ano.append(df_processado.at[i,"Ano"])

    df_novo = pd.DataFrame({"Quantidade": sudeste, "Ano": ano})

    return df_novo

# Análise 9 - Identificação dos 10 municípios brasileiros que mais solicitaram unidades habitacionais 

def municipio_financiamento(base): 

    import pandas as pd
    df = pd.DataFrame({"Município":base['Município']})
    df.insert(1,'Quantidade', base['Quantidade'])
        
    df_1 = df.groupby(["Município"])["Quantidade"].sum()

    df_2= df_1.sort_values(ascending=False).reset_index()
    
    return df_2.head(10)

# Análise 10 - Valor subsidiado pelo governo por região e por ano 

def regiao_subsidiado(base):    

    import pandas as pd

    df = pd.DataFrame(base['Região'])
    df.insert(1, 'Ano', base['Ano'])
    df.insert (2,'Valor', base['Valor_subsidiado'])
        
    df_novo = df.groupby(['Região', 'Ano'])['Valor'].sum().reset_index()

    pd.set_option("display.max_row", 75)

    return (df_novo)

# Gera o arquivo log

def gera_log (nome_arq, n_analise, dados_x, dados_y, eixo_x, eixo_y):

    arq = open((nome_arq + ".log"), "w")
    print ("Arquivo de log referente a analise:", n_analise, "intitulado: ", nome_arq, file=arq)
    print ("Os dados da analise sao: ", file = arq)
    print("Para o eixo X (",eixo_x,"): dados = ",dados_x, file=arq)
    print("Para o eixo y (",eixo_y,"): dados = ",dados_y, file=arq)
    arq.close()

# GRÁFICOS:

# Gráfico 1

def grafico_1(dados):

    # Tema: Média de unidades habitacionais financiadas por ano (2009 a 2023)
    # Tipo do gráfico: barras

    import matplotlib.pyplot as mpl

    df = media_uni_habitacionais(dados)

    anos = df["Ano"]
    media = df["Média"]
    
    mpl.figure(figsize = (15,12)) #define o tamanho da imagem 

    mpl.barh(anos, media, color = "blue", label = "Média de unidades habitacionais financiadas por ano")  
    mpl.box(True) # faz aparecer uma margem ao redor do gráfico
    mpl.title("Média de Unidades Habitacionais financiadas por ano pelo programa Minha Casa, Minha Vida")
    mpl.legend()

    mpl.xlabel('Anos')
    mpl.ylabel('Médias de unidades')

    mpl.show() #usado para gerar o gráfico

# Gráfico 2

def grafico_2(dados):

    # Tema: Valor subsidiado pelo governo por ano
    # Tipo de gráfico: linhas

    import matplotlib.pyplot as mpl

    df = montante_ano(dados)

    valor_sub = df["Valor_subsidio"]
    ano = df["Anos"]

    mpl.title('Valor subsidiado pelo Governo por ano')
    mpl.plot(ano, valor_sub)
    mpl.plot(ano,valor_sub, 'go')  #faz aparecer as bolinhas em cima do valor específico por ano 
    mpl.plot(ano, valor_sub, color = "red")

    mpl.ylim(30000, 360000)  # para que os valores do gráfico fiquem nesse intervalo 

    mpl.xlabel('Anos')
    mpl.ylabel('Valor em milhares de reais')

    mpl.show()

# Gráfico 3

def grafico_3(dados):

    # Tema: Determinação do montante total por região do valor do financiado
    # Tipo de gráfico: barras

    import matplotlib.pyplot as mpl

    df = montante_regiao(dados)

    regiao = df["Região"]
    valor_fin= df["Valor_financiado"]

    mpl.figure(figsize = (15,12)) #define o tamanho da imagem 

    mpl.bar(regiao, valor_fin, color = "yellow", label = "Valor financiado")  
    mpl.box(True) # faz aparecer uma margem ao redor do gráfico
    mpl.title("Montante do Valor financiado por Região")

    mpl.ylim (1000,260000000000)
    mpl.legend()

    mpl.xlabel('Regiões')
    mpl.ylabel('Valor em bilhões de reais')

    mpl.show() #usado para gerar o gráfico

# Gráfico 4

def grafico_4(dados):

    # Tema: Quantidade de unidades habitacionais financiadas pelos estados brasileiros de 2009 a 2023
    # Tipo de Gráfico: linhas

    import matplotlib.pyplot as mpl

    df = estados(dados)

    estado = df["Estados"]
    valores = df["Quantidade_de_financiamentos"]

    mpl.title('Quantidade de unidades habitacionais financiadas pelos estados brasileiros')
    mpl.plot(estado, valores)
    mpl.plot(estado, valores, color = "yellow")

    mpl.ylim(0, 1550000)  # para que os valores do gráfico fiquem nesse intervalo 

    mpl.plot(estado,valores,'go',color = "red")

    mpl.xlabel('Estados')
    mpl.ylabel('Valor milhões de unidades')

    mpl.show()
  
# Gráfico 5

def grafico_5(dados):   

    # Tema:
    # Tipo de Gráfico: barras

    df = capitais(dados)

    # capital = df["Capitais"]
    # corrigindo o nome das capitais

    capit = ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande','Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas', 'Brasília']
    quantidade = df["Unidades_hab"]

    import matplotlib.pyplot as mpl

    mpl.title('Unidades habitacionais contratadas por capitais brasileiras')
    mpl.plot(capit, quantidade)
    mpl.plot(capit,quantidade, 'go')  #faz aparecer as bolinhas em cima do valor específico por ano 
    mpl.plot(capit, quantidade, color = "brown")
    mpl.grid(True)

    mpl.ylim(0, 300000)  # para que os valores do gráfico fiquem nesse intervalo 

    mpl.xlabel('Capitais')
    mpl.ylabel('Unidades em milhões')
    mpl.xticks(rotation= 45)

    mpl.show()

# Gráfico 6

def grafico_6(dados):

    # Tema:
    # Tipo de Gráfico: linhas

    import matplotlib.pyplot as mpl

    df = regiao_ano_valor_fin(dados)

    anos = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]

    #plotando o gráfico
    mpl.figure(figsize = (25,20))

    norte= []
    nordeste= [] 
    centro_oeste= []
    sudeste= []
    sul= []

    for i in range (len(df['Região'])):

        if df.at[i,"Região"] == "Norte":
            norte.append(df.at[i,"Valor_financiado"])
        elif df.at[i,"Região"] == "Nordeste":
            nordeste.append(df.at[i,"Valor_financiado"])
        elif df.at[i,"Região"] == "Centro-Oeste":
            centro_oeste.append(df.at[i,"Valor_financiado"])
        elif df.at[i,"Região"] == "Sudeste":
            sudeste.append(df.at[i,"Valor_financiado"])
        else:
            sul.append(df.at[i,"Valor_financiado"])

    mpl.plot(anos, norte, color = "red", label = "Norte")
    mpl.plot(anos, nordeste, color = "yellow",label = "Nordeste")
    mpl.plot(anos, centro_oeste, color = "blue",label = "Centro-Oeste")
    mpl.plot(anos, sudeste, color = "purple",label = "Sudeste")
    mpl.plot(anos, sul, color = "gray",label = "SuL")

    mpl.ylim(10000000, 28000000000)  #valores do eixo y

    mpl.title("Valor financiado por região e ano através do programa Minha Casa, Minha Vida")
    mpl.grid(True)
    mpl.box(True)
    mpl.legend()
    mpl.xlabel("Anos")
    mpl.ylabel("Valor em bilhões de reais")

    mpl.show()

# Gráfico 7

def grafico_7(dados):

    # Tema:
    # Tipo de gráfico: barras

    import matplotlib.pyplot as mpl

    df = subsidio_10_cidades(dados)
    valor = df["Valor"]

    # Colocando os nomes 'corretos' das cidades, pois na base as letras que possuem acento apresentam erro
    cidades = ["São Paulo","João Pessoa","Rio de Janeiro","Uberlândia","Valparaíso de Goiás","Ribeirão Preto","Goiânia", "Feira de Santana", "Campo Grande","Águas Lindas de Goiás"]

    fig, ax = mpl.subplots()
    ax.bar(cidades, valor, color = "blue")
    mpl.xticks(rotation= 15)
    mpl.box(True)
    ax.set(title="As 10 cidades que mais receberma subsídio do Governo durante 2009 e 2023", ylabel="Valor em bilhões")
    mpl.show()

# Gráfico 8   

def grafico_8(dados):

    # Tema:
    # Tipo de Gráfico: barras 

    import matplotlib.pyplot as mpl

    df = unid_habit_regioes(dados)

    valor = df["Quantidade"]
    anos = df["Ano"]

    mpl.figure(figsize = (15,10)) #define o tamanho da imagem 

    mpl.bar(anos,valor,color = "red", label = "Unidades")  
    mpl.box(True) # faz aparecer uma margem ao redor do gráfico
    mpl.grid(True)
    mpl.title("Unidades habitacionais contratadas pela Região Sudeste de 2009 a 2023")
    mpl.legend()

    mpl.ylim (0,230000)

    mpl.ylabel('Quantidade de unidades habitacionais contratadas')
    mpl.xlabel('Anos')

    mpl.show() #usado para gerar o gráfico

# Gráfico 9

def grafico_9(dados):

    # Tema:
    # Tipo de Gráfico: barras

    import matplotlib.pyplot as mpl

    df = municipio_financiamento(dados)

    # Os nomes dos municípios foram inseridos manualmente, pois na base as letras que possuem acento apresentam erro.
    municipio = ['São Paulo', 'Rio de Janeiro', 'João Pessoa', 'Uberlândia', 'Goiânia', 'Ribeirão Preto', 'Brasília', 'Campo Grande', 'Valparaíso de Goiás', 'Curitiba']
    quantidade = df["Quantidade"]

    mpl.figure(figsize = (15,12)) #define o tamanho da imagem 

    mpl.barh(municipio, quantidade, color = "green", label = "Valor do financiamento")  
    mpl.box(True) # faz aparecer uma margem ao redor do gráfico
    mpl.title("OS 10 municípios brasileiros que mais solicitaram financiamento através do programa 'Minha Casa, Minha Vida'")
    mpl.legend()

    mpl.xlabel('Quantidade em milhares')
    mpl.ylabel('Municípios')

    mpl.show() #usado para gerar o gráfico

# Gráfico 10

def grafico_10(dados):

    # Tema:
    # Tipo de Gráfico: linhas

    import matplotlib.pyplot as mpl

    df = regiao_subsidiado(dados)

    anos = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]   # os anos não foram extraídos da base, pois lá eles se repetiam

    #plotando o gráfico
    
    mpl.figure(figsize = (25,20))

    norte= []
    nordeste= [] 
    centro_oeste= []
    sudeste= []
    sul= []

    for i in range (len(df['Região'])):

        if df.at[i,"Região"] == "Norte":
            norte.append(df.at[i,"Valor"])
        elif df.at[i,"Região"] == "Nordeste":
            nordeste.append(df.at[i,"Valor"])
        elif df.at[i,"Região"] == "Centro-Oeste":
            centro_oeste.append(df.at[i,"Valor"])
        elif df.at[i,"Região"] == "Sudeste":
            sudeste.append(df.at[i,"Valor"])
        else:
            sul.append(df.at[i,"Valor"])

    mpl.figure(figsize = (25,20))
    mpl.plot(anos, norte, color = "red", label = "Norte")
    mpl.plot(anos, nordeste, color = "yellow",label = "Nordeste")
    mpl.plot(anos, centro_oeste, color = "orange",label = "Centro-Oeste")
    mpl.plot(anos, sudeste, color = "green",label = "Sudeste")
    mpl.plot(anos, sul, color = "brown",label = "SuL")

    mpl.ylim(100000000, 5000000000)  #valores do eixo y

    mpl.title("Valor subsidiado por região e ano através do programa Minha Casa, Minha Vida")
    mpl.grid(True)
    mpl.box(True)
    mpl.legend()
    mpl.xlabel("Anos")
    mpl.ylabel("Valor em bilhões de reais")


    mpl.show()

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

    '''n_analise = int(input("Digite o número da análise: \n"))
    
    if n_analise == 1:
        grafico_1(dados)
    elif n_analise == 2:
        grafico_2(dados)
    elif n_analise ==3:
        grafico_3(dados)
    elif n_analise ==4:
        grafico_4(dados)
    elif n_analise ==5:
        grafico_5(dados)
    elif n_analise ==6:
        grafico_6(dados)
    elif n_analise ==7:
        grafico_7(dados)
    elif n_analise ==8:
        grafico_8(dados)
    elif n_analise == 9:
        grafico_9(dados)
    else:
        grafico_10(dados)'''
    
    grafico_5(dados)
    
    print(regiao_ano_valor_fin(dados))
    
    nome_arq = input("Digite o nome do arquivo: \n")
    n_analise = input("Digite o n° da análise: \n")
    dados_x = input("Dados de X: \n")
    dados_y = input("Dados de Y: \n")
    eixo_x = input("Eixo X: \n")
    eixo_y = input("Eixo Y: \n")

    gera_log (nome_arq, n_analise, dados_x, dados_y, eixo_x, eixo_y)
    
main()


            
                       
