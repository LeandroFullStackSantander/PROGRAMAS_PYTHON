#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE REALIZA OPERAÇOES MATEMATICAS SOLICITADAS PELO USUARIO, OU SEJA, CALCULADORA;

while True:

    print("Seja bem vindo ao sistema nacional de calculadora espacial de alta precisão"'\n')

    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    operacao = str(input("Digite a operação: (+), (-), (*), (/), (//), (**): "))
    if operacao == "+":
        resultado = n1 + n2
        print(f"O valor da operação é: {n1} + {n2} = {resultado}")
    elif operacao == "-":
        resultado = n1 - n2
        print(f"O valor da operação é: {n1} - {n2} = {resultado}")
    elif operacao == "*":
        resultado = n1 * n2
        print(f"O valor da operação é: {n1} * {n2} = {resultado}")
    elif operacao == "/":
        resultado = n1 / n2
        print(f"O valor da operação é: {n1} / {n2} = {resultado}")
    elif operacao == "//":
        resultado = n1 // n2
        print(f"O valor da operação é: {n1} // {n2} = {resultado}")
    elif operacao == "**":
        resultado = n1 ** n2
        print(f"O valor da operação é: {n1} ** {n2} = {resultado}")
    else:
        print("Operação inválida!")

