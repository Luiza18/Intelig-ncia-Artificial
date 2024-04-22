# Projeto de Inteligência Artificial: Busca de Caminho em Labirinto 🤖🧩

Este projeto foi desenvolvido como parte de um curso de Inteligência Artificial na faculdade. O objetivo é encontrar o caminho de um labirinto utilizando diferentes algoritmos de busca.

## Descrição do Desafio 📝

O desafio consiste em criar um programa capaz de encontrar o caminho válido em um labirinto, representado por uma matriz. O labirinto contém obstáculos que devem ser contornados para chegar do ponto de início ao ponto de destino.

## Algoritmos Utilizados 🚀

### Busca em Profundidade 🔍

A busca em profundidade é um algoritmo de busca não informada que explora o máximo possível em uma ramificação antes de retroceder. Isso significa que ele segue um caminho até que não haja mais nós a serem explorados nessa direção e, em seguida, retrocede para explorar outras ramificações. Esse algoritmo utiliza uma estrutura de pilha para armazenar os nós a serem explorados, o que garante que ele explore profundamente em uma direção antes de considerar outras alternativas.

### Busca em Amplitude 🌐

A busca em amplitude é outro algoritmo de busca não informada que explora todos os nós em um mesmo nível antes de avançar para o próximo nível. Em outras palavras, ele expande todos os nós vizinhos de um nível antes de passar para o próximo nível. Esse algoritmo utiliza uma estrutura de fila para armazenar os nós a serem explorados, garantindo que ele explore amplamente todas as possibilidades em cada nível antes de avançar para o próximo.

### Busca de Custo Uniforme 💰

A busca de custo uniforme é um algoritmo de busca informada que expande o nó com o menor custo acumulado até o momento. Ele utiliza uma estrutura de fila de prioridade para explorar os nós de forma ordenada pelo custo acumulado. Esse algoritmo é ideal para encontrar o caminho mais curto em termos de custo total, mesmo que o custo de movimentação entre os nós não seja uniforme.

### Busca Gulosa (Greedy Search) 🤔

A busca gulosa é um algoritmo de busca informada que escolhe o caminho que parece ser o mais próximo do objetivo com base em uma heurística. A heurística é uma função que fornece uma estimativa de quão promissor é cada nó em termos de alcançar o objetivo. Esse algoritmo prioriza os nós que têm a menor estimativa de custo para o objetivo, mas pode não garantir a solução mais eficiente em termos de custo total.

### A* (A Star) ⭐

O algoritmo A* é um dos mais populares algoritmos de busca informada. Ele combina a busca em amplitude com a busca gulosa, utilizando tanto o custo atual quanto uma heurística para determinar o próximo nó a ser explorado. O A* é eficiente e garante encontrar o caminho mais curto, desde que a heurística seja admissível (não superestime o custo) e monotônica (o custo de um nó nunca é menor que o custo do seu antecessor mais o custo para alcançá-lo).

## Executando o Projeto ▶️

Para baixar e executar o projeto, siga as instruções abaixo:

1. Clone o repositório em sua máquina local:
2. Navegue até o diretório do projeto:
3. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv env 
````
4. Ative o ambiente virtual (caso tenha criado):

    -No Windows
   ```bash
        .\env\Scripts\activate
    ````
    -No Linux/Mac
    ```bash
        source env/bin/activate
    ````
5. Instale as dependências do projeto a partir do arquivo requirements.txt:
    ```bash
    pip install -r requirements.txt
     ````
