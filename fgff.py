import sqlite3
cr=sqlite3.connect("alunos.db")
db= cr.cursor()
cr.execute("""CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade REAL NOT NULL, curso TEXT NOT NULL)""") 
cr.commit()


def inserir(a, b, c):
    cr=sqlite3.connect("alunos.db")
    db=cr.cursor()
    cr.execute("INSERT INTO alunos(nome, idade, curso) VALUES (?, ?, ?)",(a, b, c))
    cr.commit()
    cr.close()

nome= input("nome: ")
idade= int(input("idade: "))
curso= input("curso: ")
inserir(nome, idade, curso) 

