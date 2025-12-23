#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DE MULTAS NO TRANSITO;

while True:
    print("Bem vindo ao Sistema de Calculos de Multas de Transito do Brasil!",'\n')

    consulta = str(input("DESEJA REALIZAR UMA CONSULTA? DIGITE 'S' OU 'N': "))

    if consulta == "s" or consulta == "S":
        cpf = input("Digite seu CPF: ")
        if (len(cpf)) == 11:
            print("CPF VÁLIDO")
            nome = str(input("Digite seu nome: "))
            print(f"Seu nome é: {nome}, está vinculado ao cpf: {cpf}.")

            limite_velocidade = 80
            velocidade = int(input("Digite sua velocidade(km/h): "))
            if velocidade > 80:
                print("Voce foi multado")
                multa = (velocidade - limite_velocidade) * 5
                print(f"O valor da sua multa é: {multa:.2f} reais.")
                print("Mais Cuidado da Próxima Vez. Dirija com Cuidado",'\n')
            else:
                print("PARABENS! Nao existem Multas vinculadas a este cpf!",'\n')

        else:
            print("CPF INVÁLIDO")

    elif consulta == "n" or consulta == "N":
        print("Consulta Encerrada!")

    else:
        print("Entrada Inválida!")

