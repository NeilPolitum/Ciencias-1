import Tkinter as tk
'''
def posicion(event):
    global p
    p.append(str(event.x) + "," + str(event.y))
    lienzo.create_oval(event.x,event.y,event.x+3,event.y+3,fill="midnight blue",outline="yellow",width=1)
'''
        
def salir():
    root.destroy()
    

class Nodo:
    def __init__(self, info):
        self.__info = info
        self.__sig = None
        
    def info(self):
        return self.__info
    
    def sig(self):
        return self.__sig
    
    def cambiar_sig(self,direcc):
        self.__sig = direcc
        
class Lista():
    __cab = None
    
    __var = []
    __label = []
    __pos = 0

    def __init__(self):
        self.__cab = None
        
    def insertar(self, nodo):
        if self.__cab == None:
            self.__cab = nodo
            return
        
        q = None
        p = self.__cab
        while p != None and p.info() < nodo.info():
            q = p
            p = p.sig()
            
        if p != None and p.info() == nodo.info():
            print ("{nodo.info()} ya esta en la lista")
            return
        
        if q == None:
            nodo.cambiar_sig(p)
            self.__cab = nodo
            return
        
        nodo.cambiar_sig(p)
        q.cambiar_sig(nodo)
        
    def escribir_lista(self):
        p = self.__cab
        while p != None:
            print (p.info())
            p = p.sig()
            
    def buscar(self, nodo):
        p = self.__cab
        q = p
        while q != None :
            if q.info()==nodo:
                return True
            else:
                q=q.sig()
        return False
    
    def retirar(self, nodo):
        p = self.__cab
        q = None
        while p != None and p.info() != nodo.info():
            q = p
            p = p.sig()
            
        if p != None and q == None:
            self.__cab = p.sig()
            return
        
        if p != None and q != None:
            q.cambiar_sig(p.sig())
            return
        
        print("No se encontró el número")
        
    def dibujar(self):
        global var, label, pos
        p = self.__cab
        while p != None:
            self.__var.append(tk.StringVar())
            self.__label.append(tk.Label(root, textvariable = self.__var[self.__pos], bg = "white", width = 12))
            self.__var[self.__pos].set(p.info())
            self.__label[self.__pos].pack()
            self.__label[self.__pos].place(x = self.__pos*95, y = 50)
            self.__pos += 1
            
            self.__var.append(tk.StringVar())
            self.__label.append(tk.Label(root, textvariable = self.__var[self.__pos], bg = "grey"))
            self.__var[self.__pos].set("----->")
            self.__label[self.__pos].pack()
            self.__label[self.__pos].place(x = self.__pos*95, y = 50)
            p = p.sig()
            self.__pos += 1
        self.__var[self.__pos-1].set("")

lista = Lista()

root = tk.Tk()
root.geometry("1600x300")
root.title("Dibujar Lineas")
p = []
lienzo = tk.Canvas(root,width=1580,height=290,background="#fafad2")
lienzo.pack()
lienzo.place(x=0,y=0)
bt = tk.Button(root,text="Dibujar",command=lista.dibujar)
bt.pack()
bt.place(x=0,y=110)

bt2 = tk.Button(root,text="Salir",command=salir)
bt2.pack()
bt2.place(x=110,y=110)

    
print("Bienvenido, por favor ingrese una lista: ")

dato = int(input("Digite numero a insertar. (-1) para terminar: "))
while dato != -1:
    nodo = Nodo(dato)
    lista.insertar(nodo)
    dato = int(input("Digite numero a insertar. (-1) para terminar: "))

op = 1
while op != 0:
    op = int(input("Qué desea hacer?:\n"
               "1. Ver la lista\n"
               "2. Insertar número en la lista\n"
               "3. Retirar número en la lista\n"
               "4. Dibujar la lista\n"
               "0. Salir\n"))
    
    if op == 1:
        print("\n")
        lista.escribir_lista()
    elif op == 2:
        dato = int(input("Digite numero a insertar: "))
        nodo = Nodo(dato)
        lista.insertar(nodo)
    elif op == 3:
        dato = int(input("Digite numero a retirar: "))
        nodo = Nodo(dato)
        lista.retirar(nodo)
    #elif op == 4:
root.mainloop()