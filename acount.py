import sqlite3

class AlunoRepository:
    def __init__(self, db_name="alunos.db"):
        self.db_name = db_name
    def conectar(self):
        return sqlite3.connect(self.db_name)
    def criar_tabela(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
        """)

        con.commit()
        con.close()

    def inserir(self, nome, idade, curso):
     con = self.conectar()
     cur = con.cursor()

     cur.execute(
        "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
        (nome, idade, curso)
     )

     con.commit()
     novo_id = cur.lastrowid
     con.close()

     return novo_id



    def buscar_por_id(self, aluno_id):
     con = self.conectar()
     cur = con.cursor()

     cur.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
     linha = cur.fetchone()
     con.close()

     if linha:
        return Aluno(linha[0], linha[1], linha[2], linha[3])
     return None
    def atualizar(self, aluno_id, nome, idade, curso):
     con = self.conectar()
     cur = con.cursor()

     cur.execute(
        "UPDATE alunos SET nome = ?, idade = ?, curso = ? WHERE id = ?",
        (nome, idade, curso, aluno_id)
    )

     con.commit()
     con.close()
    def deletar(self, aluno_id):
     con = self.conectar()
     cur = con.cursor()

     cur.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))

     con.commit()
     con.close()




        


class Aluno:
    def __init__(self, id, nome, idade, curso):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', idade={self.idade}, curso='{self.curso}')"
    def salvar(self, repo):
     if self.id is None:
        
        novo_id = repo.inserir(self.nome, self.idade, self.curso)
        self.id = novo_id
     else:
        
      repo.atualizar(self.id, self.nome, self.idade, self.curso)


repo = AlunoRepository()
repo.criar_tabela()

aluno = Aluno(None, "Carlos", 19, "ADS")
aluno.salvar(repo)

print(aluno)  

aluno.idade = 20
aluno.curso = "Engenharia"
aluno.salvar(repo)

print(repo.buscar_por_id(aluno.id))
