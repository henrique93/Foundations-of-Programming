# - GRUPO N.: 2
# - ALUNO N.: 77459
# - ALUNO N.: 79042
# - ALUNO N.: 79450

# = =  C O N S T A N T E S  = = #

# Dimensoes do tabuleiro

N_LINHAS  = 5
N_COLUNAS = 4

# Tipos de peca

PECA_I = 'I'
PECA_O = 'O'
PECA_U = 'U'
PECA_S = 'S'
ESPACO = 'X'

# Direccoes

NORTE = 'N'
SUL   = 'S'
ESTE  = 'E'
OESTE = 'W'

# = =  T I P O S   A B S T R A C T O S   D E   I N F O R M A C A O  = = #

# ------  TIPO:  COORDENADA  ------ #

def cria_coordenada(l,c):
    '''cria_coordenada : int × int -> coordenada
    cria_coordeada(l,c) cria uma coordenada com a linha e coluna indicadas.'''
    if l not in (1, 2, 3, 4, 5) or c not in (1, 2, 3, 4):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (l,c)

# - Fim: cria_coordenada


def coordenada_linha(c):
    '''coordenada_linha : coordenada -> inteiro
    coordenada_linha(c) indica a linha coorespondente a coordenada indicada.'''
    return c[0]

# - Fim: coordenada_linha


def coordenada_coluna(c):
    '''coordenada_coluna : coordenada -> inteiro
    coordenada_coluna(c) indica a coluna coorespondente a coordenada indicada.'''
    return c[1]

# - Fim: coordenada_coluna


def e_coordenada(arg):
    '''e_coordenada : universal -> logico
    e_coordenada(arg) indica se o argumento recebido cooresponde ou nao
    a uma coordenada.'''
    if not isinstance(arg, tuple) or len(arg) != 2 or coordenada_linha(arg)\
       not in (1, 2, 3, 4, 5) or coordenada_coluna(arg) not in (1, 2, 3, 4):
        return False
    else:
        return True

# - Fim: e_coordenada


def coordenadas_iguais(c1,c2):
    '''coordenadas_iguais : coordenada × coordenada -> logico
    coordenadas_iguais(c1,c2) indica de as coordenadas recebidas sao iguais.'''
    if not e_coordenada(c1) or not e_coordenada(c2):
        raise ValueError('coordenadas_iguais: coordenadas invalidas')
    return c1 == c2

# - Fim: coordenadas_iguais


def coordenada_na_direcao(c,dx,dy):
    '''coordenada_na_direcao : coordenada × int × int -> coordenada
    coordenada_na_direcao(c,dx,dy) devolve as coordenadas que se obtem apos
    mover dx linhas e dy colunas a partir da coordenada c.'''
    if not e_coordenada(c) or not isinstance(dx,int) or not isinstance(dy,int):
        raise ValueError('coordenada_na_direcao: argumentos invalidos')
    coordenada = [coordenada_linha(c) + dx] + [coordenada_coluna(c) + dy]
    if coordenada_linha(coordenada) > 5:
        coordenada[0] = 5
    if coordenada_linha(coordenada) < 1:
        coordenada[0] = 1
    if coordenada_coluna(coordenada) > 4:
        coordenada[1] = 4
    if coordenada_coluna(coordenada) < 1:
        coordenada[1] = 1
    if tuple(coordenada) == c:
        return False
    return tuple(coordenada)

# - Fim: coordenada_na_direcao


# -- Fim: Tipo coordenada -- #


# ---------  TIPO:  PECA  --------- #

