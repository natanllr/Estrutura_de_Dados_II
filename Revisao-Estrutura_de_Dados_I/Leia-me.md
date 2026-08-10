
# 📚 Estrutura de Dados I — Algoritmos de Ordenação

Este projeto foi desenvolvido durante a disciplina de **Estrutura de Dados I**, com o objetivo de estudar e demonstrar, na prática, o funcionamento de diferentes **algoritmos de ordenação**.

O programa foi desenvolvido em **C** e permite ao usuário criar e manipular um vetor de números, além de aplicar diferentes métodos para organizar seus elementos em ordem crescente.

## 🎯 Objetivo

O principal objetivo do projeto é compreender como diferentes algoritmos podem ser utilizados para **organizar dados**, observando a lógica utilizada por cada método para comparar e reorganizar os elementos de um vetor.

O programa permite trabalhar com valores inseridos manualmente ou gerar valores de forma aleatória.

## ⚙️ Funcionalidades

O sistema possui um menu com as seguintes opções:

| Opção | Funcionalidade                           |
| ----- | ---------------------------------------- |
| `1`   | Preencher o vetor manualmente            |
| `2`   | Limpar o vetor                           |
| `3`   | Imprimir os valores do vetor             |
| `4`   | Ordenar utilizando **Bubble Sort**       |
| `5`   | Ordenar utilizando **Selection Sort**    |
| `6`   | Ordenar utilizando **Insertion Sort**    |
| `7`   | Preencher o vetor com valores aleatórios |
| `8`   | Encerrar o programa                      |

## 🔵 Bubble Sort

O **Bubble Sort** percorre o vetor comparando elementos consecutivos.

Quando o elemento atual é maior que o próximo elemento, os valores são trocados de posição. Esse processo é repetido até que todos os elementos estejam ordenados.

```text
Exemplo:

[5, 2, 8, 1]

[2, 5, 8, 1]
[2, 5, 1, 8]
[2, 1, 5, 8]
[1, 2, 5, 8]
```

## 🟢 Selection Sort

O **Selection Sort** procura elementos menores dentro da parte não ordenada do vetor e realiza a troca com o elemento que está na posição atual.

Dessa forma, a cada iteração, um elemento é colocado em sua posição correta.

```text
Exemplo:

[5, 2, 8, 1]

[1, 2, 8, 5]
[1, 2, 8, 5]
[1, 2, 5, 8]
```

## 🟡 Insertion Sort

O **Insertion Sort** organiza os elementos progressivamente.

O algoritmo seleciona um elemento e verifica sua posição em relação aos elementos anteriores, deslocando os valores quando necessário para inserir o elemento na posição correta.

```text
Exemplo:

[5, 2, 8, 1]

[2, 5, 8, 1]
[2, 5, 8, 1]
[1, 2, 5, 8]
```

## 🎲 Geração de Valores Aleatórios

O programa também possui uma função para preencher o vetor automaticamente.

A função `vetorAleatorio()` utiliza a biblioteca `stdlib.h` e a função `rand()` para gerar valores aleatórios.

Exemplo:

```text
[42, 7, 85, 13, 56, 21]
```

Isso permite testar os algoritmos de ordenação com diferentes conjuntos de dados sem precisar inserir cada valor manualmente.

## 🧹 Limpeza do Vetor

A função `limparVetor()` percorre os elementos armazenados e atribui o valor `0` para cada posição.

Essa funcionalidade permite reiniciar o vetor para realizar novos testes.

## 🖥️ Estrutura do Programa

O projeto utiliza diferentes funções para separar as responsabilidades do programa:

* `imprimeMenu()` — exibe o menu principal;
* `vetorAleatorio()` — gera valores aleatórios;
* `bubbleSort()` — executa o Bubble Sort;
* `selectionSort()` — executa o Selection Sort;
* `insertionSort()` — executa o Insertion Sort;
* `limparVetor()` — limpa os valores armazenados;
* `imprimirVetor()` — exibe os valores do vetor;
* `main()` — controla o funcionamento geral da aplicação.

## 📖 Conceitos Estudados

Através deste projeto foram trabalhados conceitos importantes de **Estrutura de Dados I**, como:

* Vetores;
* Funções;
* Estruturas de repetição;
* Estruturas condicionais;
* Manipulação de dados;
* Ordenação de elementos;
* Busca e comparação de valores;
* Troca de elementos;
* Geração de números aleatórios;
* Organização de código em funções.

## 🚀 Conclusão

Este projeto representa uma aplicação prática dos conhecimentos adquiridos em **Estrutura de Dados I**, permitindo compreender como diferentes algoritmos de ordenação trabalham sobre uma mesma estrutura de dados.

Além de apresentar o resultado final da ordenação, o projeto possibilita estudar a **lógica e o comportamento de cada algoritmo**, servindo como base para o aprofundamento dos conhecimentos em algoritmos e estruturas de dados nas próximas etapas da disciplina.

> **Estrutura de Dados I — aprendendo como organizar e manipular dados através da prática.**
