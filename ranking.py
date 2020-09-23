import sqlite3

def exibirRanking():
  conn = sqlite3.connect('ranking.db')
  cursor = conn.cursor()

  cursor.execute("""SELECT iniciais, pontuacao FROM rank ORDER BY pontuacao DESC""")
  i = 1
  for linha in cursor.fetchmany(10):
    print(str(i) + " - " + str(linha[0][0:3]) + " - " + str(linha[1]));
    i = i + 1

def inserirRanking(jogadas):
  ini = input("Iniciais: ")
  pts = pontuacao(jogadas)
  
  conn = sqlite3.connect('ranking.db')
  cursor = conn.cursor()

  cursor.execute("""INSERT INTO rank(iniciais, pontuacao) VALUES(?,?)""",(ini.upper(), pts))
  conn.commit()


def pontuacao(jogadas):
  if jogadas == 3:
    return 100
  elif jogadas == 4:
    return 80
  elif jogadas >=5:
    return 40