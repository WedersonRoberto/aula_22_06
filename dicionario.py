def sistema_usuarios():
    # Uma lista que vai guardar vários dicionários (cada dicionário é um usuário)
    banco_usuarios = [
        {"usuario": "admin", "senha": "123", "tipo": "Administrador"},
        {"usuario": "maria", "senha": "456", "tipo": "Cliente"}
    ]
    
    while True:
        print("\n--- SISTEMA DE ACESSO ---")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Usuário")
        print("3. Listar Usuários (Apenas Admin)")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                print("\n=== LOGIN ===")
                login = input("Usuário: ").strip().lower()
                senha = input("Senha: ")
                
                usuario_encontrado = None
                
                # LOOP FOR AVANÇADO: Procurando o dicionário do usuário na lista
                for u in banco_usuarios:
                    if u["usuario"] == login and u["senha"] == senha:
                        usuario_encontrado = u
                        break # Para o loop assim que acha
                
                if usuario_encontrado:
                    print(f"\nSucesso! Login realizado como {usuario_encontrado['tipo']}.")
                else:
                    print("\nErro: Usuário ou senha incorretos.")
                    
            elif opcao == 2:
                print("\n=== CADASTRO ===")
                novo_login = input("Escolha um nome de usuário: ").strip().lower()
                
                # Validação rápida: verificar se o usuário já existe
                ja_existe = False
                for u in banco_usuarios:
                    if u["usuario"] == novo_login:
                        ja_existe = True
                        break
                        
                if ja_existe:
                    print("Erro: Este nome de usuário já está em uso!")
                    continue
                    
                nova_senha = input("Escolha uma senha: ")
                tipo_perfil = input("Tipo (Administrador/Cliente): ").strip().capitalize()
                
                # Criando o DICIONÁRIO do novo usuário
                novo_usuario = {
                    "usuario": novo_login,
                    "senha": nova_senha,
                    "tipo": tipo_perfil if tipo_perfil in ["Administrador", "Cliente"] else "Cliente"
                }
                
                # Adicionando o dicionário na nossa lista
                banco_usuarios.append(novo_usuario)
                print(f"Usuário '{novo_login}' cadastrado com sucesso!")
                
            elif opcao == 3:
                print("\n=== LISTA DE USUÁRIOS REGISTRADOS ===")
                # MANIPULAÇÃO: Usando enumerate() no for para mostrar o índice/posição do item
                for indice, u in enumerate(banco_usuarios, start=1):
                    print(f"{indice}. Nome: {u['usuario']} | Perfil: {u['tipo']}")
                    
            elif opcao == 4:
                print("\nEncerrando o sistema. Até mais!")
                break
            else:
                print("Erro: Opção inválida.")
                
        except ValueError:
            print("Erro: Digite um número válido.")

# Executa o sistema
sistema_usuarios()
