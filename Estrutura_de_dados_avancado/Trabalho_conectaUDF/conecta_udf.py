# Projeto ConectaUDF - Desafio em grupo
# Estrutura de Dados II
# Grupo: Arthur, Natan, Matheus e Ivo

from collections import deque

# Rede antes: 6 usuarios e 8 amizades
rede_antes = {
    "Lucas": ["Sofia", "Vitor"],
    "Sofia": ["Lucas", "Vitor", "Camila"],
    "Vitor": ["Lucas", "Sofia", "Thiago"],
    "Camila": ["Sofia", "Thiago", "Yasmin"],
    "Thiago": ["Vitor", "Camila", "Yasmin"],
    "Yasmin": ["Camila", "Thiago"]
}

# Rede depois: entram Arthur, Natan, Matheus e Ivo, cada um com 5 amigos
rede_depois = {
    "Lucas": ["Sofia", "Vitor", "Arthur", "Ivo"],
    "Sofia": ["Lucas", "Vitor", "Camila", "Arthur", "Natan"],
    "Vitor": ["Lucas", "Sofia", "Thiago", "Matheus", "Ivo"],
    "Camila": ["Sofia", "Thiago", "Yasmin", "Matheus", "Ivo"],
    "Thiago": ["Vitor", "Camila", "Yasmin", "Arthur", "Natan"],
    "Yasmin": ["Camila", "Thiago", "Matheus", "Natan"],
    "Arthur": ["Lucas", "Sofia", "Thiago", "Matheus", "Ivo"],
    "Matheus": ["Camila", "Yasmin", "Vitor", "Arthur", "Natan"],
    "Natan": ["Yasmin", "Thiago", "Sofia", "Matheus", "Ivo"],
    "Ivo": ["Vitor", "Lucas", "Camila", "Arthur", "Natan"]
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


# Busca em largura (BFS) para achar o menor caminho entre dois usuarios
def caminho(rede, inicio, fim):
    fila = deque([[inicio]])
    visitados = {inicio}
    while fila:
        atual = fila.popleft()
        if atual[-1] == fim:
            return atual
        for amigo in rede[atual[-1]]:
            if amigo not in visitados:
                visitados.add(amigo)
                fila.append(atual + [amigo])
    return None


calcular(rede_antes, "ANTES")
calcular(rede_depois, "DEPOIS")

print("Caminho Lucas -> Yasmin:", " -> ".join(caminho(rede_depois, "Lucas", "Yasmin")))
print("Caminho Arthur -> Natan:", " -> ".join(caminho(rede_depois, "Arthur", "Natan")))