def cria_peca(p,c):
    '''cria_peca : cad. caracteres × coordenada -> peca
    cria_peca(p,c) cria uma lista que contem o tipo de peca p, a coordenada c
    coorespondente a posicao de referencia dessa peca e todas as coordenadas 
    coorespondentes as restantes posicoes ocupadas pela peca.'''
    if p not in (PECA_I, PECA_O, PECA_U, PECA_S) or not e_coordenada(c):
        raise ValueError('cria_peca: argumentos invalidos')
    elif (p == PECA_I and coordenada_linha(c) == N_LINHAS) or\
         (p == PECA_O and\
          (coordenada_linha(c) == N_LINHAS or coordenada_coluna(c) == N_COLUNAS)) or\
         (p == PECA_U and coordenada_coluna(c) == N_COLUNAS):
        raise ValueError('cria_peca: coordenada invalida')
    elif p == PECA_I:
        return [p, [c, cria_coordenada(coordenada_linha(c) + 1,\
                                       coordenada_coluna(c))]]
    elif p == PECA_O:
        c2 = cria_coordenada(coordenada_linha(c), coordenada_coluna(c) + 1)
        c3 = cria_coordenada(coordenada_linha(c) + 1, coordenada_coluna(c))
        c4 = cria_coordenada(coordenada_linha(c) + 1, coordenada_coluna(c) + 1)
        return [p, [c, c2, c3, c4]]
    elif p == PECA_U:
        return [p, [c, cria_coordenada(coordenada_linha(c),\
                                       coordenada_coluna(c) + 1)]]
    elif p == PECA_S:
        return [p, [c]]

# - Fim: cria_peca


def peca_posicoes(p):
    '''peca_posicoes : peca -> lista
    peca_posicoes(p) devolve todas as posicoes que a peca p ocupa.'''
    return p[1]

# - Fim: peca_posicoes


def peca_tipo(p):
    '''peca_tipo : peca -> cad. caracteres
    peca_tipo(p) indica o tipo de peca coorespondente a peca p.'''
    if p[0] not in (PECA_I, PECA_O, PECA_U, PECA_S):
        raise ValueError('peca_tipo: peca invalida')
    return p[0]

# - Fim: peca_tipo


def e_peca(arg):
    '''e_peca : universal -> logico
    e_peca(arg) indica se o argumento recebido cooresponde ou nao a uma peca.'''
    if not isinstance(arg, list) or len(arg) != 2 or not\
       isinstance(arg[1],list) or peca_tipo(arg) not in\
       (PECA_I, PECA_O, PECA_U, PECA_S) or\
       (peca_tipo(arg) in (PECA_I, PECA_U) and len(peca_posicoes(arg)) != 2) or\
       (peca_tipo(arg) == PECA_S and len(peca_posicoes(arg)) != 1) or\
       (peca_tipo(arg) == PECA_O and len(peca_posicoes(arg)) != 4):
        return False
    posicoes = peca_posicoes(arg)
    for i in range(len(posicoes)):
        if not isinstance(posicoes[i], tuple) or not e_coordenada(posicoes[i]):
            return False
        if len(posicoes) > 0:
            for j in range(i+1,len(posicoes)):
                if peca_posicoes(arg)[i] == peca_posicoes(arg)[j]:
                    return False
    return True

# - Fim: e_peca


def peca_na_posicao(p,c):
    '''peca_na_posicao : peca × coordenada -> logico
    peca_na_posicao(p,c) indica se a peca p se encontra ou nao na posicao
    de coordenada c.'''
    if not e_peca(p) or not e_coordenada(c):
        raise ValueError('peca_na_posicao: argumentos invalidos')
    return c in peca_posicoes(p)

# - Fim: peca_na_posicao


def peca_move(p,dx,dy):
    '''peca_move : peca × int × int -> {}
    peca_move(p,dx,dy) move a peca p dx linhas e dx colunas.'''
    if not e_peca(p) or dx not in range(-4,5) or dy not in range(-3,4):
        raise ValueError('peca_move: argumentos invalidos')
    posicoes_finais = []
    for i in range(0,len(peca_posicoes(p))):
        posicoes_finais += (coordenada_linha(peca_posicoes(p)[i]) + dx,\
                            coordenada_coluna(peca_posicoes(p)[i]) + dy),
        if not e_coordenada(posicoes_finais[i]):
            raise ValueError('peca_move: argumentos invalidos')
    p[1] = posicoes_finais
    
# - Fim: peca_move


