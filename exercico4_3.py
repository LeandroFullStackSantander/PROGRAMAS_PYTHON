#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE LÊ TRES NUMEROS E IMPRIME O MAIOR E O MENOR;

while True:

    x1 = int(input("Digite o primeiro valor: "))
    x2 = int(input("Digite o segundo valor: "))
    x3 = int(input("Digite o terceiro valor: "))

    # X1 SENDO MAIOR E X3 MENOR
    if x1 > x2:
        maior = x1
    if maior > x3:
        print("O maior é:",x1)
    if x3 < x2:
        menor = x3
    if menor < x1:
        print("O menor é:", x3)

    #X3 SENDO MAIOR E X1 SENDO MENOR
    if x3 > x2:
        maior = x3
    if maior > x1:
        print("O maior é:", x3)
    if x1 < x2:
        menor = x1
    if menor < x3:
        print("O menor é:", x1)

    #X2 SENDO MAIOR E X1 SENDO MENOR
    if x2 > x1:
        maior = x2
    if maior > x3:
        print("O maior é:", x2)
    if x1 < x2:
        menor = x1
    if menor < x3:
        print("O menor é:", x1)