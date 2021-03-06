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
```python
tempo = int(input())

horas = int((tempo / 3600))
minutos = int(((tempo - (horas * 3600)) / 60))
segundos = int((tempo % 60))

print("{}:{}:{}".format(horas, minutos, segundos))
```

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


## Gasto de Combustível
Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

### Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h).

### Saída
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 10<br/>85  | 70.833 |
| 2<br/>92   | 15.333 |
| 22<br/>67  | 122.833 |

### Código Submetido
```python
T = int(input())
V = int(input())
D = V * T

X = D / 12
print("{:.3f}".format(X))
```


## Distância
Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

### Entrada
O arquivo de entrada contém um número inteiro.

### Saída
Imprima o tempo necessário seguido da mensagem "minutos".

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 30  | 60 minutos |
| 110   | 220 minutos |
| 7  | 14 minutos |

### Código Submetido
```python
entrada = int(input())
x = 2 * entrada
print("{} minutos".format(x))
```


## Distância Entre Dois Pontos
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
![](https://1.bp.blogspot.com/-PQIs7TBdEag/T3PH5meSa2I/AAAAAAAAABI/myd8tKtGCj0/w1200-h630-p-k-no-nu/formula+distancia+entre+dois+pontos.jpg)

### Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: **x1 y1** e a segunda linha contém dois valores de ponto flutuante **x2 y2**.

### Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 1.0 7.0<br/>5.0 9.0  | 4.4721 |
| -2.5 0.4<br/>12.1 7.3  | 16.1484 |
| 2.5 -0.4<br/>-12.2 7.0  | 16.4575 |

### Código Submetido
```python
import math

entrada1 = input()
entrada2 = input()
lista1 = entrada1.split()
lista2 = entrada2.split()

x1 = float(lista1[0])
y1 = float(lista1[1])
x2 = float(lista2[0])
y2 = float(lista2[1])

resultado = math.sqrt( ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)) )
print("{:.4f}".format(resultado))
```

## Consumo
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

### Entrada
O arquivo de entrada contém dois valores: um valor inteiro *X* representando a distância total percorrida (em Km), e um valor real *Y* representando o total de combustível gasto, com um dígito após o ponto decimal.

### Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 500<br/>35.0  | 14.286 km/l |
| 2254<br/>124.4  | 18.119 km/l |
| 4554<br/>464.6  | 9.802 km/l |

### Código Submetido
```python
X = float(input()) #Km
Y = float(input()) #gasosa

print("{:.3f} km/l".format(X / Y))
```

## O Maior
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem "eh o maior". Utilize a fórmula:
![](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png)

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

### Entrada
O arquivo de entrada contém três valores inteiros.

### Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 7 14 106  | 106 eh o maior |
| 217 14 6  | 217 eh o maior |

### Código Submetido
```python
entrada = input()
lista = entrada.split()

a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

temp = (a + b + abs(a - b)) / 2
final = (temp + c + abs(temp - c)) / 2

print("{} eh o maior".format(int(final)))
```


## Área
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

### Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

### Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 3.0 4.0 5.2  | TRIANGULO: 7.800<br />CIRCULO: 84.949<br />TRAPEZIO: 18.200<br />QUADRADO: 16.000<br />RETANGULO: 12.000 |
| 12.7 10.4 15.2  | TRIANGULO: 96.520<br />CIRCULO: 725.833<br />TRAPEZIO: 175.560<br />QUADRADO: 108.160<br />RETANGULO: 132.080 |

### Código Submetido
```python
entrada = input()
lista = entrada.split()
pi = 3.14159
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

print("TRIANGULO: {:.3f}".format((A * C) / 2)) #Area = (a x c)/2
print("CIRCULO: {:.3f}".format(pi * (C * C))) #A = π r²
print("TRAPEZIO: {:.3f}".format( (C * (A + B)) / 2) ) #A = h * (B + b)/2
print("QUADRADO: {:.3f}".format(B * B))
print("RETANGULO: {:.3f}".format(A * B))
```


## Esfera
Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4 / 3) * pi * R<sup>3</sup>. Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4 / 3.0) ou (4.0 / 3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

### Entrada
O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.

### Saída
A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 3         |     VOLUME = 113.097     |
| 15         |     VOLUME = 14137.155     |
| 1523         |     VOLUME = 14797486501.627     |

### Código Submetido
```python
raio = float(input())
pi = 3.14159
volume = (4 / 3) * pi * (raio * raio * raio)

print("VOLUME = {:.3f}".format(volume))
```


## Cálculo Simples
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

### Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

### Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 12 1 5.30<br />16 2 5.10 | VALOR A PAGAR: R$ 15.50 |
| 13 2 15.30<br />161 4 5.20 | VALOR A PAGAR: R$ 51.40 |
| 1 1 15.10<br />2 1 15.10 | VALOR A PAGAR: R$ 30.20 |

### Código Submetido
```python
linha1 = input()
x1 = linha1.split()
num1 = int(x1[1])
valor1 = float(x1[2])


linha2 = input()
x2 = linha2.split()
num2 = int(x2[1])
valor2 = float(x2[2])

print("VALOR A PAGAR: R$ {:.2f}".format( (valor1 * num1) + (valor2 * num2)))
```


## Salário com Bônus
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

### Entrada
O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

### Saída
Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| JOAO<br />500.00<br />1230.30 | TOTAL = R$ 684.54 |
| PEDRO<br />700.00<br />0.00 | TOTAL = R$ 700.00 |
| MANGOJATA<br />1700.00<br />1230.50 | TOTAL = R$ 1884.58 |

### Código Submetido
```python
nome = input()
salario = float(input())
total = float(input())

print("TOTAL = R$ {:.2f}".format(salario + (total * 0.15)))
```


## Salário
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

### Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

### Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 25<br />100<br />5.50 | NUMBER = 25<br />SALARY = U$ 550.00 |
| 1<br />200<br />25.50 | NUMBER = 1<br />SALARY = U$ 4100.00 |
| 6<br />145<br />15.55 | NUMBER = 6<br />SALARY = U$ 2254.75 |

### Código Submetido
```python
number = int(input())
horas = int(input())
valor = float(input())

print("NUMBER = {}".format(number))
print("SALARY = U$ {:.2f}".format(horas * valor))
```


## Diferença
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

### Entrada
O arquivo de entrada contém 4 valores inteiros.

### Saída
Imprima a mensagem *DIFERENCA* com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 5<br />6<br />7<br />8 | DIFERENCA = -26 |
| 0<br />0<br />7<br />8 | DIFERENCA = -56 |
| 5<br />6<br />-7<br />8 | DIFERENCA = 86 |

### Código Submetido
```python
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print("DIFERENCA = {}".format((A * B) - (C * D)))
```


## Média 2
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

### Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

### Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 5.0<br />6.0<br />7.0 | MEDIA = 6.3 |
| 5.0<br />10.0<br />10.0 | MEDIA = 9.0 |
| 10.0<br />10.0<br />5.0 | MEDIA = 7.5 |

### Código Submetido
```python
A = float(input())
B = float(input())
C = float(input())

media = ((A * 2) + (B * 3) + (C * 5)) / 10
print('MEDIA = {:.1f}'.format(media))
```


## Área do Círculo
A fórmula para calcular a área de uma circunferência é: *area = π . raio<sup>2</sup>*. Considerando para este problema que *π* = 3.14159:

\- Efetue o cálculo da área, elevando o valor de *raio* ao quadrado e multiplicando por *π*.

### Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável *raio*.

### Saída
Apresentar a mensagem "A=" seguido pelo valor da variável *area*, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

|Exemplo de Entrada | Exemplo de Saída|
| :---         |     :---     |
| 2.00         |     A=12.5664     |
| 100.64       |     A=31819.3103    |
| 150.00       |     A=70685.7750    |

### Código Submetido
```python
pi = 3.14159
raio = float(input())
area = pi * (raio * raio)
print("A={:.4f}".format(area))
```
