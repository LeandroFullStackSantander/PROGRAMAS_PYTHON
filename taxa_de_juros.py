#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE CALCULA GANHOS COM JUROS APLICADOS NA POUPANÇA EM DETERMINADOS PERÍODOS.

print("CAIXA ECONÔMICA FEDERAL")
#taxa de juros da CEF
rendimento_mensal = 0.005
#CONTADORES
taxa_referencial = 1
soma = 1
#VARIAVEIS INICIALIZADAS COM 0 "ACUMULADORES"
deposito_atualizado = 0
periodo_meses = 0
ganhos_juros = 0
total_ganho = 0
saldo_mes = 0

deposito_inicial = int(input("Insira o valor da deposito inicial para a poupança: "'\n'))
deposito_mensal = int(input("Quanto será depositado mensalmente, conforme contrato: "'\n'))

while soma <= 10:
    taxa_referencial = taxa_referencial + 0.0015

    deposito_atualizado = (deposito_inicial + deposito_mensal)

    ganhos_juros = (deposito_atualizado * rendimento_mensal) + taxa_referencial

    total_ganho = total_ganho + ganhos_juros + deposito_atualizado

    saldo_mes = saldo_mes + total_ganho

    periodo_meses = periodo_meses + 1

    soma = soma + 1

    print(f"Rendimento Mês: {periodo_meses}, com ganhos de: {ganhos_juros:5.3f} reais.")
    print(f"SALDO MES DE JUROS: {saldo_mes:.2f} + SOMA DE DEPOSITOS: {deposito_atualizado:.2f} = SALD_ATUALIZADO:{saldo_mes + deposito_atualizado:.2f}")
    print(f"SALDO MES ATUALIZADO: {saldo_mes + deposito_atualizado:5.2f} reais."'\n')

print(f"A soma total: {saldo_mes:.2f} reais de ganhos com juros aplicados na CEF. Que totaliza {total_ganho + deposito_atualizado + saldo_mes:5.2f} reais na poupança após {soma - 1} meses. Com deposito mensal de {deposito_mensal} reais.")










