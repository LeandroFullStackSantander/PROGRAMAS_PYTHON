#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA CONTA PONTOS CONFORME ACERTA A RESPOSTA DE CADA QUESTÃO e estuda principios de acumuladores!

n = 1
soma = 0
while n <= 20:
    x = int(input(f"Digite o {n} número: "))
    soma = soma + x
    n = n + 1

print(f"Soma: {soma}")