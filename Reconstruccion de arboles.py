import tkinter as tk

root = tk.Tk()
root.geometry("700x700")
root.title("Reconstruccion de arboles")

class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__izq, self.__der = None, None
        
    def info(self):
        return self.__dato
    
    def rIzq(self):
        return self.__izq
    
    def rDer(self):
        return self.__der
    
    def cambiar_izq(self, direcc):
        self.__izq = direcc
        
    def cambiar_der(self,direcc):
        self.__der = direcc

class Arbol():
    def __init__(self):
        self.__raiz=None
        
    def posorden(self, raiz):
        if raiz != None:
            self.posorden(raiz.rIzq())
            self.posorden(raiz.rDer())
            print(str(raiz.info()))
            
    def preorden(self,raiz):
        if raiz != None:
            print(str(raiz.info()))
            self.preorden(raiz.rIzq())
            self.preorden(raiz.rDer())
            
    def raizarbol(self):
        return self.__raiz
    
    def inorden(self,raiz):
        if raiz != None:
            self.inorden(raiz.rIzq())
            print(str(raiz.info()))
            self.inorden(raiz.rDer())
        
    def recArbol(self, inOrder, preOrder, raiz=None):
        if len(inOrder)!=len(preOrder):
            print("Vectores con diferentes longitudes")
            return     
        print("----------------------------------------------------------------")
        print("Pre:")
        for i in preOrder:
            print(i)
        
        print("In:")
        for i in inOrder:
            print(i)
            
        if len(preOrder)>0:
            info=preOrder[0]
            p=Nodo(info)
            if len(preOrder)>1:
                newIn = inOrder[0:inOrder.index(info)]
                newPre = preOrder[1:inOrder.index(info)+1]        
                p.cambiar_izq(self.recArbol(newIn,newPre,p))
                newIn = inOrder[inOrder.index(info)+1:]
                newPre = preOrder[inOrder.index(info)+1:]
                p.cambiar_der(self.recArbol(newIn,newPre,p))
                
        else:
            return None
        
        if raiz==None:
            self.__raiz = p
            
        else:
            return p
            
                
        
op = 99
ar = Arbol()
while op != 0:
    print("\n¿Qué desea hacer?\n"
          "1. Insertar un arbol\n"
          "2. Listar en inorden\n"
          "3. Listar en preorden\n"
          "4. Listar en postorden\n"
          "0. Salir")
    op = int(input("Digite la opcion: "))
    
    if(op==1):
        preS = input("Preorder: ")
        inoS = input("Inorder: ")
        pre=preS.split(",")
        ino=inoS.split(",")
        ar.recArbol(ino,pre)
    elif(op==2):
        ar.inorden(ar.raizarbol())
    elif(op==3):
        ar.preorden(ar.raizarbol())
    elif(op==4):
        ar.posorden(ar.raizarbol())            
    elif(op==0):
        print("Calabaza, calabaza, cada quien pa su gran puta mierda")
        
        
        
        