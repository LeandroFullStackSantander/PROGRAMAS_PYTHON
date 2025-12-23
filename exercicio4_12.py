#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DO CONSUMO DE ENERGIA ELÉTRICA.



while True:
    print("SEJA BEM VINDO AO SISTEMA DE FORNECIMENTO DE ENERGIA ELETRICA."'\n')
    preco_a_pagar = True
    valor_consumo = True
    consulta = str(input("Deseja obter o valor do seu consumo de energia mensal?: [S/N] ->: "))

    if consulta == "S" or consulta == "s":

        tipo_de_instalacao = str(input("Qual o seu tipo de instalação: [R]-RESIDENCIAS, [I]-INDÚSTRIAS, [C]-COMÉRCIO : "))
        if tipo_de_instalacao != "r" and tipo_de_instalacao != "R" and tipo_de_instalacao != "c" and tipo_de_instalacao != "C" and tipo_de_instalacao != "i" and tipo_de_instalacao != "I":
            print("(1) Dados Inválidos, tente novamente!!!")


        elif tipo_de_instalacao == "R" or tipo_de_instalacao == "r":
            valor_consumo = int(input("Digite o valor do consumo em kWh: "))
            if valor_consumo <= 500:
                valor_kWh = 0.40
                preco_a_pagar = valor_consumo * valor_kWh
                print("---r: ", preco_a_pagar)
            elif valor_consumo > 500:
                    valor_kWh = 0.65
                    preco_a_pagar = valor_consumo * valor_kWh
                    print("---R: ", preco_a_pagar)


        elif tipo_de_instalacao == "c" or tipo_de_instalacao == "C":
            valor_consumo = int(input("Digite o valor do consumo em kWh: "))
            if valor_consumo <= 1000:
                valor_kWh = 0.55
                preco_a_pagar = valor_consumo * valor_kWh
                print("---c:", preco_a_pagar)
            elif valor_consumo > 1000:
                    valor_kWh = 0.60
                    preco_a_pagar = valor_consumo * valor_kWh
                    print("---C: ", preco_a_pagar)


        elif tipo_de_instalacao == "I" or tipo_de_instalacao == "i":
            valor_consumo = int(input("Digite o valor do consumo em kWh: "))
            if valor_consumo <= 5000:
                valor_kWh = 0.55
                preco_a_pagar = valor_consumo * valor_kWh
                print("---i: ", preco_a_pagar)
            elif valor_consumo > 5000:
                    valor_kWh = 0.60
                    preco_a_pagar = valor_consumo * valor_kWh
                    print("---I: ", preco_a_pagar)

        print(f"Tipo de Instalação : {tipo_de_instalacao}, Valor a pagar: {preco_a_pagar:.2f} reais."'\n')

    elif consulta == "N" or consulta == "n":
            print("Encerrando o sistema."'\n')
            x = 10
            while x >= 0:
                print(x)
                x -= 1
            print("Sistema ENCERRADO."'\n')
            break

    else:
        print("Opção Inválida, tente novamente!!!")