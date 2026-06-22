estoque = {
    "banana": 30,
    "maçã": 25,
    "morango": 12,
    "melancia": 5,
    "uva": 15,
    "laranja": 50,
    "abacaxi": 8,
    "manga": 20,
    "abacate": 10,
    "limão": 40,
    "pera": 18,
    "mamão": 7,
    "pêssego": 14,
    "kiwi": 22,
    "cereja": 60
}
while True:
    print("Verificação do estoque.")
    print("Opção 1 : Verificar no estoque .")
    print("Opção 2 : Sair")

    opcao = input("Escolha uma opção (1 ou 2 ):").strip()

    if opcao == "1":
        busca = input("Digite a fruta que deseja verificar : ").strip().lower()
        if busca in estoque:
            quantidade = estoque[busca]
            print(f"\n Fruta encontrada : {busca.capitalize()}")
            print(f"Quantidade atual : {quantidade} unidades")
            if quantidade > 15 :
                print("Estoque ok. ")
            elif 1<= quantidade<=15:
                print("Estoque necessitanto de reposição .")
            elif quantidade == 0 :
                print("Sem estoque")
        else:
            print("Fruta não encontrada no estoque.")
    elif opcao == "2":
        print("Saindo do sistema de estoque. ")  

        print("Estoque atualizado.") 
        break     
                   