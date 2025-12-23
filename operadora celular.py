#DEVELOPER : LEANDRO CASTRO;
#LINGUAGEM: PYTHON;
#PROGRAMA QUE CALCULA VALOR DA MENSALIDADE DE UM PLANO DE CELULAR;
while True:
    plano = input("Qual o plano de celular?: ")

    if plano == "falopouco":
        minutos_plano = 100
        extra = 0.20
        preco = 50
    if plano == "falomuito":
        minutos_plano = 500
        extra = 0.15
        preco = 99
    if plano != ("falopouco") and (plano != "falomuito"):
        print("Plano Desconhecido")

    if plano == "falopouco" or plano == "falomuito":
        minutos_consumidos = int(input("Quantos minutos voce consumiu?: "))
        print("Voce vai pagar:")
        print(f"Preço do plano R${preco:10.2f}")
        suplemento = 0
        if minutos_consumidos > minutos_plano:
            suplemento = extra * (minutos_consumidos - minutos_plano)
            print(f"Suplemento: R${suplemento:10.2f}")
            print(f"Total R${preco + suplemento:10.2f}")
