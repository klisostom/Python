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
