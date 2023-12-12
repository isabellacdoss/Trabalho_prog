# Análise 5 - Avaliação da disparidade na quantidade de unidades habitacionais contratadas pelas capitais dos estados brasileiros durante os anos de 2009 a 2023


import matplotlib.pyplot as mpl

capitais = ['Rio Branco', 'Maceió','Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal','Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas', 'Brasília']
quantidade = [2138, 43661, 1313, 23495, 44351, 36163, 1528, 65139, 26211, 27098, 55108, 42587, 6088, 78360, 52136, 6238, 22768, 120772, 11631, 50905, 6975, 4519,3659, 267143, 24058, 4687587, 55586] 

mpl.figure(figsize = (15,10))
mpl.pie(quantidade, labels = capitais, autopct = '%1.1f%%', shadow = True, startangle = 95)

mpl.title("Porcentagem de financiamentos por capitail brasileira")

mpl.show()


