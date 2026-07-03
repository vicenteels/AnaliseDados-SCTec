import numpy as np

#Acesso a indices funciona como um array normal
arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2[1, 2])

print(arr2.shape)
print(arr2.size)
print(arr2.dtype)


print(arr1 + 10)

print(arr2 * 2)

print(np.mean(arr1)) #media

print(np.median(arr2)) #Mediana

desvio_padrao = np.std(arr1)
print(desvio_padrao)

variancia = np.var(arr1)
print(variancia)

min = np.min(arr2)
max = np.max(arr2)
print(min)
print(max)