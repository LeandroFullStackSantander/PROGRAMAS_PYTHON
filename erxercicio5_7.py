#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE IMPRIME OS VALORES DE TABUADA ESCOLHIDO PELO USUARIO DIGITANDO INICIO E FIM!!!


print('\n'"PROGRAMA QUE IMPRIME OS VALORES DE TABUADA ESCOLHIDO PELO USUARIO DIGITANDO INICIO E FIM!!!")

valor_inicio = int(input("Valor de inicio: "))
ate_onde = int(input("Valor final: "))
n = int(input("Tabuada de: "))
operacao = str(input("Qual operacao: "))

x = valor_inicio

while valor_inicio <= ate_onde:
    if operacao == "*":
        print(f"{n} {operacao} {valor_inicio} = {n * valor_inicio}")
    valor_inicio += 1
