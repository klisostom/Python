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