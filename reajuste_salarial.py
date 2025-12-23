#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA O REAJUSTE SALARIAL DOS EMPREGADOS DE UMA EMPRESA CLT;
while True:

    valor_salario = float(input("Digite o valor do salario: "))

    if valor_salario > 1250.00:
        percentual = 0.10
        novo_salario = valor_salario + (valor_salario * percentual)

    if valor_salario <= 1250.00:
        percentual = 0.15
        novo_salario = valor_salario + (valor_salario * percentual)

    print(f"Seu novo salário com reajuste de {percentual*100}% será de: {novo_salario} reais.")