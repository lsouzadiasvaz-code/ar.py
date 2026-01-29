import sqlite3
def criar_tabela():
 tb = sqlite3.connect("alunos.db")
 cr = tb.cursor()
 cr.execute("""
  CREATE TABLE IF NOT EXISTS alunos(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome TEXT  NOT NULL,
           idade REAL NOT NULL,
           curso TEXT NOT NULL
 )
           """)
 tb.commit()
 tb.close()


def inserir(nome, idade, curso):
 tb= sqlite3.connect("alunos.db")
 cr = tb.cursor()
 tb.execute("INSERT INTO alunos(nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso))
            
 tb.commit()
 tb.close()


def listar():
 tb = sqlite3.connect("alunos.db")
 cr = tb.cursor()
 cr.execute("SELECT * FROM alunos")
 linhas = cr.fetchall()
 
 print(linhas)
 return linhas

criar_tabela()
inserir("bruna", 16, "dev")

listar()
              
           
