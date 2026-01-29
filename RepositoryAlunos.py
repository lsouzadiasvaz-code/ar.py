import sqlite3
class ReposytorySchool:
    
    
    def create(self):
        table= sqlite3.connect("School.db")
        curse= table.cursor()
        curse.execute("""CREATE TABLE IF NOT EXISTS School(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER NOT NULL, curso TEXT NOT NULL)""")
        table.commit()
        table.close()
    def insert(self, nome, idade, curso):
        table= sqlite3.connect("School.db")
        curse= table.cursor()
        curse.execute("INSERT INTO School(nome, idade, curso) VALUES(?, ?, ?)",(nome, idade, curso))
        table.commit()
        table.close()
    def update(self, nome, idade, a, b):
        table= sqlite3.connect("School.db")
        curse= table.cursor()
        curse.execute(f"UPDATE School SET {a}=? WHERE nome=? AND idade=?",(b, nome, idade))
        table.commit()
        table.close()

    def select_all(self):    
     table= sqlite3.connect("School.db")
     curse= table.cursor()
     curse.execute("SELECT*FROM School")
     alunos = curse.fetchall()
     table.close()
     return alunos
     
    
    
    def select(self, nome, idade):
        table= sqlite3.connect("School.db")
        curse= table.cursor()
        curse.execute("SELECT*FROM School WHERE nome=? AND idade=?",(nome, idade))
        aluno= curse.fetchall()
        return aluno
    
    def delete(self, nome, idade):
        table= sqlite3.connect("School.db")
        curse= table.cursor()
        curse.execute("DELETE  FROM School WHERE nome=? AND idade=?",(nome, idade))
        table.commit()
        table.close()





        


                      
        


    
        





