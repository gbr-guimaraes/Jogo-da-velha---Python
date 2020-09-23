from procgen import clear
import random
from ranking import inserirRanking

# ------------------------------------------
# Vetor para armazenar o tabuleiro
# ------------------------------------------
tabuleiro = [[0,0,0],
             [0,0,0],
             [0,0,0]
            ]

jogadas = 0

def monta_tabuleiro():
    """Monta o tabuleiro do jogo com as jogadas executadas
    """
    clear()             # Limpa a tela (função da procgen)
    print("""
Jogo da velha 
-------------

Você joga com X e o computador joga com O. 
Utilize o teclado numérico para jogar, você começa :)    
        
        """)

    # Poderia ter usado um ou mais loops para montar o tabuleiro
    # mantive mais simples por fins didáticos
    print("+---+---+---+")
    print("| " + posicao(0,0) + " | " + posicao(0,1) + " | " + posicao(0,2) + " |")
    print("+---+---+---+")
    print("| " + posicao(1,0) + " | " + posicao(1,1) + " | " + posicao(1,2) + " |")
    print("+---+---+---+")
    print("| " + posicao(2,0) + " | " + posicao(2,1) + " | " + posicao(2,2) + " |")
    print("+---+---+---+")
    print("")

#------------------------------------------------------------------------
def posicao(x,y):
#------------------------------------------------------------------------    
    """Retorna o conteúdo da posição informada x,y
    """    
    # 1 é a jogada "X"
    # -1 é a jogada "O"
    # 0 significa que está vazio

    valor = tabuleiro[x][y]
    if(valor==1):
        return "X"
    elif(valor==-1):
        return "O"
    else:
        return " "

#------------------------------------------------------------------------
def jogador():
#------------------------------------------------------------------------    
    """Faz a movimentação do jogador
    """    
    ocupado = True
    while ocupado:
        p = input("Qual sua jogada? ")
        valor = verifica(p)
        if (valor==0):
            marcajogada(p,1)
            contaJogadas()
            ocupado = False
    

#------------------------------------------------------------------------
def computador():
#------------------------------------------------------------------------    
    """Faz a movimentação do computador
    """    
    ocupado = True
    while ocupado:
        p = str(random.randrange(1,9))
        valor = verifica(p)
        if (valor==0):
            marcajogada(p,-1)
            ocupado = False

#------------------------------------------------------------------------
def marcajogada(p,valor):
#------------------------------------------------------------------------
    """Marca no tabuleiro a jogada
    """
    if(p=="7"): tabuleiro[0][0]=valor
    if(p=="8"): tabuleiro[0][1]=valor
    if(p=="9"): tabuleiro[0][2]=valor

    if(p=="4"): tabuleiro[1][0]=valor
    if(p=="5"): tabuleiro[1][1]=valor
    if(p=="6"): tabuleiro[1][2]=valor

    if(p=="1"): tabuleiro[2][0]=valor
    if(p=="2"): tabuleiro[2][1]=valor
    if(p=="3"): tabuleiro[2][2]=valor    

#------------------------------------------------------------------------
def verifica(p):
#------------------------------------------------------------------------    
    """Verifica o valor que está preenchido no tabuleiro
    """    
    if(p=="7"): valor = tabuleiro[0][0]
    if(p=="8"): valor = tabuleiro[0][1]
    if(p=="9"): valor = tabuleiro[0][2]

    if(p=="4"): valor = tabuleiro[1][0]
    if(p=="5"): valor = tabuleiro[1][1]
    if(p=="6"): valor = tabuleiro[1][2]

    if(p=="1"): valor = tabuleiro[2][0]
    if(p=="2"): valor = tabuleiro[2][1]
    if(p=="3"): valor = tabuleiro[2][2]
    return valor



#------------------------------------------------------------------------
def alguem_ganhou():
    """Essa função verifica se alguém ganhou.
    """

    #Verifica as linhas
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma==3 or soma ==-3:
            fimDejogo(soma)
            return True

    #Verifica as colunas
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma==3 or soma ==-3: 
          fimDejogo(soma)
          return True

    #Verifica as duas diagonais
    soma = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    if soma==3 or soma ==-3: 
        fimDejogo(soma)
        return True

    soma = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if soma==3 or soma ==-3: 
        fimDejogo(soma)
        return True

    # Verifica se deu empate
    """A verificação de empate será a ultima para não haver problemas caso alguem ganhe na ultima jogada"""
    n = 0
    """Corrigi o range que estava verificando apenas de 1 a 8, pois o parametro final não é incluso"""
    for i in range(1,10):
        if(verifica(str(i))!=0):
            n = n + 1 
    if n==9:
        print("Empate")
        return True

    return False

#------------------------------------------------------------------------
def quemGanhou(soma):
  """Essa função verifica quem ganhou"""
  if soma == 3:
    print("Jogador Venceu!")
    inserirRanking(jogadas);
  elif soma == -3:
    print("PC Venceu!")

#------------------------------------------------------------------------
def reseta():
  """Essa função reseta o tabuleiro"""
  tabuleiro[0][0] = 0
  tabuleiro[0][1] = 0
  tabuleiro[0][2] = 0
  
  tabuleiro[1][0] = 0
  tabuleiro[1][1] = 0
  tabuleiro[1][2] = 0

  tabuleiro[2][0] = 0
  tabuleiro[2][1] = 0
  tabuleiro[2][2] = 0

  global jogadas
  jogadas = 0

#------------------------------------------------------------------------
def contaJogadas():
  global jogadas
  jogadas = jogadas + 1

#------------------------------------------------------------------------
def fimDejogo(soma):
  monta_tabuleiro()            
  print("Fim de jogo")
  quemGanhou(soma)
  print("Jogadas = " + str(jogadas))
  reseta()

#------------------------------------------------------------------------