def posicoes_adjacentes(p,d):
    '''posicoes_adjacentes : peca × cad. caracteres -> lista
    posicoes_adjacentes(p,d) devolve uma lista com todas as coordenadas
    coorespondentes a posicoes adjacentes a peca p na direcao d.'''
    if not e_peca(p) or d not in (NORTE, SUL, ESTE, OESTE):
        raise ValueError('posicoes_adjacentes: argumentos invalidos')
    posicoes = []
    if d == NORTE:
        if coordenada_linha(peca_posicoes(p)[0]) == 1:
            return False
        for i in range(len(peca_posicoes(p))):
            if (coordenada_linha(peca_posicoes(p)[i]) - 1,\
                coordenada_coluna(peca_posicoes(p)[i])) not in peca_posicoes(p):
                posicoes += cria_coordenada(coordenada_linha(peca_posicoes(p)[i]) - 1,\
                                            coordenada_coluna(peca_posicoes(p)[i])),
    elif d == SUL:
        if coordenada_linha(peca_posicoes(p)[-1]) == 5:
            return False
        for i in range(len(peca_posicoes(p))):
            if (coordenada_linha(peca_posicoes(p)[i]) + 1,\
                coordenada_coluna(peca_posicoes(p)[i])) not in peca_posicoes(p):
                posicoes += cria_coordenada(coordenada_linha(peca_posicoes(p)[i]) + 1,\
                                            coordenada_coluna(peca_posicoes(p)[i])),
    elif d == ESTE:
        if coordenada_coluna(peca_posicoes(p)[-1]) == 4:
            return False
        for i in range(len(peca_posicoes(p))):
            if (coordenada_linha(peca_posicoes(p)[i]),\
                coordenada_coluna(peca_posicoes(p)[i]) + 1) not in peca_posicoes(p):
                posicoes += cria_coordenada(coordenada_linha(peca_posicoes(p)[i]),\
                                            coordenada_coluna(peca_posicoes(p)[i]) + 1),
    elif d == OESTE:
        if coordenada_coluna(peca_posicoes(p)[0]) == 1:
            return False
        for i in range(len(peca_posicoes(p))):
            if (coordenada_linha(peca_posicoes(p)[i]),\
                coordenada_coluna(peca_posicoes(p)[i]) - 1) not in peca_posicoes(p):
                posicoes += cria_coordenada(coordenada_linha(peca_posicoes(p)[i]),\
                                            coordenada_coluna(peca_posicoes(p)[i]) - 1),
    for e in posicoes:
        if not e_coordenada(e):
            return False
    return posicoes

# - Fim: posicoes_adjacentes


# -- Fim: Tipo peca -- #


# -------  TIPO: TABULEIRO  ------- #

def cria_tabuleiro(file):
    '''cria_tabuleiro : cad. caracteres -> tabuleiro
    cria_tabuleiro(file) recebe um ficheiro com a estrutura de um tabuleiro e 
    abre-o criando um tabuleiro de jogo.'''
    if not isinstance(file, str):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    file = open(file,'r')
    tabuleiro = file.readlines()
    tabuleiro = tabuleiro[0:5]
    tabuleiro_final = []
    linha = 0
    coluna = 0
    while tabuleiro_final == []:
        if tabuleiro[linha][coluna] != ESPACO:
            tabuleiro_final = [cria_peca(tabuleiro[linha][coluna],\
                                         cria_coordenada(linha+1,coluna+1))]
        coluna += 1
        if coluna == 4:
            coluna = 0
            linha += 1
            if linha == 5:
                raise ValueError('cria_tabuleiro: argumentos invalidos')
    for i in range(len(tabuleiro)):
        tabuleiro[i] = tabuleiro[i][0:4]
        for j in range(len(tabuleiro[i])):
            for k in range(len(tabuleiro_final)):
                if cria_coordenada(i+1,j+1) in tabuleiro_final[k][1] or\
                   tabuleiro[i][j] == ESPACO:
                    break
                elif k == len(tabuleiro_final) - 1:
                    tabuleiro_final += [cria_peca(tabuleiro[i][j],cria_coordenada(i+1,j+1))]
    return tabuleiro_final

# - Fim: cria_tabuleiro


def tabuleiro_posicao(t,c):
    '''tabuleiro_posicao : tabuleiro × coordenada -> peca
    tabuleiro_posicao(t,c) devolve a peca que se encontra na posicao
    de coordenada c no tabuleiro t.'''
    if not e_tabuleiro(t) or not e_coordenada(c):
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    for i in range(len(t)):
        if c in peca_posicoes(t[i]):
            return t[i]
    return ESPACO

