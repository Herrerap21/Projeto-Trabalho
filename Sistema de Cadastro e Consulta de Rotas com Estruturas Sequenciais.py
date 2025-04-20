rotas = []


def cadastrar_rota():
    origem = input("Cidade de origem: ").strip().title()
    destino = input("Cidade de destino: ").strip().title()
    try:
        distancia = float(input("Distância entre as cidades (km): "))
    except ValueError:
        print("Distância inválida.")
        return

    rota = {"origem": origem, "destino": destino, "distancia": distancia}
    rotas.append(rota)
    print("Rota cadastrada com sucesso!\n")


def listar_rotas():
    if not rotas:
        print("Nenhuma rota cadastrada.\n")
        return

    print("\nRotas cadastradas:")
    for i, r in enumerate(rotas, start=1):
        print(f"{i}. {r['origem']} -> {r['destino']} : {r['distancia']} km")
    print()


def buscar_rota():
    origem = input("Origem: ").strip().title()
    destino = input("Destino: ").strip().title()

    for r in rotas:
        if r["origem"] == origem and r["destino"] == destino:
            print(
                f"Rota encontrada: {r['origem']} -> {r['destino']} ({r['distancia']} km)\n")
            return
    print("Rota não encontrada.\n")


def menu():
    while True:
        print("1. Cadastrar rota")
        print("2. Listar rotas")
        print("3. Buscar rota")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_rota()
        elif opcao == "2":
            listar_rotas()
        elif opcao == "3":
            buscar_rota()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
