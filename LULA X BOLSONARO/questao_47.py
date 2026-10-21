try:
    valor = int(input("Digite um número: "))
    res = 10 / valor
except ZeroDivisionError:
    print("Ocorreu um erro de divisão por zero")
except ValueError:
    print("Ocorreu um erro de valor inválido")