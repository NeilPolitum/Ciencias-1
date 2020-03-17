import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Reconstruccion de arboles")
var = []
label = []
for i in range(4):
    var.append(tk.StringVar())
    label.append(tk.Label(root, textvariable = var[i], borderwidth = 2))
    label[i].pack()
    
var[0].set("In-Order:")
label[0].place(x=150,y=20)
tfIn=tk.Entry(root,width=20)
tfIn.pack()
tfIn.place(x=210,y=20)

var[1].set("Pre:")
label[1].place(x=20,y=60)
tfPre=tk.Entry(root,width=20)
tfPre.pack()
tfPre.place(x=70,y=60)

var[2].set("Post:")
label[2].place(x=260,y=60)
tfPost=tk.Entry(root,width=20)
tfPost.pack()
tfPost.place(x=310,y=60)

frame=tk.Frame(root,width=460,height=250)
frame.pack(expand=True, fill="both") #.grid(row=0,column=0)
canvas=tk.Canvas(frame,bg='#FFFFFF',scrollregion=(0,0,1500,1500))
hbar=tk.Scrollbar(frame,orient="horizontal")
hbar.pack(side="bottom",fill="x")
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(frame,orient="vertical")
vbar.pack(side="right",fill="y")
vbar.config(command=canvas.yview)
canvas.config(width=460,height=250)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side="left",expand=True,fill="both")
frame.place(x=10,y=150)

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
        self.__contx=10
        self.__conty=10
        
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
        canvas.delete("all")
        self.dibujar(self.__raiz)
        
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
        canvas.delete("all")
        self.dibujar(self.__raiz)
    
    def dibujar(self,raiz,contx=10,conty=10,raizOrigen=Nodo(None)):
        if raiz != None:
            self.dibujar(raiz.rIzq(),contx,conty+40,raiz)
            p=raiz.rIzq()
            contx0=contx
            while p!=None:
                contx=contx+40
                p=p.rIzq()
            self.dibujar(raiz.rDer(),contx+40,conty+40,raiz)
            if raizOrigen.rIzq()==raiz:
                canvas.create_line(contx+40,conty-30,contx+10,conty,arrow="last")
            if raizOrigen.rDer()==raiz:
                canvas.create_line(contx0-20,conty-30,contx+10,conty,arrow="last")
            canvas.create_rectangle(contx,conty,contx+20,conty+20)
            canvas.create_text(contx+10,conty+10,text=str(raiz.info()))
            print(str(raiz.info()))
        
def inpr():
    ar = Arbol()
    inoS=tfIn.get()
    preS=tfPre.get()
    pre=preS.split(",")
    ino=inoS.split(",")
    ar.recArbolPre(ino,pre)
    tfIn.delete(0,'end')
    tfPre.delete(0,'end')
    
def inpo():
    ar=Arbol()
    inoS=tfIn.get()
    postS=tfPost.get()
    post=postS.split(",")
    ino=inoS.split(",")
    ar.recArbolPost(ino,post)
    tfIn.delete(0,'end')
    tfPost.delete(0,'end')
    
inpre = tk.Button(root, text="In-Pre", command=inpr)
inpre.pack()        
inpre.place(x=80,y=100)

inpost = tk.Button(root, text="In-Post", command=inpo)
inpost.pack()        
inpost.place(x=320,y=100)
                
root.mainloop()
'''    
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
        
'''
        
        