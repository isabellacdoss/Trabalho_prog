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

def montante_ano (base, ano):       # mostra o valor total subsidiado pelo governo durante o ano

    somatorio = 0 
    for i in range (len(base["Ano"])):
        if (base.at[i, 'Ano']) == ano:
            a = (base.at[i, 'Valor_subsidiado'])
            somatorio += a

    print ("O valor subsidiado pelo governo durante o ano de", ano, "foi de", somatorio)

# Análise 3 - Determinação dos montante total por região do valor do financiamento (2009 a 2023)

def montante_regiao (base, regiao):  

    somatorio = 0 
    for i in range (len(base["Região"])):
        if (base.at[i, 'Região']) == regiao:
            a = (base.at[i, 'Valor_financiamento'])
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

# Análise 6 - 



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

    opcoes = int(input("Escolha uma opção:\n 1 - "))


    ano = int(input("Digite o ano (2009 a 2023):\n"))
    regiao = input("Digite o nome da região(Norte, Nordeste, Centro-Oeste, Sudeste ou Sul):\n")
      
    n = media_uni_habitacionais (dados,ano)

    print (dados)

    print()

    estado (dados)

    print ()

    print ("Média de unidades habitacionais no ano de", ano, ":" , n)

main()


            
                       
