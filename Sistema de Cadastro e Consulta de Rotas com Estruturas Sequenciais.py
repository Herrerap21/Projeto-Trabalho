rotas = []

def cadastrar_rota():
    origem = input("Origem: ").strip().title()
    destino = input("Destino: ").strip().title()
    try:
        distancia = float(input("Distância em km: "))
    except ValueError:
        print("Distância inválida.\n")
        return

    rota = {
        "origem": origem,
        "destino": destino,
        "distancia": distancia
    }
    rotas.append(rota)
    print("Rota cadastrada com sucesso!\n")

def listar_rotas():
    if not rotas:
        print("Nenhuma rota cadastrada.\n")
        return

    print("\nRotas cadastradas:")
    print("-" * 40)
    for i, r in enumerate(rotas, 1):
        print(f"{i}. {r['origem']} -> {r['destino']}".ljust(30) + f"{r['distancia']} km")
    print("-" * 40 + "\n")

def buscar_por_origem():
    origem = input("Buscar rotas com origem em: ").strip().title()
    encontrados = [r for r in rotas if r["origem"] == origem]
    if encontrados:
        print(f"\nRotas com origem em {origem}:")
        for r in encontrados:
            print(f"- {r['origem']} -> {r['destino']} ({r['distancia']} km)")
    else:
        print("Nenhuma rota encontrada.\n")
    print()

def buscar_por_destino():
    destino = input("Buscar rotas com destino em: ").strip().title()
    encontrados = [r for r in rotas if r["destino"] == destino]
    if encontrados:
        print(f"\nRotas com destino em {destino}:")
        for r in encontrados:
            print(f"- {r['origem']} -> {r['destino']} ({r['distancia']} km)")
    else:
        print("Nenhuma rota encontrada.\n")
    print()

def exemplo_rotas_reais():
    exemplos = [
        {"origem": "Itaperuna", "destino": "Rio de Janeiro", "distancia": 228},
        {"origem": "São Paulo", "destino": "Belo Horizonte", "distancia": 586},
        {"origem": "Brasília", "destino": "Goiânia", "distancia": 209},
        {"origem": "Curitiba", "destino": "Florianópolis", "distancia": 300},
        {"origem": "Salvador", "destino": "Recife", "distancia": 839}
    ]
    rotas.extend(exemplos)
    print("Rotas de exemplo adicionadas!\n")

def menu():
    while True:
        print("1. Cadastrar nova rota")
        print("2. Listar todas as rotas")
        print("3. Buscar por origem")
        print("4. Buscar por destino")
        print("5. Inserir rotas reais de exemplo")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_rota()
        elif opcao == "2":
            listar_rotas()
        elif opcao == "3":
            buscar_por_origem()
        elif opcao == "4":
            buscar_por_destino()
        elif opcao == "5":
            exemplo_rotas_reais()
        elif opcao == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()

