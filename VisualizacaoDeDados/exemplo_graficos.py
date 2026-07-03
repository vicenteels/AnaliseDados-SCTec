import matplotlib.pyplot as plt

# plt.plot([1, 3, 5], [2, 6, 7])

x = ['Maçãs', 'Laranja', 'Uva']
y = [5, 3, 7]

plt.bar(x, y)

plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()