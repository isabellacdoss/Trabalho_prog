# Gráficos

def grafico_1 ():

    import matplotlib.pyplot as mpl
    import numpy as np

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
    import numpy as np 

    valores = [46802.09, 151253.0, 139322.99, 205832.32, 156336.89, 217680.92, 254939.85, 219517.03, 150234.44, 124757.51, 117391.95, 201072.62, 350850.5, 240661.91, 40507.9]
    anos = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

    mpl.title('Valor subsidiado pelo Governo por ano')
    mpl.plot(anos, valores)
    mpl.plot(anos,valores, 'go')  # faz aparecer as bolinhas em cima do valor específico por ano 
    mpl.plot(anos, valores, color = "red")

    mpl.ylim(30000, 360000)  # para que os valores do gráfico fiquem nesse intervalo 
    mpl.xlim(2009,2023)

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

def grafico_8 ():
    '''Região        Ano 
Centro-Oeste  2009     325
              2010     338
              2011     350
              2012     343
              2013     364
              2014     368
              2015     382
              2016     369
              2017     350
              2018     343
              2019     326
              2020     315
              2021     300
              2022     274
              2023     294
Nordeste      2009    1023
              2010    1014
              2011     977
              2012     959
              2013    1002
              2014    1033
              2015    1046
              2016     961
              2017     914
              2018     809
              2019     797
              2020     632
              2021     631
              2022     691
              2023     683
Norte         2009     152
              2010     161
              2011     166
              2012     173
              2013     191
              2014     198
              2015     199
              2016     172
              2017     153
              2018     148
              2019     139
              2020     121
              2021     130
              2022     134
              2023     127
Sudeste       2009    1361
              2010    1363
              2011    1327
              2012    1296
              2013    1319
              2014    1326
              2015    1296
              2016    1219
              2017    1191
              2018    1090
              2019    1156
              2020    1091
              2021    1097
              2022    1085
              2023    1049
Sul           2009    1014
              2010    1075
              2011    1073
              2012    1065
              2013    1090
              2014    1081
              2015    1064
              2016     980
              2017     934
              2018     896
              2019     887
              2020     837
              2021     784
              2022     736
              2023     705'''

def grafico_9 ():
    import matplotlib.pyplot as mpl
    import numpy as np

    anos = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    norte = [725414897.8499999, 2051186392.0500002, 1112260653.900005, 2689378411.7999854, 4088328989.099965, 3890385196.949994, 3606700406.8499737, 2427659086.350007, 2551901427.59999, 3341421521.549974, 2961465200.399985, 2994608088.4499865, 2890771038.599986, 2805990904.5000086, 2246042432.399998]
    nordeste = [8838175475.849955, 19268851781.25, 10894153582.349653, 23179690733.85074, 30404388110.1003, 34293216066.900658, 35700759714.00043, 27262751659.650135, 32656114122.000782, 34563644946.15071, 27520914099.450592, 25036410741.300278, 28086165897.299835, 31874926759.949894, 25764633630.750084]
    centro_oeste = [4878445992.899983, 10788261285.0, 6678951113.099811, 15805814019.000036, 20065394146.94999, 23490491525.69983, 19851779560.499855, 15093353944.199783, 19878231439.49989, 18914074150.04995, 17370077274.899815, 15965407783.049847, 12583607758.649998, 13171215207.74996, 9628956944.99998]
    sudeste= [21017598702.300026, 39183235434.900024, 18345236543.249702, 47450452447.34978, 50298283055.25027, 48174868530.45041, 46897781370.45006, 40461697148.25028, 58160429417.09962, 67259388393.59922, 53566528548.14988, 56780171799.449615, 46508609017.34995, 41296387404.29975, 27608987053.949757]
    sul = [11966692348.799967, 23689609628.700005, 10771412181.899574, 28979535699.15003, 34815926282.99978, 32051365487.249706, 28210988352.59931, 26182376822.10025, 27760848508.650368, 29916563850.750294, 23038250226.75012, 21733383114.750034, 16382098681.050226, 15835169091.150215, 10532744155.049953]


    mpl.figure(figsize = (25,20))
    mpl.plot(anos, norte, color = "red", label = "Norte")
    mpl.plot(anos, nordeste, color = "yellow",label = "Nordeste")
    mpl.plot(anos, centro_oeste, color = "orange",label = "Centro-Oeste")
    mpl.plot(anos, sudeste, color = "green",label = "Sudeste")
    mpl.plot(anos, sul, color = "brown",label = "SuL")

    mpl.ylim(100000000, 70000000000)  #valores do eixo y

    mpl.title("Valor subsidiado por região e ano através do programa Minha Casa, Minha Vida")
    mpl.grid(True)
    mpl.box(True)
    mpl.legend()
    mpl.xlabel("Anos")
    mpl.ylabel("Valor em bilhões de reais")

    mpl.show()
   
#def grafico_10 ():



def main():

    n_analise = int(input("Digite o número da análise: \n"))

    if n_analise == 1:
        grafico_1()
    elif n_analise == 2:
        grafico_2()
    elif n_analise ==3:
        grafico_3()
    elif n_analise ==4:
        grafico_4()
    elif n_analise ==5:
        grafico_5()
    elif n_analise ==6:
        grafico_6()
    elif n_analise ==7:
        grafico_7()
    elif n_analise ==8:
        grafico_8()
    else:
        grafico_9()
    #else:
        #grafico_10()
        
main()







