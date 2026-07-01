num1 = int(input("Insira o numero inicial: "))
num2 = int(input("Insira o numero final: "))

for i in range(num1, num2+1):
    if i % 2 == 0:
        print (i, end=" ")