import random

"""
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor, e 
pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.
"""

valor_aleatorio = random.randrange(1, 11)

def is_integer(value):
    try:
        int(value)
        return True
    except:
        pass
    return False

while True:
    chute = input("Chute um número entre 1 e 10:\n")

    if not is_integer(chute):
        print("Informe um valor inteiro!\n")
        continue
    elif int(chute) == valor_aleatorio:
        print("Parabéns, você acertou!!!")
        break
    elif int(chute) > (valor_aleatorio + 3):
        print("Você chutou alto!")
        continue
    elif int(chute) < (valor_aleatorio - 3):
        print("Você chutou baixo!")
        continue
    else:
        print("Tá perto!!")