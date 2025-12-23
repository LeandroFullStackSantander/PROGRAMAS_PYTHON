#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE INTERROMPE A REPETIÇÃO DO WHILE SE O "ZERO" FOR DIGITADO!!!
# EXERCICIO DO LIVRO 5_14



#contador
c = 0
#acumulador
s = 0
while True:
    v = int(input("Digite um numero a somar ou '0' para sair: "))
    if v == 0:
        break
    s = s + v
    c = c + 1
print(f"Soma Total = {s}")
print(f"Contagem de numeros digitados = {c}")
print(f"Média Aritimetica = {s/c}")