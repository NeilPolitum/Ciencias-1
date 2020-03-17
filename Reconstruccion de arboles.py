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
        
    def recArbolPre(self, inOrder, preOrder, raiz=None):
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
                p.cambiar_izq(self.recArbolPre(newIn,newPre,p))
                newIn = inOrder[inOrder.index(info)+1:]
                newPre = preOrder[inOrder.index(info)+1:]
                p.cambiar_der(self.recArbolPre(newIn,newPre,p))
                
        else:
            return None
        
        if raiz==None:
            self.__raiz = p
            
        else:
            return p
        
    def recArbolPost(self, inOrder, postOrder, raiz=None):
        
        print("-------------------------")
        print("Post:")
        for i in postOrder:
            print(i)
        
        print("In:")
        for i in inOrder:
            print(i)
        if len(inOrder)!=len(postOrder):
            print("Vectores con diferentes longitudes")
            return     
            
        if len(postOrder)>0:
            info=postOrder[len(postOrder)-1]
            p=Nodo(info)
            if len(postOrder)>1:
                newIn = inOrder[0:inOrder.index(info)]
                newPost = postOrder[0:inOrder.index(info)]        
                p.cambiar_izq(self.recArbolPost(newIn,newPost,p))
                newIn = inOrder[inOrder.index(info)+1:]
                newPost = postOrder[inOrder.index(info):-1]
                p.cambiar_der(self.recArbolPost(newIn,newPost,p))
                
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
          "5. Insertar en post\n"
          "0. Salir")
    op = int(input("Digite la opcion: "))
    
    if(op==1):
        ar=Arbol()
        preS = input("Preorder: ")
        inoS = input("Inorder: ")
        pre=preS.split(",")
        ino=inoS.split(",")
        ar.recArbolPre(ino,pre)
    elif(op==2):
        ar.inorden(ar.raizarbol())
    elif(op==3):
        ar.preorden(ar.raizarbol())
    elif(op==4):
        ar.posorden(ar.raizarbol()) 
    elif(op==5):
        ar=Arbol()
        postS = input("Postorder: ")
        inoS = input("Inorder: ")
        post=postS.split(",")
        ino=inoS.split(",")
        ar.recArbolPost(ino,post)           
    elif(op==0):
        print("Calabaza, calabaza, cada quien pa su gran puta mierda")
        
        
        
        