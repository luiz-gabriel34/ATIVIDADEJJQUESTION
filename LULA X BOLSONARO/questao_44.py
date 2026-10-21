def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc(65, 1.70)
print(resultado)