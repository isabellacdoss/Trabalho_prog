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

