"""
Objetivo: Crie um jogo que levará o usuário a vários possíveis finais de acordo com as
respostas que forem passadas para ele.
"""

jogar = input("Você deseja jogar? Caso afirmativo, digite 'sim':\n")
jogar = jogar.strip().lower()


def aceitou_jogar(aceitou: str) -> bool:
    return aceitou == 'sim'


def is_a(caracterer: str) -> str:
    return caracterer == 'a'


def a_continucao() -> bool:
    resposta = input("""
    Você fica entusiasmado com a notícia. Afinal, estava esperando por isso há algum tempo.
    Decide se levantar e ir de encontro aquele homem. Chegando lá, você diz que aceita
    o desafio. Ele informa que a última vez que a princesa foi vista foi entrando na
    floresta pela estrada norte. Você sabe que a estrada norte é conhecida por
    abrigar vários bandidos perigosos.

    Deseja seguir em frente? Digite a, caso deseje desistir da aventura, digite b.\n
    """)
    resposta = resposta.strip().lower()

    if is_a(resposta):
        return a_continuacao_a1()
    elif is_b(resposta):
        return a_finished_b()

    print("Informe o valor esperado!")
    return False


def a_continuacao_a1() -> bool:
    print("""
    Você termina de beber aquela cerveja. E sai. Não esperou nem mesmo amanhecer!
    Afinal, se trata de uma princesa desaparecida e isso não pode esperar.
    O mensageiro do rei diz que caso a traga de volta viva, irá receber 200 moedas
    de ouro e um cavalo. FIM, POR ENQUANTO!
    """)
    return False


def a_finished_b() -> bool:
    print("""
    Você decide não se arriscar e ignora o aviso daquele homem. Afinal, você
    está aí para se divertir e, quem sabe, conseguir uma noite com uma das garçonetes.
    FIM!
    """)
    return False


def is_b(caracterer: str) -> bool:
    return caracterer == 'b'


def is_c(caracterer: str) -> bool:
    return caracterer == 'c'


def b_continucao() -> bool:
    resposta = input("""
    Você decide não se arriscar e ignora o aviso daquele homem. Afinal, você está aí
    para se divertir e, quem sabe, conseguir uma noite com uma das garçonetes!

    Nesse momento, passa uma delas na sua frente. Você percebe que ela é bem bonita,
    agrada aos seus olhos. O que deseja fazer? Soltar uma cantada pra ela, digite a;
    Dar um tapa em sua bunda, digite b; Não fazer, só olhar e voltar para o bar,
    digite c.\n
    """)
    resposta = resposta.strip().lower()

    if is_a(resposta):
        print("""
        Você fala algo pra ela, pensando ser sua melhor poesia. Porém, ela segue em
        frente. Parece que não ouviu suas palavras ou simplesmente não gosta deste
        tipo de aproximação. FIM!
        """)
        return False
    elif is_b(resposta):
        print("""
        Você dá um tapa e aperta bem forte aquele bumbum empinado. Ela olha de
        volta pra você com uma expressão de espanto e raiva.
        É amigo...
        5 homens fortes e armados se levantam e se aproximam de você. Parece que
        nesta taberna pessoas como você não são bem vindas.

        Você luta bem contra o primeiro e o segundo, mas cinco é demais não é mesmo?!
        Você acaba levando uma surra e fica caido no chão. Em seguida, é arrastado
        pra rua e deixado lá. Você acorda pela manhã, com um cachorro sarnento
        lambendo sua boca. FIM!
        """)
        return False
    elif is_c(resposta):
        print("""
        Você volta para o bar, senta e passa a noite sem problemas. Apenas bebendo,
        enquanto o dinheiro render no seu bolso. FIM!
        """)
        return False

    print("Informe o valor esperado!")
    return False


aceitou = aceitou_jogar(jogar)
querJogarAinda = True

while aceitou and querJogarAinda:
    primeiraResposta = input("""
    Você está numa taberna, tomando sua cerveja quente. Está frio lá fora.
    O ambiente ai dentro é acolhedor, tem várias pessoas no recinto e algumas
    garçonetes servindo. A porta de entrada abre e entra um homem acompanhado de dois
    soldados do rei. Ele fala:'O rei manda avisar que está em busca de valorosos
    herois, para encontrar sua filha que está perdida na floresta.'.

    Caso você aceite, digite a. Caso contrário, digite b:\n
    """)
    primeiraResposta = primeiraResposta.strip().lower()

    if is_a(primeiraResposta):
        if a_continucao() is False:
            vaiContinuar = input("""
 -> Deseja iniciar a aventura novamente? Digite sim, caso contrário digite
    qualquer coisa pra sair:\n
    """)
            if aceitou_jogar(vaiContinuar) is False:
                querJogarAinda = False
                continue
    elif is_b(primeiraResposta):
        if b_continucao() is False:
            vaiContinuar = input("""
 -> Deseja iniciar a aventura novamente? Digite sim, caso contrário digite
    qualquer coisa pra sair:\n
    """)
            if aceitou_jogar(vaiContinuar) is False:
                querJogarAinda = False
                continue
    else:
        print("Informe o valor esperado!")
        continue
