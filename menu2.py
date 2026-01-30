from RepositoryAlunos import ReposytorySchool

import os
import os


import sqlite3
repository= ReposytorySchool()
repository.create()

class Alunos:
    


    def add(self, nome, idade, curso):        
        aluno= repository.select(nome, idade)
        if idade<18:
            return "invalida"
        if aluno:
            return "aluno ja existe"
        else:
            repository.insert(nome, idade, curso)
            return "adicionado"
    def busc(self, nome, idade):
        busc_1=repository.select(nome, idade)
        if busc_1:
            for i in busc_1:
             return f"id:{i[0]}, nome:{i[1]}, idade:{i[2]}, curso:{i[3]}"
        else:
            return -1
    def updt(self, nome, idade, a, b):
            if idade<18:
                return "invalido"
            busc_3= repository.select(nome, idade)
            if busc_3:
                if a == "nome":
                    repository.update(nome, idade,  a, b)
                    return "nome atualizado"
                elif a == "idade":
                    repository.update(nome, idade,  a, b)
                    return "idade atualizada"
                elif a == "curso":
                    repository.update(nome, idade, a, b)
                    return "curso atualizado"
                else:
                    print("invalido")
            else:
                return "aluno não encontrado"
    def del_1(self, nome, idade):
        busc_4= repository.select(nome, idade)
        if busc_4:
            repository.delete(nome, idade)
            return "aluno removido"
        else:
            return "aluno não existia"
    
                
print("adicionar")
print("listar")
print("buscar")
print("atualizar")
print("deletar")
print("sair")
classm = Alunos()

while True:
    try:
        msg= str(input("qual? ")).lower()
    except ValueError:
        print("invalido")
    if msg=="sair":
        print("encerrado")  
        break
    elif msg=="adicionar":
          try:
              nome= str(input("nome: "))
              idade= int(input("idade: "))
              curso= str(input("curso: "))
          except ValueError:
              print("invalido")

          add_1=classm.add(nome, idade, curso)
          print(add_1)
    elif msg== "listar":
        all_1= repository.select_all()
        for i in all_1:
            print(f"id: {i[0]}, nome: {i[1]}, idade: {i[2]}, curso: {i[3]}")
    elif msg=="buscar":
        try:
            nome= str(input("nome: "))
            idade= int(input("idade: "))
        except ValueError:
            print("invalido")
        print(classm.busc(nome, idade))
    elif msg=="atualizar":
        try:
            name= str(input("nome: "))
            idd= int(input("idade: "))
            print("nome")
            print("idade")
            print("curso")
            ds= str(input("o que voce quer mudar? "))
            ds_1= str(input(f"para qual {ds} voce quer mudar? "))
        except ValueError:
            print("invalido")
        upt= classm.updt(name, idd, ds, ds_1)
        print(upt)
    elif msg == "deletar":
        try:
            nome= str(input("nome: "))
            idade= int(input("idade: "))
        except ValueError:
            print("invalido")
        del_1= classm.del_1(nome, idade)
        print(del_1)

        

        

 
       


        

        

       
          
              
     
          

    

    







