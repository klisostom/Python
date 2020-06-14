import random

"""
Objetivo: Crie um script que responda qualquer pergunta que for feita a ele. Recomendo ter 
uma base de possíveis respostas (10-20 ou mais). Ex: Será que devo sair de casa hoje? Seu
script reponde: “Sim, vai lá!”
"""

conjunto_respostas = [
    'Sim, vai lá!',
    'Não, é estranho!',
    'Talvez dê certo.',
    'Talvez, quem sabe?!',
    'Pode ser.',
    'Eu acho que não.',
    'Pode ser amanhã?',
    'E se fosse com você?',
    'E se fosse comigo?',
    'E se fosse com um parente seu?',
    'Não, acredito que não.',
    'Tu vai mesmo é?',
    'Vai dar certo!',
    'Tem que dar certo, desta vez.',
    'Vamos tocer!',
    'Daqui há 1 hora nós vamos.',
    'Já não sei o que dizer.',
    'Isso é possível!',
    'Falta pouco!',
    'É isso aí!'
]

pergunta = input("Faça alguma pergunta:\n")
resposta = conjunto_respostas[random.randrange(1, len(conjunto_respostas) + 1)]
print(resposta)