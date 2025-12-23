#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE MOSTRA UMA SEQUENCIA NUMERICA COM  APENAS OS NUMEROS IMPARES

print('\n' "PROGRAMA QUE MOSTRA UMA SEQUENCIA NUMERICA COM  APENAS OS NUMEROS IMPARES, e ou MULTIPLOS DE 3!!!")

limite = int(input("Digite ate onde voce quer que vá a sequencia numerica: "))

x = 1
while x <= limite:
    #if x % 3 == 0: #utiliza essa linha para imprimir os multiplos de 3!!!!
    print(x, end=" ")
    x = x + 2
