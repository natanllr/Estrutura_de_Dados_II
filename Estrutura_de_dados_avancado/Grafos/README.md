# Material do Estudante - Prática de Grafos

**Disciplina:** Estrutura de Dados II  
**Unidade III:** Grafos  
**Professora:** Kadidja Valéria  
**Conteúdo-base:** Capítulo 1 - Conceitos Fundamentais  
**Duração prevista:** atividades distribuídas ao longo da aula de 2 horas  

---

## 1. Objetivos da prática
Ao final das atividades, você deverá ser capaz de:
- Representar problemas utilizando grafos.
- Identificar vértices e arestas.
- Reconhecer incidência e adjacência.
- Diferenciar grafos não dirigidos e grafos dirigidos.
- Determinar ordem, tamanho e grau de vértices.
- Reconhecer laços e arestas paralelas.
- Analisar isomorfismo e subgrafos.
- Construir e conferir sequências de graus.
- Utilizar ferramentas digitais para representar grafos.

---

## 2. Orientações gerais
- Leia o enunciado antes de iniciar o desenho.
- Quando solicitado, registre primeiro os conjuntos de vértices `V` e de arestas `E`.
- Utilize círculos ou pontos para representar vértices e linhas/setas para representar arestas.
- Em grafos dirigidos, a seta deve indicar claramente a origem e o destino.
- Não entregue somente o desenho: apresente também as respostas e justificativas solicitadas.
- Quando utilizar uma plataforma digital, registre uma captura de tela ou o link da atividade.

---

## 3. Atividade 1 - Desenhando um grafo
**Proposta**  
Considere:
```text
V = {1, 2, 3, 4, 5}
E = {(1,2), (1,4), (1,5), (2,3), (3,4), (4,4)}
```

**Faça:**
- [ ] Desenhe o grafo.
- [ ] Identifique o número de vértices.
- [ ] Identifique o número de arestas.
- [ ] Determine a ordem `|V|`.
- [ ] Determine o tamanho `|E|`.
- [ ] Identifique se existe laço.
- [ ] Determine o grau de cada vértice.

> ⚠️ **Atenção:** a aresta `(4,4)` é um laço. No cálculo do grau, um laço é contado duas vezes.

**Plataformas:** Papel e lápis; Graph Online; diagrams.net; Graphviz; Google Colab com Python e NetworkX.

---

## 4. Atividade 2 - Incidência e adjacência
Utilize o grafo construído na Atividade 1.

**Faça:**
- [ ] Liste os vértices adjacentes a cada vértice.
- [ ] Informe quais arestas são incidentes em cada vértice.
- [ ] Escolha dois vértices adjacentes e explique por que são considerados vizinhos.
- [ ] Escolha dois vértices não adjacentes e justifique sua resposta.

**Registro:**

| Vértice | Vértices adjacentes | Arestas incidentes |
| :---: | :--- | :--- |
| **1** | | |
| **2** | | |
| **3** | | |
| **4** | | |
| **5** | | |

**Plataformas:** Papel; Graph Online; diagrams.net; quadro colaborativo indicado pela professora.

---

## 5. Atividade 3 - Modelagem de uma rede de amizades
Considere quatro pessoas: **João, Carolina, Maria e Marco.**

**Situação:** Crie uma pequena rede de amizades entre essas pessoas.

**Faça:**
- [ ] Defina o conjunto de vértices `V`.
- [ ] Defina o conjunto de arestas `E`.
- [ ] Desenhe o grafo correspondente.
- [ ] Informe se o grafo deve ser dirigido ou não dirigido. Justifique a escolha.
- [ ] Identifique quem possui maior grau no grafo criado.

> 💡 **Questão para reflexão:** O que os vértices e as arestas representam nesse problema?

**Plataformas:** diagrams.net; Graph Online; Canva; papel; Google Colab com NetworkX.

---

## 6. Atividade 4 - Modelagem de ruas de mão única
**Situação:** Considere um pequeno sistema urbano formado por cruzamentos e ruas de mão única.

**Faça:**
- [ ] Represente cada cruzamento ou ponto relevante por um vértice.
- [ ] Represente cada rua por uma aresta dirigida. Utilize setas para indicar o sentido permitido.
- [ ] Defina os conjuntos `V` e `E`.
- [ ] Escolha um vértice e determine:
  - Seu grau de entrada;
  - Seu grau de saída.
