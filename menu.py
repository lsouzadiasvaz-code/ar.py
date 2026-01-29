import json


try:
 with open("funcionarios", "r") as f:
  lista = json.load(f)
except FileNotFoundError:
 lista = []

def add(a, b, c, d):
 lista.append({"nome": a, "idade":b, "cargo":c, "salario":d})

def salvar():
 with open("funcionarios", "w", encoding="utf-8") as f:
  json.dump(lista, f, ensure_ascii=False, indent=2)

def buscar(a):
 count = 0
 for i in lista:
  
  if a == lista[count]["nome"]:  
   return count
  else:
   count +=1
   
 return -1



   

print("adicionar")
print("deletar")
print("atualizar")
print("buscar")
print("listar")
print("sair")

while True:
 msg = input("o que voce deseja? ")
 if msg == "sair":
  print("encerrado")
  break
 elif msg == "adicionar":
  try:
   name = str(input("nome: "))
  except ValueError:
   print("nome invalido")
  try:
   age = int(input("idade: "))
  except ValueError:
   print("idade invalida")
  if age < 18:
   print("usuario e menor de idade")
  else:
   try:
    function = str(input("cargo: "))
   except ValueError:
    print("invalido")
   try:
    value = float(input("salario: "))
   except ValueError:
    print("salario invalido")
   add_user = add(name, age, function, value)
   print("usuario cadastrado")
   salvar()
 elif msg == "listar":
  for user in lista:
   for chave, valor in user.items():
    print(f"{chave}: {valor}")
 elif msg == "buscar":
  try:
   msg_search = str(input("nome "))
  except ValueError:
   print("nome invalido")
  search_user = buscar(msg_search)
  if search_user<0:
   print("usuario não encontrado")
  else:
   print(f"nome:{lista[search_user]["nome"]} idade:{lista[search_user]["idade"]} cargo:{lista[search_user]["cargo"]} salario:R${lista[search_user]["salario"]}")
 elif msg == "deletar":
  try:
   msg_del = str(input("nome: "))
  except ValueError:
   print("nome invalido")
  search_del = buscar(msg_del)
  if search_del<0:
   print("usuario ja não existia")
  else:
   del lista[search_del]
   print("usuario deletado")
   salvar()
 elif msg == "atualizar":
  try:
   msg_update = str(input("nome: "))
  except ValueError:
   print("nome invalido")
  search_update = buscar(msg_update)
  if search_update<0:
   print("usuario não encontrado")
  else:
   print("idade")
   print("cargo")
   print("salario")
   try:
    msg_update_1= str(input("qual voce quer mudar? "))
   except ValueError:
    print("invalido")
   if msg_update_1=="idade":
    try:
     msg_age= int(input("qual a nova idade? "))
    except ValueError:
     print("invalido")
    if msg_age <18:
     print("idade invalida")
    else:
     lista[search_update]["idade"]= msg_age
     print(f"idade de {msg_update} foi atualizada")
     salvar()
   elif msg_update_1=="cargo":
    try:
     msg_function= input("qual o novo cargo? ")
    except ValueError:
     print("invalido")
    lista[search_update]["cargo"]=msg_function
    print(f"o cargo de {msg_update} foi atualizado")
    salvar()
   elif msg_update_1=="salario":
    try:
     msg_value= float(input("qual o novo salario? "))
    except ValueError:
     print("invalido")
    lista[search_update]["salario"]= msg_value
    print(f"salario de {msg_update} foi atualizado")
    salvar()

  
  

 
     

   
  



