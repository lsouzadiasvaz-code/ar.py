import json
import os
try:
    with open("gastos_mensais", "r") as f:
        gastos_mensais=json.load(f)
except FileNotFoundError:
    gastos_mensais=[]
try:
    with open("gastos", "r") as f:
        gastos= json.load(f)
except FileNotFoundError:
    gastos_1=[]




def save():
    with open("gastos", "w", encoding="utf-8")as f:
        json.dump(gastos_1, f, indent=2, ensure_ascii=False)





def produto( produto, quantidade, preço):
   total= quantidade*preço
   gastos_1.append({"nome": produto, "quantidade": quantidade, "preço": preço, "total":total})

        
def busc(a):
    count=0
    for i in gastos_1:
        if i == gastos_1[count]["nome"]:
         return count
        else:
            count+=1

        return -1
        
      







print("cacular lucro")
print("adicionar produto")
print("remover produto")
print("buscar produto")
print("listar produtos")
print("atualizar produto")
print("apagar produto")
print("sair")
while True:
    try:
        msg= input(" o que voce deseja?")
    except ValueError:
        print("invalido")
    if msg == "sair":
        print("encerrado")
        break
    if msg == "adicionar produto":

        try:                   
           nm=input("nome: ")
           preço=float(input("preço: "))
           quantidade= int(input("quantidade: "))                  
         
        except ValueError:
            print("invalido")
    
    add_0= produto(nm, preço, quantidade)
    print("produto adicionado")
    save()
    if msg == "buscar produtos":
        try:
            nm=input("nome: ")
        except ValueError:
            print("invalido")
        
        busc_0= busc(nm)
        if busc_0<0:
            print("produto não encontrado")
        else:
            print(f"nome:{gastos_1[busc_0]["nome"]}, preço:{gastos_1[busc_0]["preço"]}, quantidade:{gastos_1[busc_0]["quantidade"]}, {gastos_1[busc_0]["total"]}")

        

        
                         



    
    



    
    