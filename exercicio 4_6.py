#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DO PREÇO A PAGAR PELO KM PERCORRIDO EM VIAGENS;

parcelar = True

while True:
    print("SEJA BEM VINDO AO NOSSO SISTEMA DE COMPRA DE PASSAGENS!!!"'\n')
    distancia_a_percorrer = float(input("Qual a distância deseja VIAJAR?(km): "'\n'))
    print("NOTA: O valor da passagem é calculado de acordo com a distancia."'\n')

    if distancia_a_percorrer <= 200:
        valor_por_km = 0.50
        valor_a_pagar = valor_por_km * distancia_a_percorrer

    if distancia_a_percorrer > 200:
        valor_por_km = 0.45
        valor_a_pagar = valor_por_km * distancia_a_percorrer

    print(f"O Valor a ser cobrado é de: R${valor_a_pagar:6.2f} reais."'\n')

    compra = str(input("Deseja continuar? (S/N): "))
    if compra == 's' or compra == 'S':
        pagamento = int(input("Qual a forma de pagamento?: Digite 1 para CARTAO DE CRÉDITO OU 2 para PIX: "))

        if pagamento == 1:
           parcelar = str(input("Deseja parcelar?(S/N): "))
        if parcelar == 's' or parcelar == 'S':
           parcelas = int(input("Qual a quantidade de parcelas?: "))
           valor_a_pagar = (valor_a_pagar / parcelas)
           print(f"O valor fica em {parcelas} parcelas de : R${valor_a_pagar:6.2f} reais."'\n')
           print("Obrigado pela compra e confiança em nossos serviços!"'\n')

        else:
            print(f"O valor a ser pago A VISTA NO CARTÃO é de: R${valor_a_pagar:6.2f} reais."'\n')

        if pagamento == 2:
            print("O QR CODE SERÁ GERADO NA TELA DO COMPUTADOR, ESCANEIE PARA REALIZAR O PAGAMENTO!"'\n')
            print("Obrigado pela compra e confiança em nossos serviços!"'\n')

    if compra == 'n' or compra == 'N':
        print("Obrigado, desculpe se lhe decepcionamos em alguma coisa, prometo que na próxima seremos melhores amigos."'\n')

        final = str(input("Deseja finalizar?(S/N): "))
        if final == 's' or final == 'S':
            print("Finalizado com sucesso!"'\n')
        else:
            print("Algo mais? Faça uma nova consulta!"'\n')