- [ ] Explique por que um grafo não dirigido não representa adequadamente essa situação.

**Plataformas:** diagrams.net; Graph Online; Graphviz; Google Colab com NetworkX.

---

## 7. Atividade 5 - Desafio de isomorfismo
A professora apresentará dois grafos para comparação.

**Faça:**
- [ ] Compare a quantidade de vértices.
- [ ] Compare a quantidade de arestas.
- [ ] Observe os graus dos vértices.
- [ ] Procure uma correspondência entre os vértices dos dois grafos.
- [ ] Verifique se as adjacências são preservadas.
- [ ] Registre o mapeamento encontrado.
- [ ] Conclua, justificadamente, se os grafos são isomorfos.

**Registro sugerido:**

| Vértice do grafo G | Vértice correspondente no grafo H |
| :---: | :---: |
| | |
| | |
| | |

> 📌 **Nota:** Não considere apenas a aparência dos desenhos. Grafos desenhados de formas diferentes podem apresentar a mesma estrutura.

**Plataformas:** Papel; Graph Online; diagrams.net.

---

## 8. Atividade 6 - Construindo subgrafos
A partir do grafo `G` indicado pela professora, construa dois subgrafos diferentes.

**Faça:** Para cada subgrafo:
- [ ] Informe o conjunto de vértices.
- [ ] Informe o conjunto de arestas.
- [ ] Desenhe o subgrafo.
- [ ] Confirme que seus vértices e arestas pertencem ao grafo original.

**Registro:**

**Subgrafo G1**
- `V1 = { }`
- `E1 = { }`

**Subgrafo G2**
- `V2 = { }`
- `E2 = { }`

**Plataformas:** Graph Online; diagrams.net; papel; Google Colab com NetworkX.

---

## 9. Atividade 7 - Desafio da sequência de graus
Construa um grafo simples de acordo com a sequência de graus indicada pela professora.

**Faça:**
- [ ] Crie os vértices necessários.
- [ ] Adicione as arestas progressivamente.
- [ ] Calcule o grau de cada vértice.
- [ ] Organize os graus em ordem não decrescente.
- [ ] Compare a sequência obtida com a sequência solicitada. Caso não coincida, revise as arestas.

**Registro:**

| Vértice | Grau |
| :---: | :---: |
| | |
| | |

**Sequência final de graus:** `( ______________________________ )`

**Plataformas:** Papel; Graph Online; Python/NetworkX no Google Colab.

---

## 10. Plataformas recomendadas
- **Graph Online:** Indicado para construção visual rápida de grafos e exploração das conexões.
- **diagrams.net:** Indicado para desenhar grafos, redes, mapas simplificados e modelos de situações-problema.
- **Graphviz:** Indicado para representar grafos por meio de uma descrição textual/código.
- **Google Colab + Python/NetworkX:** Indicado para relacionar os conceitos da Teoria dos Grafos à implementação computacional.
- **Canva:** Pode ser utilizado nas atividades de modelagem predominantemente visual.
- **Papel e lápis:** Continua sendo uma opção adequada para os exercícios conceituais e para os primeiros esboços.

---

## 11. Entrega das atividades
Ao final da aula, entregue um único documento contendo:
- Nome do estudante ou integrantes da dupla.
- Identificação das atividades.
- Desenhos dos grafos.
- Conjuntos `V` e `E`, quando solicitados.
- Cálculos, respostas e justificativas.
- Captura de tela ou link, quando utilizada uma plataforma digital.

---

## 12. Checklist de revisão
- [ ] Identifiquei corretamente vértices e arestas.
- [ ] Diferenciei grafo dirigido e não dirigido.
- [ ] Identifiquei incidência e adjacência.
- [ ] Calculei os graus quando solicitado.
- [ ] Considerei o laço corretamente no cálculo do grau.
- [ ] Utilizei setas nos grafos dirigidos.
- [ ] Justifiquei a análise de isomorfismo.
- [ ] Identifiquei corretamente os subgrafos.
- [ ] Conferi a sequência de graus.
- [ ] Revisei os desenhos e as justificativas.
- [ ] Registrei a plataforma utilizada.

---

## 13. Referência
> GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos e aplicações.** Blumenau: Editora IFC, 2022.  
> *Material de apoio elaborado a partir do Capítulo 1 - Conceitos Fundamentais.*
