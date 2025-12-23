#DEVELOPER: LEANDRO CASTRO
#LINGUAGEM: PYTHON
#PROGRAMA QUE CONTROLA UMA MAQUINA DE REGISTROS!!!


print("MAQUINA REGISTRADORA DE SUPERMERCADO LCM Ltda.")
print("SEJA BEM VINDO E BOAS COMPRAS.")

#acumulador
preco_item = 0
somatorio_preco = 0

#contador
count = 0

while True:
    code_produto = str(input("Digite o código do produto: "))

    if code_produto == '0':
        break
    elif code_produto == '1':
        preco_item = 0.50
        print(f"Preço do item: {preco_item} centavos.")
    elif code_produto == '2':
        preco_item = 1.00
        print(f"Preço do item: {preco_item} real.")
    elif code_produto == '3':
        preco_item = 4.00
        print(f"Preço do item: {preco_item} reais")
    elif code_produto == '5':
        preco_item = 7.00
        print(f"Preço do item: {preco_item} reais.")
    elif code_produto == '9':
        preco_item = 8.00
        print(f"Preço do item: {preco_item} reais.")
    else:
        print("Código Inválido! Tente novamente.")

    count += 1
    somatorio_preco = somatorio_preco + preco_item

print(f"Quantidade de itens: {count}")
print(f"Subtotal: {somatorio_preco} reais")
