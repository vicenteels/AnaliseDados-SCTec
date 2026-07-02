def dividir(a, b):
    r = 0
    try:
        r = a / b
        return print(r)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")
    except:
        print("Erro inesperaod, verifique se os dados inseridos são dois numeros validos")

dividir(4, 2)