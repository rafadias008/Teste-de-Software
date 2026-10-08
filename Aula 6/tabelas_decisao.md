# Exercício 1: Classificação do IMC

Condições:

- C1: IMC < 18,5
- C2: IMC < 25
- C3: IMC < 30

### Tabela completa

| Condição | R1 | R2 | R3 | R4 |
| -------- | -- | -- | -- | -- |
| IMC < 18,5 | S | N | N | N |
| IMC < 25 | - | S | N | N |
| IMC < 30 | - | - | S | N |
| -------- | -- | -- | -- | -- |
| Abaixo do Peso | X | -- | -- | -- |
| Peso normal | -- | X | -- | -- |
| Sobrepeso | -- | -- | X | -- |
| Obesidade | -- | -- | -- | X |


## Exercício 4: Frete grátis


Condições:

- C1: Compra > R$200
- C2: Cliente Premium
- C3: Peso =< 30


| Condição | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
| -------- | -- | -- | -- | -- | -- | -- | -- | -- |
| Compra > R$200 | S | S | S | S | N | N | N | N |
| Cliente Premium | S | S | N | N | S | S | N | N |
| Peso =< 30 | S | N | S | N | S | N | S | N |
| -------- | -- | -- | -- | -- | -- | -- | -- | -- |
| Frete Grátis | X | -- | -- | -- | -- | -- | -- | -- |
| Frete Cobrado | -- | X | X | X | X | X | X | X |


## Tabela Reduzida

| Condição | R1 | R2 | R3 | R4 |
| -------- | -- | -- | -- | -- |
| Compra > R$200 | N | S | S | S |
| Cliente Premium | - | N | S | S |
| Peso =< 30 | - | - | N | S |
| -------- | -- | -- | -- | -- |
| Frete Grátis | -- | -- | -- | X |
| Frete Cobrado | X | X | X | -- |


