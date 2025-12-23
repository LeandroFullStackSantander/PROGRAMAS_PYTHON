#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE CALCULA O TOTAL DE JUROS PAGO EM UMA DIVIDA CONFORME O PERIODO A SER PARCELADO!

print("SEJA BEM VINDO AO 'SPC' - SISTEMA DE PROTEÇÃO AO CRÉDITO")

valor_divida = int(input("Qual o valor da sua dívida? -> R$ "))
taxa_de_juros_mensal = float(input("Qual a taxa de juros? (%) -> "))
#valor_parcela = int(input("Quanto você irá pagar por parcela? -> R$ "))
periodo_meses = int(input("Você irá pagar em quantos meses? -> "))

#contadores
soma = 0
#acumuladores
total_divida = 0
juros_acumulado = 0
valor_parcela = 0

while soma <= periodo_meses:
    transforma_taxa = taxa_de_juros_mensal / 100
    juros_acumulado = valor_divida * transforma_taxa * periodo_meses
    total_divida = valor_divida + juros_acumulado
    valor_parcela = total_divida / periodo_meses
    soma = soma + 1

print(f"Você irá pagar {total_divida:.2f} reais em {periodo_meses}X.")
print(f"Ou seja, voce ira pagar {valor_parcela:.2f} reais por parcela.")
print(f"O valor pago de juros é de: {juros_acumulado:.2f} reais no acumulado.")