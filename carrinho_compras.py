print("=== Carrinho de Compras ===\n")
total = 0
carrinho ={}
while True :
    item = input("Item (ou 'sair' para finalizar) : ") .strip()
    if item.lower() == 'sair':
        break
    preco = float(input(f"Preço do {item} : R$ "))
    qtd = int(input("Quantidade : "))

    subtotal = preco * qtd
    total += subtotal
    # FORMATO: carrinho[item] = {"qtd": qtd, "subtotal": subtotal}

    carrinho[item] = {
        "qtd": qtd, 
        "subtotal": subtotal
        }
    

    
print("\n=== Carrinho de Compra === ")
for item, dados in carrinho.items() :    
    print(f"{dados["qtd"]} x {item} - R$ {dados["subtotal"]:.2f}")
print(f"Total à pagar : R$ {total:.2f}")

if total > 100:
    desconto = total * 0.10
    total_com_desconto = total - desconto
    print(f"Desconto aplicado (10%): - R$ {desconto:.2f}")
    print(f"Total à pagar : R$ {total_com_desconto:.2f}")
else:
    print(f"Total à pagar : R$ {total:.2f}")