# Projeto ConectaUDF - Desafio em grupo
# Estrutura de Dados II

# Rede original
rede_antes = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"]
}

# Rede com os 4 usuarios novos e as 5 amizades novas
rede_depois = {
    "Ana": ["Bruno", "Carla", "Gabriel"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Igor"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa", "Helena"],
    "Gabriel": ["Ana", "Helena"],
    "Helena": ["Gabriel", "Felipe"],
    "Igor": ["Diego", "Julia"],
    "Julia": ["Igor"]
}


def calcular(rede, nome):
    print("----", nome, "----")
    for usuario in rede:
        print(usuario, "- grau:", len(rede[usuario]))

    n = len(rede)
    soma_graus = sum(len(a) for a in rede.values())
    E = soma_graus // 2
    D = 2 * E / (n * (n - 1))

    print("Usuarios:", n)
    print("Soma dos graus:", soma_graus)
    print("Amizades:", E)
    print(f"Densidade: {D:.2%}")
    print()


calcular(rede_antes, "ANTES")
calcular(rede_depois, "DEPOIS")
