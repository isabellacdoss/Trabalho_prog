import os
import pandas as pd

print(os.listdir(os.getcwd()))

dados = pd.read_csv("mcmv_financiado_fgts.csv", sep=";", encoding="ISO-8859-1")
print(dados.head())

#dados.rename (columns = {'txt_municipio': 'Município', 'txt_uf' : 'Estado'}, inplace = True)
#print (dados)
