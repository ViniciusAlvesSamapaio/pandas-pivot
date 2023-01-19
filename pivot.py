import pandas as pd 
import numpy as np

#dados pivot
dias = pd.date_range(start='20230202', periods=12)

pessoa = ['vinicius', 'marcos', 'roger']
np.random.choice(pessoa)

nome = []
gasto = []
for i in range(12):
        nome.append(np.random.choice(pessoa))
        gasto.append(np.round(np.random.rand()*100, 2))
#print(gasto)
#print(nome)
df = pd.DataFrame({"dias":dias, "nome":nome, "gasto":gasto})

print(df)

#pivot

df = df.pivot( index = 'dias',columns = 'nome', values = 'gasto' )

print(df)

#dados pivot table

vendas = [2, 6, 9, 3, 6]

data = pd.date_range("20230202","20230202", periods=5)

vendedor = ["vinicius", "guilherme", "robson", "vinicius", "guilherme"]

df2 = pd.DataFrame({"vendas":vendas, "data":data, "vendedor":vendedor}) #dataframe usado para testar o pivot table

#pivot table

df2 = pd.pivot_table(df2, values='vendas', columns='vendedor', index='data', aggfunc="sum")

print(df2)
