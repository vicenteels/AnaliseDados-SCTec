import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('Analise/titanic.csv')

print(df.head())

print(df.info())

print(df.describe())

print(df.dtypes)

#Filtro
print(df[df['age'] >= 10].head())

#linhas duplicadas
duplicateRows = df[df.duplicated()]
print(duplicateRows)
print(len(duplicateRows))

df.drop_duplicates(keep='last', inplace=True)

#Valores nulos
df.dropna(subset='deck', inplace=True) #exclui linhas com valor nulo na coluna específica

df.replace(np.nan, '0', inplace=True) #substitui valores nulos por valor específico

#Renomear colunas
df = df.rename(columns={'sex': 'Genero'})

sorted_df = df.sort_values(by='Genero', ascending=True)
print(sorted_df)