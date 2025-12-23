#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DO IMPOSTO DE RENDA;

while True:
    salario = float(input("Qual o seu salário para calculo do imposto de renda: "))
    base = salario
    imposto = 0

    if base > 3000:
        imposto = imposto + ((base - 3000) * 0.35)
        base = 3000
        print(imposto)
    if base > 1000:
        imposto = imposto + ((base - 1000) * 0.20)
        print(imposto)
    print(f"Salario: R$ {salario:6.2f} Imposto a Pagar: R$ {imposto:6.2f} reais.")