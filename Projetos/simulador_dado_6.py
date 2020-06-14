import random

"""
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.
"""

print("Você gostaria de jogar o dado? Digite 'sim' ou 'não', sem aspas:")
resposta = input().lower().strip()

while True:
    if resposta == 'sim':
        print(random.randrange(1, 7))
    elif resposta == 'não':
        break;
    else:
        print("Informe a resposta esperada: 'sim' ou 'não, sem aspas!")

    print("Você gostaria de jogar o dado? Digite 'sim' ou 'não', sem aspas:")
    resposta = input().lower().strip()

