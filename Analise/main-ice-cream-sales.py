import pandas as pd

df = pd.read_csv('Analise/Ice Cream Sales.csv')

sorted_df = df.sort_values(by='Temperature', ascending=True)

print(sorted_df['Temperature'])