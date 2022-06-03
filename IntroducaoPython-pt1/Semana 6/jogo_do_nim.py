import random

def partida():
    global jogo
    jogo = int(input(f"Bem vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato \n"))
    if jogo == 1:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? \n"))
        global salvarm
        salvarm = m
        if n < m:
                print("O número de peças deve ser > número de jogadas ")
                partida()
        else:
            if(n % (m + 1) == 0):
                print("Você começa!")
                jogador_escolhe_jogada(n, m)
            else:
                print("Computador começa!")
                computador_escolhe_jogada(n, m)
    elif jogo == 2:
        global usuario
        usuario = 0
        campeonato()
    else:
        erro = str(input("Entrada de dado inválida \n Digite Y para tentar novamente... "))
        #raise ValueError
        if erro == "Y" or "y":
            partida()
        else:
            quit()

def campeonato():
    for jogo in range(1, 4):
        print("**** Rodada ", jogo, " **** \n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n < (m + 1):
                print("O número de peças deve ser > número de jogadas ")
                campeonato()
        else:
            if(n % (m + 1) == 0):
                print("Você começa!")
                jogador_escolhe_jogada(n, m)
            else:
                print("Computador começa!")
                computador_escolhe_jogada(n, m)

    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador")


def jogador_escolhe_jogada(n, m):
    jogada_jogador = int(input("Quantas peças você vai tirar? "))
    if jogada_jogador <= m:
        n = n - jogada_jogador
        print("Voce tirou ", jogada_jogador, "peças.")
        if(n == 0):
            print("Parabéns você ganhou (era pro computador ganhar)")
        else:
            print("Agora restam ", n, "peças no tabuleiro. \n")
            computador_escolhe_jogada(n, m)
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        jogador_escolhe_jogada(n, m)
        # return jogada_jogador

def computador_escolhe_jogada(n, m):
    if(n <= m):
        print("O computador retirou ", n, " peças")
        print("Fim do jogo! O computador ganhou! \n")
    else:
        jogada_computador = n % (m + 1)
        n = n - jogada_computador
        if n % (m + 1) == 0 and jogada_computador <= m and jogada_computador != 0:
            print("O computador tiroud ", jogada_computador, " peças")
            print("Agora restam ", n, " peças no tabuleiro. \n")
            jogador_escolhe_jogada(n, m)
        elif jogada_computador == 1:
            print("O computador tirou uma peça.")
            jogador_escolhe_jogada(n, m)
        else:
            print("Teste deu errado")
            jogador_escolhe_jogada(n, m)

partida()
