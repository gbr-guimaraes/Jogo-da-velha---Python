import random
from game import monta_tabuleiro, jogador, computador, alguem_ganhou
from procgen import clear
from ranking import exibirRanking


#---------------------------------
# Programa de Jogo da velha
# Gabriel Guimarães Felix - 23/setembro/2020
#---------------------------------
def main():
    """Rotina principal do jogo da velha
    """

    #---------------------------------
    # Laço principal do programa
    #---------------------------------
    fim = False

    while not fim:
        monta_tabuleiro()    # Desenha o tabuleiro
        jogador()            # Jogador faz o movimento

        if alguem_ganhou(): 
            fim = True       # Preciso verificar após cada jogador jogar 
        else:
            computador()     # computador faz o movimento
            if alguem_ganhou(): 
                fim = True   # Preciso verificar após cada jogador 
    op = input("Jogar Novamente?[S/N]\n");
    if(op == 'S' or op == 's'):
      main();
    elif(op == 'N' or op == 'n'):
      return

def menu():
  """Essa função exibe o menu do jogo"""
  ver = True

  while ver:
    clear()
    print("""
    1 - Jogar
    2 - Mostrar Ranking
    3 - Sair
    """);

    op = int(input("O que deseja fazer: "));

    if op == 1:
      main()
    elif op == 2:
      clear()
      exibirRanking()
      input("Pressione enter para voltar ao menu...")
    elif op == 3:
      ver = False

#---------------------------------
# Inicializa o gerador de números aleatórios
#---------------------------------
random.seed
menu()
