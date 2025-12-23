#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE IMPRIME OS VALORES DE TABUADA ESCOLHIDO PELO USUARIO!!!


print('\n'"PROGRAMA QUE IMPRIME OS VALORES DE TABUADA ESCOLHIDO PELO USUARIO!!!")

n = int(input("Tabuada de: "))
operacao = str(input("Qual operacao: "))


x = 1
while x <= 10:
    if operacao == "*":
        print(f"{n} {operacao} {x} = {n * x}")
    x += 1
