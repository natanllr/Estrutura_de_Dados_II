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

# Rede do grupo: Arthur, Natan, Matheus e Ivo, cada um com 5 amigos
rede_depois = {
    "Arthur": ["Bianca", "Caio", "Daniela", "Eduardo", "Nathalia"],
    "Natan": ["Bianca", "Fernanda", "Gustavo", "Heloisa", "Icaro"],
    "Matheus": ["Fernanda", "Joana", "Kaique", "Larissa", "Murilo"],
    "Ivo": ["Joana", "Nathalia", "Otavio", "Paula", "Rafael"],

    "Bianca": ["Arthur", "Natan"],
    "Fernanda": ["Natan", "Matheus"],
    "Joana": ["Matheus", "Ivo"],
    "Nathalia": ["Ivo", "Arthur"],

    "Caio": ["Arthur"],
    "Daniela": ["Arthur"],
    "Eduardo": ["Arthur"],
    "Gustavo": ["Natan"],
    "Heloisa": ["Natan"],
    "Icaro": ["Natan"],
    "Kaique": ["Matheus"],
    "Larissa": ["Matheus"],
    "Murilo": ["Matheus"],
    "Otavio": ["Ivo"],
    "Paula": ["Ivo"],
    "Rafael": ["Ivo"]
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
