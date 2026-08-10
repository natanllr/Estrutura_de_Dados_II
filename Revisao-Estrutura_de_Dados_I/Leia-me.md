# Estrutura de Dados I - Algoritmos de Ordenação

Este projeto foi desenvolvido durante a matéria de **Estrutura de Dados I**. A ideia foi criar um programa simples para entender na prática como funcionam alguns métodos de ordenação.

O programa trabalha com um vetor de até **1000 valores** e permite inserir números manualmente ou gerar valores aleatórios. Depois disso, é possível ordenar os valores utilizando diferentes métodos.

## Funcionalidades

O programa possui um menu com as seguintes opções:

* **1 - Preencher o Vetor:** permite inserir os valores manualmente.
* **2 - Limpar o Vetor:** zera os valores armazenados.
* **3 - Imprimir o Vetor:** mostra os valores presentes no vetor.
* **4 - Bubble Sort:** ordena o vetor utilizando o método Bubble Sort.
* **5 - Selection Sort:** ordena utilizando Selection Sort.
* **6 - Insertion Sort:** ordena utilizando Insertion Sort.
* **7 - Preencher Vetor Aleatoriamente:** gera valores aleatórios para o vetor.
* **8 - Sair:** encerra o programa.

## Métodos de Ordenação

### Bubble Sort

Compara os valores que estão lado a lado. Se o valor da esquerda for maior que o da direita, eles são trocados.

O processo continua até que o vetor esteja completamente ordenado.

### Selection Sort

Percorre o vetor procurando valores menores e realiza as trocas necessárias para colocar os elementos em ordem crescente.

### Insertion Sort

Pega os elementos um por um e os coloca na posição correta em relação aos elementos que já foram ordenados.

## Exemplo

Um vetor pode começar dessa forma:

```text
64, 25, 12, 22, 11, 90
```

Depois de aplicar um dos métodos de ordenação:

```text
11, 12, 22, 25, 64, 90
```

## O que foi utilizado

O projeto foi feito em **C** e utiliza principalmente:

* Vetores;
* Funções;
* `for` e `while`;
* Estruturas condicionais;
* Manipulação de valores;
* `rand()` para geração de números aleatórios;
* Bubble Sort;
* Selection Sort;
* Insertion Sort.

## Sobre o projeto

O objetivo principal foi colocar em prática o conteúdo estudado em **Estrutura de Dados I**, principalmente a parte de ordenação de dados.

A partir desse projeto, pude entender melhor como cada método funciona e como diferentes algoritmos podem chegar ao mesmo resultado utilizando estratégias diferentes.

Este projeto também serve como base para os conteúdos que serão estudados em **Estrutura de Dados II**.
