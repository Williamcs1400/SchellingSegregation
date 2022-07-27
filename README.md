## Apresentação do modelo:
O modelo de segregação de Schelling é um modelo clássico baseado em agentes, demonstrando como mesmo uma preferência leve por vizinhos semelhantes pode levar a um grau de segregação muito maior do que intuitivamente esperaríamos. O modelo consiste em agentes em uma grade quadrada, onde cada célula da grade pode conter no máximo um agente. Os agentes vêm em duas cores: vermelho e azul. Eles ficam felizes se um certo número de seus oito possíveis vizinhos são da mesma cor, e infelizes caso contrário. Agentes infelizes escolherão uma célula vazia aleatória para mover para cada etapa, até que estejam felizes. O modelo continua em execução até que não haja agentes insatisfeitos.

## Hipotese:
Os agentes têm preferência leve por vizinhos que são mais parecidos com você, eles são felizes se um certo número de seus oito possíveis vizinhos são mais parecidos com ele, e infelizes caso contrário.

## Variáveis usadas na simulação:
* **Largura:** largura da janela
* **Altura:** altura da janela
* **Densidade:** densidade de agentes no sistema
* **Fração minoritária:** fração de agentes que são minoritários
* **Hemofilia:** quantidade de agentes que devem ser similares para que outro agente seja feliz

## Como usar o programa:
* ```python run.py```

