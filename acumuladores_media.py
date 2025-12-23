#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PRINCIPIOS DE ACUMULADORES COM APLICAÇÃO NO CALCULO DE MÉDIAS!

x = 1
soma = 0

while x <= 5:
    n = int(input(f"Passo:{x}, Digite um numero inteiro: "))
    soma += n #soma = soma + n
    x += 1 #x = x + 1
print(f"Média: {soma/5:5.2f}")