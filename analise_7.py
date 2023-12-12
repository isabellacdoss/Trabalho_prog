#Análise 7

import matplotlib.pyplot as mpl
cidades = {"São Paulo": 2.9,"João Pessoa": 2.2,"Rio de Janeiro": 2.1,"Uberlândia":1.6,"Valparaíso de Goiás": 1.39,"Ribeirão Preto": 1.31,"Goiânia": 1.23, "Feira de Santana":1.17, "Campo Grande": 1.15,"Águas Lindas de Goiás": 1.13}

fig, ax = mpl.subplots()
ax.bar(cidades.keys(), cidades.values())
mpl.xticks(rotation= 15)
mpl.box(True)
ax.set(title="As 10 cidades que mais receberma subsídio do Governo durante 2009 e 2023", ylabel="Valor em bilhões")
mpl.show()

