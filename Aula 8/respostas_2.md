# Análise MC/DC: embarque

## a) Regra e pares independentes

A especificação exige cartão e documento válidos e que a pessoa tenha sido chamada ou possua prioridade:

pares_independentes(decisao, n) enumera as $2^n$ linhas da tabela-verdade, compara linhas que diferem somente em uma condição e guarda o par se a decisão mudar. Os índices são baseados na ordem lexicográfica da tabela, começando em zero, com False antes de True.

| Índice | A | B | C | D | Resultado da regra |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | F | F | F | F | F |
| 1 | F | F | F | V | F |
| 2 | F | F | V | F | F |
| 3 | F | F | V | V | F |
| 4 | F | V | F | F | F |
| 5 | F | V | F | V | F |
| 6 | F | V | V | F | F |
| 7 | F | V | V | V | F |
| 8 | V | F | F | F | F |
| 9 | V | F | F | V | F |
| 10 | V | F | V | F | F |
| 11 | V | F | V | V | F |
| 12 | V | V | F | F | F |
| 13 | V | V | F | V | V |
| 14 | V | V | V | F | V |
| 15 | V | V | V | V | V |

## b) Quantidade de pares e conjuntos mínimos

- $A$: 3 pares: (5, 13), (6, 14) e (7, 15). Para $A$ alterar o resultado, $B$ deve ser V e pelo menos uma entre $C$ e $D$ deve ser V.
- $B$: 3 pares: (9, 13), (10, 14) e (11, 15). Simetricamente, $A$ deve ser V e pelo menos uma entre $C$ e $D$ deve ser V.
- $C$: 1 par: (12, 14). $A=B=V$ e $D=F$ fazem $C$ decisivo.
- $D$: 1 par: (12, 13). $A=B=V$ e $C=F$ fazem $D$ decisivo.

Há quatro conjuntos MC/DC mínimos, cada um com cinco casos:

| Conjunto | Índices das linhas | Encontra o defeito? |
|---|---|:---:|
| M1 | 12, 14, 13, 6, 10 | Não |
| M2 | 12, 14, 13, 6, 9 | Sim |
| M3 | 12, 14, 13, 5, 10 | Sim |
| M4 | 12, 14, 13, 5, 9 | Sim |

As linhas 12, 13 e 14 são necessárias para os pares únicos de $C$ e $D$. Para cobrir $A$, é preciso adicionar o par (6, 14) ou (5, 13); para $B$, o par (10, 14) ou (9, 13). As duas escolhas são independentes, portanto há $2\times2=4$ conjuntos. Cinco casos são o mínimo: os pares de $C$ e $D$ conectam três linhas, e a cobertura de $A$ e $B$ requer mais dois casos distintos.

## c) Testes com todos V e todos F

Com (V, V, V, V), a regra e a função defeituosa retornam V. Com (F, F, F, F), ambas retornam F. Portanto, esses dois testes não expõem a diferença. O código disponível em embarque.py expressa as decisões como expressões booleanas de curto-circuito; medir somente os casos extremos não equivale a cobrir cada efeito independente das quatro condições.

A medição isolada executou os dois casos com sucesso e exibiu 100% de cobertura, mas contou zero ramos. As expressões and/or são cobertas como linhas, sem decisões de ramo registradas pelo coverage.py nessa função. Portanto, esse 100% não comprova avaliação independente das condições nem ausência do defeito.

## d) Detecção do defeito e correção

O Python interpreta a expressão original sem parênteses como (A and B and C) or D, pois and tem precedência sobre or. A especificação, porém, é A and B and (C or D). Com $D=V$, a implementação defeituosa pode aprovar mesmo quando cartão ou documento é falso.

M1 não contém caso com $D=V$ e $A\land B=F$, então não detecta o problema. M2 contém a linha 9 (V, F, F, V); M3 contém a linha 5 (F, V, F, V); M4 contém ambas. Nessas linhas, a função defeituosa retorna V por causa de D, mas a regra retorna F. Assim, M2, M3 e M4 detectam o defeito.

O MCC (Multiple Condition Coverage) exige todas as $2^4=16$ combinações. Ele necessariamente inclui as linhas 5 e 9, logo sempre revela essa divergência.

A correção é agrupar a alternativa com parênteses: cartao and documento and (grupo_chamado or prioridade). A função pode_embarcar em embarque.py já usa essa expressão; pode_embarcar_defeituosa preserva a expressão original para comparação nos testes.
