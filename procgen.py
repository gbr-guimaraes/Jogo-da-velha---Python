from os import system, name

def clear(): 
    """Limpa a tela
    """
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def pausa(mensagem = "Pressione qualquer tecla para continuar..."):
    """Executa uma pausa, tem como opcional uma mensagem
    """
    print("")
    print(mensagem)
    system('read n1')

def iif(condicao, valor1, valor2):
    """Retornar valor1 se a condição for verdadeira, senão retorna valor 2
    """
    if (eval(condicao)):
        return valor1
    else:
        return valor2
