import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Analise/titanic.csv')

survived_counts = df['survived'].value_counts()
print(survived_counts)

plt.figure(figsize=(8, 6))

plt.bar(survived_counts.index, survived_counts, color='blue')

plt.xticks([0, 1], ['Não sobreviventes', 'Sobreviventes'])
plt.title('Contagem de sobreviventes')
plt.ylabel('Contagem')

plt.show()