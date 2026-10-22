# Análise de All-Uses: preco_final

## a) Definições, usos e pares DU

Os números de linha abaixo referem-se ao código do enunciado. Um c-use é um uso em uma expressão computacional; um p-use é um uso em uma condição de predicado.

| Variável | Linha | Tipo | Ocorrência |
|---|---:|---|---|
| `total` | 2 | definição | `total = preco` |
| `total` | 5 | c-use e definição | uso de `total` no lado direito; nova atribuição no lado esquerdo |
| `total` | 6 | p-use | condição `total < 50` |
| `total` | 7 | definição | `total = 50` |
| `total` | 8 | c-use | valor retornado |
| `desconto` | 4 | definição | `desconto = preco * 0.2` |
| `desconto` | 5 | c-use | subtraído na expressão que atualiza `total` |

Pares DU factíveis para total:

| Definição | Uso | Condição para o caminho definição-uso |
|---:|---:|---|
| 2 | 5 (c-use) | `vip` verdadeiro |
| 2 | 6 (p-use) | `vip` falso; a definição da linha 2 chega à condição |
| 2 | 8 (c-use) | `vip` falso e `total >= 50` |
| 5 | 6 (p-use) | `vip` verdadeiro |
| 5 | 8 (c-use) | `vip` verdadeiro e o `total` atualizado é `>= 50` |
| 7 | 8 (c-use) | `total < 50` na linha 6, então o valor é substituído por 50 |

Para desconto, há o par DU $(4,5)$: a linha 4 define desconto e a linha 5 o usa. Não existe caminho que pule a definição e chegue ao uso, pois ambos estão no mesmo ramo if vip.

## b) Pares que a suíte anterior não percorria

Antes deste exercício, os testes existentes cobriam forca e embarque, mas não chamavam preco_final. Portanto, não percorriam nenhum dos seis pares DU de total nem o par $(4,5)$ de desconto.

Os casos adicionados em test_preco.py exercitam todos eles: preço 100 sem VIP percorre $(2,6)$ e $(2,8)$; preço 40 sem VIP percorre $(2,6)$ e $(7,8)$; preço 200 com VIP percorre $(2,5)$, $(4,5)$, $(5,6)$ e $(5,8)$; preço 40 com VIP percorre $(2,5)$, $(4,5)$, $(5,6)$ e $(7,8)$.

## c) Completar All-Uses e explicar o defeito

All-Uses exige que cada definição alcance pelo menos um caminho definição-uso para cada uso alcançável sem outra definição da variável no caminho. Para completar a cobertura, é preciso incluir pelo menos um caso sem VIP, para os usos de total alcançados diretamente a partir da linha 2; um caso com VIP, para os usos da definição da linha 5 e para o uso de desconto; além de entradas acima e abaixo do limite de 50, para exercitar as duas saídas do predicado da linha 6 e a definição da linha 7.

O ramo VIP do enunciado calcula total * 0.8 - desconto. Como total começa igual ao preço e desconto já vale 20% do preço, essa expressão subtrai o desconto duas vezes: o resultado fica em 60% do preço, em vez de 80%. Por exemplo, com preço 200 e VIP, o resultado do código original é 120, mas o esperado é 160. O caso VIP com preço 40 não revela a divergência porque os dois resultados acabam elevados para o piso de 50.

A suíte anterior não viu o defeito porque sequer executava a função. Mesmo uma suíte que só testasse preços abaixo do limite poderia mascará-lo pelo piso mínimo. O caso VIP de preço 200 foi incluído para observar o valor calculado sem essa interferência.

Uma medição direcionada confirma a diferença: os casos preço 100 sem VIP, preço 40 sem VIP e preço 40 com VIP passam e atingem 100% de ramos (4/4) em preco_final, mas omitem o par DU (5,8), pois não há caso VIP cujo total após o desconto permaneça acima de 50. O caso VIP de preço 200 cobre esse par e revela a fórmula incorreta do enunciado.

## d) Correção e execução

A fórmula deve subtrair o desconto uma única vez: total = total - desconto. A função corrigida está em src/preco.py; os testes de cobertura dos pares DU estão em test/test_preco.py.

Na execução completa, passaram 20 testes. O relatório mostrou preco.py com 100% de cobertura e 4/4 ramos. O subconjunto de três casos acima também chegou a 100% de ramos, mas não completou All-Uses.
