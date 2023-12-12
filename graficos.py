# Gráficos

def grafico_1 ():

    import matplotlib.pyplot as mpl

    # dados retirados da análise da base 

    anos = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
    medias = [65.20, 98.25, 105.53, 106.12, 109.77, 110.21, 110.09, 105.95, 120.94, 127.24, 117.19, 121.84, 120.10, 127.05, 97.08]

    mpl.figure(figsize = (15,12)) #define o tamanho da imagem 

    mpl.barh(anos, medias, color = "blue", label = "Média de unidades habitacionais financiadas por ano")  
    mpl.box(True) # faz aparecer uma margem ao redor do gráfico
    mpl.title("Média de Unidades Habitacionais financiadas por ano pelo programa Minha Casa, Minha Vida")
    mpl.legend()

    mpl.show() #usado para gerar o gráfico

def grafico_2 ():

    import matplotlib.pyplot as mpl

    valores = [46802.09, 151253.0, 139322.99, 205832.32, 156336.89, 217680.92, 254939.85, 219517.03, 150234.44, 124757.51, 117391.95, 201072.62, 350850.5, 240661.91, 40507.9]
    anos = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


    mpl.title('Valor subsidiado pelo Governo por ano')
    mpl.plot(anos, valores)
    mpl.plot(anos,valores, 'go')  # faz aparecer as bolinhas em cima do valor específico por ano 
    mpl.plot(anos, valores, color = "red")

    mpl.ylim(30000, 360000)  # para que os valores do gráfico fiquem nesse intervalo 

    mpl.xlabel('Anos')
    mpl.ylabel('Valor em real')

    mpl.show()

def grafico_3 ():

    import matplotlib.pyplot as plt

    valor = [12946852220.03, 92040243169.13,63795437310.07,256984119921.14,113083192208.50 ]
    regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']

def grafico_4():
    import matplotlib.pyplot as mpl

    valores = [3037, 91836, 1372, 26464, 201136, 138976, 67719, 445158,  89701, 104815, 103275, 699513, 64168, 154347, 532971, 176833, 63344, 270560, 123881, 440762, 29244, 4714, 281194, 1494892, 81896, 19823, 55586]
    estados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul','Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']

    # O estado que menos solicitou financiamentos foi o Amapá, com 1372 financiamentos.
    # O estado que mais solicitou financiamentos foi São Paulo, com 1494892 financiamentos.

def grafico_5 ():

    # Análise 5 - Avaliação da disparidade na quantidade de unidades habitacionais contratadas pelas capitais dos estados brasileiros durante os anos de 2009 a 2023

    import matplotlib.pyplot as mpl

    capitais = ['Rio Branco', 'Maceió','Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal','Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas', 'Brasília']
    quantidade = [2138, 43661, 1313, 23495, 44351, 36163, 1528, 65139, 26211, 27098, 55108, 42587, 6088, 78360, 52136, 6238, 22768, 120772, 11631, 50905, 6975, 4519,3659, 267143, 24058, 4687587, 55586] 

    mpl.figure(figsize = (15,10))
    mpl.pie(quantidade, labels = capitais, autopct = '%1.1f%%', shadow = True, startangle = 95)

    mpl.title("Porcentagem de financiamentos por capitail brasileira")

    mpl.show()

def grafico_6 ():
    import matplotlib.pyplot as mpl
    import numpy as np

    #Informações extraídas da base

    anos =[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    norte = [3319568246.700005, 7232612229.750032, 9017751325.800016, 10438799575.34998, 15078316833.750034, 16303938826.199924, 16205746722.000032, 13859145791.999966, 13381470175.949984, 14879736703.05004, 14998665477.900028, 14554124529.299913, 14064165188.999977, 16454345219.099987, 14414396454.599987]
    nordeste = [25516616248.649998, 51298393879.499626, 65913366249.900764, 70944014138.39946, 93383051984.25114, 113756875526.09918, 128144815107.44943, 105664663864.04878, 113240710260.45036, 107563475950.79945, 97857236256.44984, 90076744283.3996, 98071440364.49971, 119642031568.95035, 99530211854.09955]
    centro_oeste= [15593881546.200045, 35351377003.50005, 51475735807.7999, 55541162675.25037, 70660643210.54988, 84014507432.09967, 80732908699.05014, 72844034441.8498, 81950051104.79977, 72490147791.3001, 74269983623.24953, 70975115224.49977, 63600411669.000175, 69398887093.20052, 58032712328.69943]
    sudeste= [88947228732.00127, 153164938422.90076, 174957455242.351, 191630079901.50107, 215008370766.89807, 225540312007.19748, 251476479018.60083, 263827892392.65173, 321685525197.00024, 329146176009.1543, 314258802911.24963, 321485539677.0021, 324672361534.50226, 369415588320.59937,309545048683.50085]
    sul= [41746976239.649895, 79660059434.25047, 94660162079.25027, 103301112193.05151, 128457748727.8497, 136144221890.55074, 139877414835.59927, 136597884991.19879, 140265005333.8497, 135482464283.39957, 125893470649.19977, 115057231956.44942, 104147912454.14955, 118351984901.09967, 96604233157.95035]

    #plotando o gráfico
    mpl.figure(figsize = (25,20))
    mpl.plot(anos, norte, color = "red", label = "Norte")
    mpl.plot(anos, nordeste, color = "yellow",label = "Nordeste")
    mpl.plot(anos, centro_oeste, color = "blue",label = "Centro-Oeste")
    mpl.plot(anos, sudeste, color = "purple",label = "Sudeste")
    mpl.plot(anos, sul, color = "gray",label = "SuL")

    mpl.ylim(100000000, 400000000000)  #valores do eixo y

    mpl.title("Valor financiado por região e ano através do programa Minha Casa, Minha Vida")
    mpl.grid(True)
    mpl.box(True)
    mpl.legend()
    mpl.xlabel("Anos")
    mpl.ylabel("Valor em bilhões de reais")

    mpl.show()

def grafico_7 (numero):

    #Análise 7

    import matplotlib.pyplot as mpl
    cidades = {"São Paulo": 2.9,"João Pessoa": 2.2,"Rio de Janeiro": 2.1,"Uberlândia":1.6,"Valparaíso de Goiás": 1.39,"Ribeirão Preto": 1.31,"Goiânia": 1.23, "Feira de Santana":1.17, "Campo Grande": 1.15,"Águas Lindas de Goiás": 1.13}

    fig, ax = mpl.subplots()
    ax.bar(cidades.keys(), cidades.values())
    mpl.xticks(rotation= 15)
    mpl.box(True)
    ax.set(title="As 10 cidades que mais receberma subsídio do Governo durante 2009 e 2023", ylabel="Valor em bilhões")
    mpl.show()

'''def grafico_8 ():

def grafico_9 ():

def grafico_10 ():'''

def main():
    grafico_1 ()

main()






