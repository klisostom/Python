## Idade em Dias

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

### Entrada
O arquivo de entrada contém um valor inteiro.

### Saída
Imprima a saída conforme exemplo fornecido.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
|400 | 1 ano(s)<br/> 1 mes(es)<br/> 5 dia(s) |     
|800 | 2 ano(s)<br/>2 mes(es)<br/>10 dia(s) |         
|30 | 0 ano(s)<br/>1 mes(es)<br/> 0 dia(s)|
            
### Código Submetido
```python
tempo_anos = int(input())
anos = int(tempo_anos / 365)
meses = int(((tempo_anos - (anos * 365)) / 30))
dias = int((tempo_anos % 365 % 30))

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
```


## Conversão de Tempo
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

### Entrada
O arquivo de entrada contém um valor inteiro **N**.

### Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
|556 | 0:9:16 |  
|1   | 0:0:1  |  
|140153 | 38:55:53 | 

### Código Submetido
tempo = int(input())

horas = int((tempo / 3600))
minutos = int(((tempo - (horas * 3600)) / 60))
segundos = int((tempo % 60))

print("{}:{}:{}".format(horas, minutos, segundos))


## Cédulas
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

### Entrada
O arquivo de entrada contém um valor inteiro **N** (0 < **N** < 1000000).

### Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: *“Presentation Error”*.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
|576 | 576<br/> 5 nota(s) de R$ 100,00<br/>1 nota(s) de R$ 50,00<br/>1 nota(s) de R$ 20,00<br/>0 nota(s) de R$ 10,00<br/>1 nota(s) de R$ 5,00<br/>0 nota(s) de R$ 2,00<br/>1 nota(s) de R$ 1,00 |
|11257 | 11257<br/>112 nota(s) de R$ 100,00<br/>1 nota(s) de R$ 50,00<br/>0 nota(s) de R$ 20,00<br/>0 nota(s) de R$ 10,00<br/>1 nota(s) de R$ 5,00<br/>1 nota(s) de R$ 2,00<br/>0 nota(s) de R$ 1,00
|503 | 503<br/>5 nota(s) de R$ 100,00<br/>0 nota(s) de R$ 50,00<br/>0 nota(s) de R$ 20,00<br/>0 nota(s) de R$ 10,00<br/>0 nota(s) de R$ 5,00<br/>1 nota(s) de R$ 2,00<br/>1 nota(s) de R$ 1,00

### Código Submetido
```python
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c = 0
entrada = int(input())
a_sacar = entrada
valor = entrada

while entrada > 0:
    if a_sacar >= 100:
        while a_sacar >= 100:
            a_sacar = a_sacar - 100
            c100 = c100 + 1
    if a_sacar >=  50:
        while a_sacar >= 50:
            a_sacar = a_sacar - 50
            c50 = c50 + 1
    if a_sacar >= 20:
        while a_sacar >= 20:
            a_sacar = a_sacar - 20
            c20 = c20 + 1
    if a_sacar >= 10:
        while a_sacar >= 10:
            a_sacar = a_sacar - 10
            c10 = c10 + 1
    if a_sacar >= 5:
        while a_sacar >= 5:
            a_sacar = a_sacar - 5
            c5 = c5 + 1
    if a_sacar >= 2:
        while a_sacar >= 2:
            a_sacar = a_sacar - 2
            c2 = c2 + 1
    if a_sacar >= 1:
        while a_sacar >= 1:
            a_sacar = a_sacar - 1
            c = c + 1

    entrada = a_sacar

print(valor)
print("{} nota(s) de R$ 100,00".format(c100))
print("{} nota(s) de R$ 50,00".format(c50))
print("{} nota(s) de R$ 20,00".format(c20))
print("{} nota(s) de R$ 10,00".format(c10))
print("{} nota(s) de R$ 5,00".format(c5))
print("{} nota(s) de R$ 2,00".format(c2))
print("{} nota(s) de R$ 1,00".format(c))
```