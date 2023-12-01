import os
import pandas as pd

print(os.listdir(os.getcwd()))

dados = pd.read_csv("mcmv_financiado_fgts.csv", sep=";", encoding="ISO-8859-1")
dados.head()
dados.rename (columns = {'txt_municipio':'Município','txt_uf':'Estado','txt_regiao':'Região','num_ano_financiamento':'Ano','qtd_uh_financiadas':'Quantidade_de_unid_financiadas','vlr_financiamento':'Valor_financiado','vlr_subsidio': 'Valor_subsidiado'}, inplace = True)

media = dados.Quantidade_de_unid_financiadas.mean()

print (int(media))


