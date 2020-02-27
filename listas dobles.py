import tkinter as tk

#Interfaz
root = tk.Tk()
root.geometry("500x600")
root.title("Listas dobles")
lienzo = tk.Canvas(root,width=500,height=450,background="#fafad2")
lienzo.pack()
lienzo.place(x=0,y=150)
tf = tk.Entry(root,width = 20)
var = tk.StringVar(value="Ingrese el numero:")
label = tk.Label(root,textvariable = var)
label.pack()
label.place(x=10,y=30)
tf.pack()
tf.place(x=115,y=32)


# Lógica
class Nodo_Dobles:
    def __init__(self, info):
        self.__info = info
        self.__sig = None
        self.__ant = None
        
    def info(self):
        return self.__info

    def sig(self):
        return self.__sig
    
    def ant(self):
        return self.__ant
    
    def cambiar_sig(self, direcc):
        self.__sig = direcc
        
    def cambiar_ant(self, direcc):
        self.__ant = direcc
        
class Lista_Doble():
    __cablista_doble = None
    def __init__(self):
        self.__cablista_doble = None
        
    def insertar_Doble(self, nodo):
        if self.__cablista_doble == None:
            self.__cablista_doble = nodo
            print("Se insertó {} en la cabeza".format(nodo.info()))
            return
        
        q = None
        p = self.__cablista_doble
        
        while p!=None and p.info()<nodo.info():
            q = p
            p = p.sig()
            
        if p!=None and p.info()==nodo.info():
            print("{} ya esta en la lista".format(nodo.info()))
            return
        
        print("Se insertó "+str(nodo.info()))
        if p==None:
            q.cambiar_sig(nodo)
            nodo.cambiar_ant(q)
        elif p.info()<nodo.info():
            p.cambiar_sig(nodo)
            nodo.cambiar_ant(p)
        else:
            nodo.cambiar_sig(p)
            nodo.cambiar_ant(q)
            p.cambiar_ant(nodo)
            if q!=None:
                q.cambiar_sig(nodo)
            else:
                self.__cablista_doble = nodo
    
    def escribir_lista_Doble(self):
        print("Hacia adelante")
        ult = None
        p = self.__cablista_doble
        
        while p!=None:
            ult = p
            print(p.info())
            p = p.sig()
        
        print("Hacia atrás")
        
        while ult!=None:
            print(ult.info())
            ult = ult.ant()
            
    def buscar_lista_Doble(self, numero):
        comprobar = False
        p = self.__cablista_doble
        
        while p!=None:
            if p.info()==numero:
                comprobar = True
                break
            p = p.sig()
        
        if comprobar:
            print(str(numero)+" Si existe")
        else:
            print(str(numero)+" No existe")
    
    def retirar_lista_Doble(self, numero):
        if self.__cablista_doble==None:
            print("{}".format("Lista Vacia"))
            return
        p = self.__cablista_doble
        
        if p.sig()==None and p.ant()==None:
            if p.info()==numero:
                self.__cablista_doble = None
                print("retirada la llave {}".format(numero))
            else:
                print ("No existe la llave {}".format(numero))
            return
        q = None
        
        while p!=None and p.info()<numero:
            q = p
            p = p.sig()
            
        if p==None:
            print("No existe la llave {}".format(numero))
            return
        
        if p.info()==numero:
            if q!=None:
                q.cambiar_sig(p.sig())
                s = p.sig()
                if s!=None:
                    s.cambiar_ant(q)
                p = None
            else:
                s = p.sig()
                self.__cablista_doble = p.sig()
                s.cambiar_ant(None)
                p = None
            
            print("retirada la llave {}".format(numero))
        else:
            print("No existe la llave {}".format(numero))

lista=Lista_Doble()

def insBut():
    dato=tf.get()
    nodo=Nodo_Dobles(dato)
    lista.insertar_Doble(nodo)
    
def retBut():
    dato=tf.get()
    lista.retirar_lista_Doble(dato)
    
def busBut():
    dato=tf.get()
    lista.buscar_lista_Doble(dato)
      
ins=tk.Button(root, text="Insertar", command=insBut)
ins.pack()
ins.place(x=250,y=30,width=50,height=20)
ret= tk.Button(root, text="Retirar", command=retBut)
ret.pack()
ret.place(x=250,y=60,width=50,height=20)
bus=tk.Button(root, text="Buscar", command=busBut)
bus.pack()
bus.place(x=250,y=90,width=50,height=20)
dib=tk.Button(root, text="Dibujar")
dib.pack()
dib.place(x=250,y=120,width=50,height=20)

root.mainloop()

