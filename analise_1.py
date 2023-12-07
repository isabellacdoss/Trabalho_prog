import matplotlib.pyplot as mpl

# dados retirados da análise da base 

anos = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
medias = [65.20, 98.25, 105.53, 106.12, 109.77, 110.21, 110.09, 105.95, 120.94, 127.24, 117.19, 121.84, 120.10, 127.05, 97.08]

mpl.figure(figsize = (15,12)) #define o tamanho da imagem 

mpl.bar(anos, medias, color = "blue", label = "Média de unidades habitacionais financiadas por ano")
mpl.box(True) # faz aparecer uma margem ao redor do gráfico
mpl.title("Média de Unidades Habitacionais financiadas por ano pelo programa Minha Casa, Minha Vida")
mpl.legend()

mpl.show() #usado para gerar o gráfico



