#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DO EMPRÉSTIMO BANCARIO PARA COMPRA DE IMÓVEIS;

#CONNTINUUUAAAAAAAAAAAAAAAA.........

while True:

    print("SIMULAÇÃO DE EMPRÉSTIMO BANCÁRIO NO BANCO LCM Ltda!"'\n')

    imovel = int(input("Que tipo de imóvel deseja simular? [1]-APARTAMENTO [2]-CASA: "))
    if imovel == 1:
        imovel = APARTAMENTO
        print(f"Ok! {imovel} selecionado!")
    elif imovel == 2:
        imovel = CASA
        print(f"Ok! {imovel} selecionado!")

    valor_imovel = float(input("Qual valor do imóvel: "))
    valor_salario = float(input("Digite o valor do seu salário bruto: "))
    anos_a_pagar = int(input("Em Quantos anos deseja pagar: "))

    valor_prestacao = valor_imovel / (anos_a_pagar * 12)

    if imovel == 1 or imovel == 2:
            if valor_prestacao < valor_salario * 0.3:
                    print("Emprestimo Aprovado!"'\n')
                    print(f"O valor da prestação fica {anos_a_pagar * 12} vezes de: {valor_prestacao:.2f} reais."'\n')
            else:
                if valor_prestacao >= valor_salario * 0.3:
                    print("Emprestimo Não Aprovado!"'\n'"Você não atende aos requesitos!"'\n')

    else:
        print("Entrada não reconhecida!")