# - Fim: tabuleiro_posicao


def actualiza_tabuleiro(t,c,d):
    '''actualiza_tabuleiro : tabuleiro × coordenada × cad. caracteres -> {}
    actualiza_tabuleiro(t,c,d) modifica o tabuleiro de modo a mover a peca na
    posicao de coordenada c na direcao d.'''
    if not e_tabuleiro(t) or not e_coordenada(c) or\
       d not in (NORTE, SUL, ESTE, OESTE):
        raise ValueError('actualiza_tabuleiro: argumentos invalidos')
    elif d == NORTE:
        dx, dy = -1, 0
    elif d == SUL:
        dx, dy = 1, 0
    elif d == ESTE:
        dx, dy = 0, 1
    elif d == OESTE:
        dx, dy = 0, -1
    for e in t:
        if c in peca_posicoes(e):
            e = peca_move(tabuleiro_posicao(t,c), dx, dy)
            break

# - Fim: actualiza_tabuleiro


def tabuleiro_posicao_livre(t,c):
    '''tabuleiro_posicao_livre : tabuleiro × coordenada -> logica
    tabuleiro_posicao_livre(t,c) indica se a posicao de coordenada c no
    tabuleiro c esta ou nao livre, ou seja, indica se e um espaco vazio.'''
    if not e_tabuleiro(t) or not e_coordenada(c):
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    return tabuleiro_posicao(t,c) == ESPACO

# - Fim: tabuleiro_posicao_livre


def e_tabuleiro(arg):
    '''e_tabuleiro : universal -> logico
    e_tabuleiro(arg) indica se o argumento recebido e ou nao um tabuleiro.'''
    if not isinstance(arg,list) or len(arg) > 14:
        return False
    for e in arg:
        if not e_peca(e):
            return False
    return True

# - Fim: e_tabuleiro


# -- Transformador de saida -- #

def desenha_tabuleiro(t):
    ''' desenha_tabuleiro : tabuleiro -> {}
        desenha_tabuleiro(t) desenha o tabuleiro de jogo t para o ecra.'''
    
    DESENHOS = {'TOPO'     : ('+---+','|   |','|   |'),
                'FUNDO'    : ('|   |','|   |','+---+'),
                'ESQUERDA' : ('+----','|    ','+----'),
                'DIREITA'  : ('----+','    |','----+'),
                'TOPOESQ'  : ('+----','|    ','|    '),
                'TOPODIR'  : ('----+','    |','    |'),
                'FUNDOESQ' : ('|    ','|    ','+----'),
                'FUNDODIR' : ('    |','    |','----+'),
                'CENTRO'   : ('+---+','|   |','+---+'),
                'ESPACO'   : ('     ','     ','     ')}    
    
    desenho = [[0] * 4, [0] * 4, [0] * 4, [0] * 4, [0] * 4]

    print('\n      1    2    3    4    ')
    print('   ---------------------- ')
    
    for l in range(N_LINHAS):
        s1 = ''
        s2 = ''
        s3 = ''
        
        for c in range(N_COLUNAS):
            
            if desenho[l][c] == 0:
                p = tabuleiro_posicao(t, cria_coordenada(l + 1, c + 1))
                                
                if p == ESPACO:
                    desenho[l][c] = 'ESPACO'
                elif peca_tipo(p) == PECA_I:
                    desenho[l][c] = 'TOPO'
                    desenho[l+1][c] = 'FUNDO'
                elif peca_tipo(p) == PECA_U:
                    desenho[l][c]     = 'ESQUERDA'
                    desenho[l][c+1]   = 'DIREITA'
                elif peca_tipo(p) == PECA_O:
                    desenho[l][c]     = 'TOPOESQ'
                    desenho[l+1][c]   = 'FUNDOESQ'
                    desenho[l][c+1]   = 'TOPODIR'
                    desenho[l+1][c+1] = 'FUNDODIR'
                elif peca_tipo(p) == PECA_S:
                    desenho[l][c]     = 'CENTRO'
                else:
                    raise ValueError ('desenha_tabuleiro: problema a aceder a tabuleiro')
                    
            s1 = s1 + DESENHOS[desenho[l][c]][0]
            s2 = s2 + DESENHOS[desenho[l][c]][1]
            s3 = s3 + DESENHOS[desenho[l][c]][2]

        print('  |', s1, '| ')
        print(l+1, '|', s2, '|', l+1)
        print('  |', s3, '|')    
    
    print('   ------          ------ ')
    print('      1    2    3    4    ')

