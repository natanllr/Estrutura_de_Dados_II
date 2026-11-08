"""
Mini-projeto ConectaUDF — Desafio em grupo
Redes sociais, grafos e cálculos (Estrutura de Dados II)

Compara a rede original (6 usuários) com a rede atualizada
(10 usuários, 5 novas amizades): graus, número de arestas,
densidade, caminhos mínimos e sugestão de amizades.
"""
from collections import deque

# ---------------------------------------------------------------
# Rede original (código-base do guia)
# ---------------------------------------------------------------
rede_original = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"],
}

# ---------------------------------------------------------------
# Rede atualizada: +4 usuários (Gabriel, Helena, Igor, Julia)
# +5 amizades: Gabriel-Ana, Gabriel-Helena, Helena-Felipe,
#              Igor-Diego, Igor-Julia
# ---------------------------------------------------------------
rede_nova = {
    "Ana": ["Bruno", "Carla", "Gabriel"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Igor"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa", "Helena"],
    "Gabriel": ["Ana", "Helena"],
    "Helena": ["Gabriel", "Felipe"],
    "Igor": ["Diego", "Julia"],
    "Julia": ["Igor"],
}


def validar(rede):
    """Confere se toda amizade é recíproca (grafo não direcionado)."""
    for usuario, amigos in rede.items():
        for amigo in amigos:
            if usuario not in rede.get(amigo, []):
                raise ValueError(f"Amizade não recíproca: {usuario} -> {amigo}")


def metricas(rede):
    """Retorna V (usuários), E (amizades) e D (densidade)."""
    n = len(rede)
    soma_graus = sum(len(a) for a in rede.values())
    E = soma_graus // 2
    D = 2 * E / (n * (n - 1))
    return n, soma_graus, E, D


def caminho_minimo(rede, origem, destino):
    """Busca em largura (BFS): menor caminho entre dois usuários."""
    fila = deque([[origem]])
    visitados = {origem}
    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]
        if atual == destino:
            return caminho
        for amigo in rede[atual]:
            if amigo not in visitados:
                visitados.add(amigo)
                fila.append(caminho + [amigo])
    return None


def sugerir_amizades(rede, usuario):
    """Sugere amigos de amigos, ordenados pelo nº de amigos em comum."""
    amigos = set(rede[usuario])
    contagem = {}
    for amigo in amigos:
        for candidato in rede[amigo]:
            if candidato != usuario and candidato not in amigos:
                contagem[candidato] = contagem.get(candidato, 0) + 1
    return sorted(contagem.items(), key=lambda x: (-x[1], x[0]))


def imprimir_tabela(original, nova):
    print(f"{'Usuário':<10}{'Grau antes':>12}{'Grau depois':>13}{'Variação':>10}")
    print("-" * 45)
    for usuario in nova:
        antes = len(original[usuario]) if usuario in original else None
        depois = len(nova[usuario])
        txt_antes = str(antes) if antes is not None else "—"
        variacao = f"+{depois - antes}" if antes is not None else "novo"
        print(f"{usuario:<10}{txt_antes:>12}{depois:>13}{variacao:>10}")


def resumo(nome, rede):
    n, soma, E, D = metricas(rede)
    graus = {u: len(a) for u, a in rede.items()}
    maior = max(graus.values())
    mais_conectados = [u for u, g in graus.items() if g == maior]
    print(f"\n== {nome} ==")
    print(f"Usuários (V): {n}")
    print(f"Soma dos graus: {soma}")
    print(f"Amizades (E = soma/2): {E}")
    print(f"Densidade D = 2E/[V(V-1)] = {2*E}/{n*(n-1)} = {D:.4f} ({D:.2%})")
    print(f"Grau médio: {soma / n:.2f}")
    print(f"Maior grau: {maior} -> {', '.join(mais_conectados)}")
    return n, E, D


if __name__ == "__main__":
    validar(rede_original)
    validar(rede_nova)

    n1, E1, D1 = resumo("Rede original", rede_original)
    n2, E2, D2 = resumo("Rede atualizada", rede_nova)

    print("\n== Comparação de graus ==")
    imprimir_tabela(rede_original, rede_nova)

    print("\n== Antes x depois ==")
    print(f"Usuários: {n1} -> {n2}")
    print(f"Amizades: {E1} -> {E2}")
    print(f"Densidade: {D1:.2%} -> {D2:.2%} (queda de {(D1 - D2) * 100:.2f} pontos percentuais)")

    print("\n== Caminhos mínimos (BFS) ==")
    for origem, destino in [("Ana", "Felipe"), ("Julia", "Gabriel"), ("Julia", "Helena")]:
        c = caminho_minimo(rede_nova, origem, destino)
        print(f"{origem} -> {destino}: {' -> '.join(c)} ({len(c) - 1} arestas)")

    print("\n== Sugestões de amizade (amigos em comum) ==")
    for usuario in ["Julia", "Gabriel", "Ana"]:
        sugestoes = sugerir_amizades(rede_nova, usuario)
        txt = ", ".join(f"{c} ({q} em comum)" for c, q in sugestoes)
        print(f"{usuario}: {txt}")
