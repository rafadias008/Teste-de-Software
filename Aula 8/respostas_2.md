# Análise MC/DC: embarque

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

A medição isolada executou os dois casos com sucesso e exibiu 100% de cobertura, mas contou zero ramos. As expressões and/or são cobertas como linhas, sem decisões de ramo registradas pelo coverage.py nessa função. Portanto, esse 100% não comprova avaliação independente das condições nem ausência do defeito.

## d) Detecção do defeito e correção

O Python interpreta a expressão original sem parênteses como (A and B and C) or D, pois and tem precedência sobre or. A especificação, porém, é A and B and (C or D). Com $D=V$, a implementação defeituosa pode aprovar mesmo quando cartão ou documento é falso.

M1 não contém caso com $D=V$ e $A\land B=F$, então não detecta o problema. M2 contém a linha 9 (V, F, F, V); M3 contém a linha 5 (F, V, F, V); M4 contém ambas. Nessas linhas, a função defeituosa retorna V por causa de D, mas a regra retorna F. Assim, M2, M3 e M4 detectam o defeito.

O MCC (Multiple Condition Coverage) exige todas as $2^4=16$ combinações. Ele necessariamente inclui as linhas 5 e 9, logo sempre revela essa divergência.