# - Fim: desenha_tabuleiro

# -- Fim: Tipo tabuleiro -- #


# = =  O U T R A S   F U N C O E S  = = #

def jogada_valida(t,c,d):
    '''jogada_valida : tabuleiro × coordenada × cad. caracteres -> logico
    jogada_valida(t,c,d) india se a jogada coorespondente a mover a peca que
    ocupa a posicao de coordenada c no tabuleiro t na direcao d e ou nao
    possivel/valida.'''
    if not e_tabuleiro(t) or not e_coordenada(c) or\
       d not in (NORTE, SUL, ESTE, OESTE):
        raise ValueError('jogada_valida: argumentos invalidos')
    elif tabuleiro_posicao_livre(t,c) == True or\
         posicoes_adjacentes(tabuleiro_posicao(t,c),d) == False:
        return False
    for e in posicoes_adjacentes(tabuleiro_posicao(t,c),d):
        if tabuleiro_posicao(t,e) != ESPACO:
            return False
    return True

# - Fim: jogada_valida


def pede_jogada():
    '''pede_jogada : {} → coordenada, cad. caracteres
    pede_jogada() pede ao utilizador que indique uma linha (entre 1 e 5),
    uma coluna (entre 1 e 4) e uma direcao (N, S, E ou O), verifica se os
    valores introduzidos sao validos e, caso sejam, devolve um elemento
    do tipo coordenada, formada pela linha e coluna indicadas, e a
    direcao indicada.'''
    try:
        linha = eval(input('Introduza uma linha (1 a 5): '))
    except(NameError, SyntaxError):
        print('Linha invalida.')
        return pede_jogada()
    if not linha in (1, 2, 3, 4, 5):
        print('Linha invalida.')
        return pede_jogada()
    try:
        coluna = eval(input('Introduza uma coluna (1 a 4): '))
    except(NameError, SyntaxError):
        print('Coluna invalida.')
        return pede_jogada()
    if not coluna in (1, 2, 3, 4):
        print('Coluna invalida.')
        return pede_jogada()
    direccao = input('Introduza uma direccao (N, S, E ou W): ')
    if not direccao in (NORTE, SUL, ESTE, OESTE):
        print('Direcao invalida.')
        return pede_jogada()
    return cria_coordenada(linha, coluna), direccao

# - Fim: pede_jogada


def jogo_terminado(t):
    '''jogo_terminado : tabuleiro -> logico
    jogo_terminada(t) indica se o jogo que decorre no tabuleiro t esta
    ou nao terminado.'''
    if not e_tabuleiro(t):
        raise ValueError('jogo_terminado: argumentos invalidos')
    for e in t:
        if peca_tipo(e) == PECA_O and cria_coordenada(5,2) in peca_posicoes(e)\
           and cria_coordenada(5,3) in peca_posicoes(e):
            return True
    return False

# - Fim: jogo_terminado


def jogo_quadrado(file):
    '''jogo_quadrado : cad. caracteres → {}
    jogo_quadrado(file) e a funcao que, usando funcoes anteriormente definidas,
    permite ao utilizado jogar um jogo completo de "Liberta o Quadrado".'''
    if not isinstance(file, str):
        raise ValueError('jogo_quadrado: argumentos invalidos')
    cont_jogadas = 0
    t = cria_tabuleiro(file)
    while not jogo_terminado(t):
        desenha_tabuleiro(t)
        coordenada, direccao = pede_jogada()
        while not jogada_valida(t, coordenada, direccao):
            print('Jogada invalida.')
            coordenada, direccao = pede_jogada()
        actualiza_tabuleiro(t, coordenada, direccao)
        cont_jogadas += 1
    print('Parabens, terminou o jogo em', cont_jogadas, 'jogadas.')

# - Fim: jogo_quadrado

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#///////////////////////////////////// FIM /////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\