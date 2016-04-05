#Grupo 4 / 77459 - Henrique Lourenco / 79042 - Jorge Heleno / 79450 - Valerie Duarte

from auxiliar import *

#Funcao que recebe um numero inteiro positivo menor que 10 de fosforos nas 
#3 pilhas p1, p2 e p3, respectivamente, e pede ao jogador j (1, 2 ou automatico)
#que retire um numero inteiro de objectos (maior que zero e menor que o numero 
#de fosforos na pilha escolhida) de uma pilha p (1, 2 ou 3).
def pede_jogada(p1,p2,p3,j):
    pilha = (p1,p2,p3)
    if (p1 < 0 or p1 >= 10) or (p2 < 0 or p2 >= 10) or (p3 < 0 or p3 >= 10):
        raise ValueError('pede_jogada: valor invalido nas pilhas')
    elif j != 1 and j != 2:
        raise ValueError('pede_jogada: numero de jogador invalido')
    else:
        print('- Jogador',j,'-')
        p = eval(input('Seleccione uma pilha (1, 2 ou 3): '))
        while p not in (1,2,3):
            print('Pilha invalida.')
            p = eval(input('Seleccione uma pilha (1, 2 ou 3): '))
        o = eval(input('Indique o numero de objectos a retirar (max: '\
                       + str(pilha[p-1]) + '): '))
        while o > pilha[p-1] or o <= 0:
            print('Numero de objectos invalido.')
            p = eval(input('Seleccione uma pilha (1, 2 ou 3): '))
            while p not in (1,2,3):
                print('Pilha invalida.')
                p = eval(input('Seleccione uma pilha (1, 2 ou 3): '))
            o = eval(input('Indique o numero de objectos a retirar (max: '\
                       + str(pilha[p-1]) + '): '))
        return p, o


#Funcao que desenha o jogo, escreve na shell do python o numero de fosforos 
#existentes em cada pilha (p1, p2 e p3), cada fosforo e representado pela 
#string 'o-----' e por baixo de cada pilha e escrito o numero de fosforos 
#existentes nessa pilha.
def desenha_jogo(p1,p2,p3):
    if (p1 < 0 or p1 >= 10) or (p2 < 0 or p2 >= 10) or (p3 < 0 or p3 >= 10):
        raise ValueError('desenha_jogo: valor invalido nas pilhas')
    else:
        pilhas = [p1,p2,p3]
        print('')
        while not (pilhas[0] == pilhas[1] == pilhas[2]):
            if pilhas[0] == pilhas[1] and pilhas[0] > pilhas[2]:
                print('o-----   o-----         ')
                pilhas[0] = pilhas[0] - 1
                pilhas[1] = pilhas[1] - 1
            elif pilhas[0] == pilhas[2] and pilhas[0] > pilhas[1]:
                print('o-----            o-----')
                pilhas[0] = pilhas[0] - 1
                pilhas[2] = pilhas[2] - 1
            elif pilhas[1] == pilhas[2] and pilhas[1] > pilhas[0]:
                print('         o-----   o-----')
                pilhas[1] = pilhas[1] - 1
                pilhas[2] = pilhas[2] - 1
            elif pilhas[0] > pilhas[1] and pilhas[0] > pilhas[2]:
                print('o-----                  ')
                pilhas[0] = pilhas[0] - 1
            elif pilhas[1] > pilhas[0] and pilhas[1] > pilhas[2]:
                print('         o-----         ')
                pilhas[1] = pilhas[1] - 1
            elif pilhas[2] > pilhas[0] and pilhas[2] > pilhas[1]:
                print('                  o-----')
                pilhas[2] = pilhas[2] - 1
        while pilhas[0] != 0:
            print('o-----   o-----   o-----')
            pilhas[0] = pilhas[0] - 1
        print('\np1 =',p1,'  p2 =',p2,'  p3 =',p3)


#Funcao que verifica se o jogo esta ou nao terminado, tem resultado logico, 
#Verdadeiro quando o numero de fosforos em cada pilha (p1, p2 e p3) sao 0 Falso
#nos restantes casos
def jogo_terminado(p1,p2,p3):
    if (p1 < 0 or p1 >= 10) or (p2 < 0 or p2 >= 10) or (p3 < 0 or p3 >= 10):
        raise ValueError('jogo_terminado: valor invalido nas pilhas')
    elif not (p1 == 0 and p2 == 0 and p3 == 0):
        return False
    else:
        return True


#Funcao que actualiza o numero de fosforos existentes em cada pilha, recebe o
#numero inteiro existente nas pilhas (p1, p2 e p3), a pilha (p) escolhida pelo
#jogador e o numero inteiro de objectos a retirar (o) dessa pilha e retira o
#fosforos a pilha p.
def actualiza_pilhas(p1,p2,p3,p,o):
    pilhas = [p1,p2,p3]
    if (p1 < 0 or p1 >= 10) or (p2 < 0 or p2 >= 10) or (p3 < 0 or p3 >= 10):
        raise ValueError('actualiza_pilhas: valor invalido nas pilhas')
    elif p < 1 or p > 3:
        raise ValueError('actualiza_pilhas: pilha invalida')
    elif o <= 0 or o >= 10 or o > pilhas[p-1]:
        raise ValueError('actualiza_pilhas: numero de objectos invalido')
    else:
        pilhas[p-1] = pilhas[p-1] - o
        return pilhas[0], pilhas[1], pilhas[2]


#Funcao que utiliza as funcoes anteriores e corre o jogo, recebe o numero 
#inteiro de fosforos em cada pilha (p1, p2 e p3) e um valor logico (True ou
#False) que determina se existe jogador automatico (True) ou 2 jogadores (False).
def jogo_nim(p1,p2,p3,logic):
    j = 0
    if (p1 < 0 or p1 >= 10) or (p2 < 0 or p2 >= 10) or (p3 < 0 or p3 >= 10):
        raise ValueError('jogo_nim: valor invalido nas pilhas')
    elif logic != True and logic != False:
        raise ValueError('jogo_nim: valor logico invalido')
    elif logic == True:
        while jogo_terminado(p1,p2,p3) == False:
            j = j + 1
            if j == 3:
                j = 0
            elif j == 1:
                desenha_jogo(p1,p2,p3)
                p, o = pede_jogada(p1,p2,p3,j)
                p1, p2, p3 = actualiza_pilhas(p1,p2,p3,p,o)
            else:
                desenha_jogo(p1,p2,p3)
                p, o = automatico(p1,p2,p3)
                p1, p2 ,p3 = actualiza_pilhas(p1,p2,p3,p,o)
        if j == 1:
            print('Parabens, ganhou ao jogador automatico!')
        else:
            print('Perdeu o jogador 1. O vencedor foi o jogador automatico.')
    else:
        while jogo_terminado(p1,p2,p3) == False:
            j = j + 1
            if j == 3:
                j = 1
            desenha_jogo(p1,p2,p3)
            p, o = pede_jogada(p1,p2,p3,j)
            p1, p2, p3 = actualiza_pilhas(p1,p2,p3,p,o)
        if j == 1:
            print('Perdeu o jogador 2. O vencedor foi o jogador 1.')
        else:
            print('Perdeu o jogador 1. O vencedor foi o jogador 2.')