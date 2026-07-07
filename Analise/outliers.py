import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Analise/titanic.csv')

sns.boxplot(x=df['age'])

plt.show()