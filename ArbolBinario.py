import Tkinter as tk

root = tk.Tk()
root.title("Arboles binarios")
root.geometry("750x500")
tf = []
var = []
label = []
frame=tk.Frame(root,width=720,height=400)
frame.pack(expand=True,fill="both")
lienzo = tk.Canvas(frame,width=720,height=480,background="#fafad2")
lienzo.config(width=720,height=380)
lienzo.pack(side="left",expand=True)
lienzo.place(x=10,y=10)


class Nodo:
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
        
class Arbol:
    __raiz = None
    __contx = 300
    __conty = 10
    __i = 0
    def __init__(self):
        self.__raiz = None
        
    def raizarbol(self):
        return self.__raiz
    
    def inorden(self,raiz):
        if raiz != None:
            self.inorden(raiz.rIzq())
            print(str(raiz.info()))
            self.inorden(raiz.rDer())
            
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
            
    def contar(self,raiz):
        if raiz != None:
            cont = self.contar(raiz.rIzq()) + 1
            cont1 = self.contar(raiz.rDer()) + 1
            if cont > cont1:
                return cont
            else:
                return cont1
                
    def niveles(self,raiz,n):
        if raiz != None:
            if n == 0:
                print(raiz.info())
            self.niveles(raiz.rIzq(),n-1)
            self.niveles(raiz.rDer(),n-1)
    def insertar(self,nodo):
        if self.__raiz == None:
            self.__raiz = nodo
            return
        
        p = self.__raiz;
        
        while p != None:
            q = p
            if nodo.info()<p.info():
                p = p.rIzq()
            elif nodo.info()>p.info():
                p = p.rDer()
            else:
                print("Numero repetido: "+str(nodo.info()))
                return
            
        if nodo.info()<q.info():
            q.cambiar_izq(nodo)
        else:
            q.cambiar_der(nodo)
            
    def borrarNodo(self,q,p):
        if p.rIzq() == None:
            r = p.rDer()
        elif p.rDer() == None:
            r = p.rIzq()
        else:
            s = p
            r = p.rDer()
            t = r.rIzq()
            while t != None:
                s = r
                r = t
                t = t.rIzq()
                
            if p != s:
                s.cambiar_izq(r.rDer())
                r.cambiar_der(p.rDer())
            r.cambiar_izq(p.rIzq())
        
        if q==None:
            self.__raiz = r
        elif p == q.rIzq():
            q.cambiar_izq(r)
        else:
            q.cambiar_der(r)
        print("Eliminado: " + str(p.info()))
        p = None
        
    def pintar(self,raiz):
        if raiz != None:
            lienzo.create_oval(self.__contx,self.__conty,self.__contx+30,self.__conty+30)
            lienzo.create_text(self.__contx+16,self.__conty+20, text=str(raiz.info()))
            if raiz.rIzq()!=None:
                lienzo.create_line(self.__contx+15,self.__conty+30,self.__contx-35,self.__conty+50)
            if raiz.rDer()!=None:
                lienzo.create_line(self.__contx+15,self.__conty+30,self.__contx+65,self.__conty+50)
            self.__conty=self.__conty+50
            self.__contx=self.__contx-50
            self.pintar(raiz.rIzq())
            self.__contx=self.__contx+100
            self.pintar(raiz.rDer())
            self.__conty=self.__conty-50
            self.__contx=self.__contx-50
            #self.preorden(raiz.rIzq())
            #self.preorden(raiz.rDer())
'''   
class NodoCola:
    def __init__(self,v):
        self.__info = v
        self.__sig = None
        
    def cambiar_sig(self,direcc):
        self.__sig = direcc
        
    def traer_info(self):
        return self.__info

    def traer_sig(self):
        return self.__sig
    
class CCola:
    def __init__(self):
        self.__cola = NodoCola("nodo cabeza de la cola")
        self.__cola.cambiar_sig(self.__cola)
        
    def ins_cola(self,nodo_arbol):
        nuevo = NodoCola(nodo_arbol)
        nuevo.cambiar_sig(self.__cola.traer_sig())
        
        self.__cola.cambiar_sig(nuevo)
        self.__cola = nuevo
        
    def retirar_cola(self):
        if self.__cola.traer_sig() == self.__cola:
            print("Cola vacia...")
            return None
        q = self.__cola.traer_sig()
        r = q.traer_sig()
        temp = r.traer_info()
        q.cambiar_sig(r.traer_sig())
        
        if q == q.traer_sig():
            self.__cola = q
        return temp
    
    def vacia(self):
        if self.__cola.traer_sig() == self.__cola:
            return True
        return False
'''    
    
op = 99
ar = Arbol()

def pintar():
    ar.pintar(ar.raizarbol())

lis = tk.Button(root,text="Dibujar", height = 2, width = 10, command=pintar)
lis.pack()
lis.place(x=20,y=410)

while op != 0:
    print("\n¿Qué desea hacer?\n"
          "1. Insertar un número\n"
          "2. Listar en inorden\n"
          "3. Listar en preorden\n"
          "4. Listar en postorden\n"
          "5. Listar por niveles\n"
          "6. Eliminar un nodo\n"
          "7. Pintar el arbol\n"
          "0. Salir")
    op = int(input("Digite la opcion: "))
    
    if(op==1):
        dato = int(input("Digite el numero a insertar: "))
        nodo = Nodo(dato)
        ar.insertar(nodo)
    elif(op==2):
        ar.inorden(ar.raizarbol())
    elif(op==3):
        ar.preorden(ar.raizarbol())
    elif(op==4):
        ar.posorden(ar.raizarbol())
    elif(op==5):
        niv = int(input("Ingrese el nivel limite que desea listar: "))
        for i in range(niv+1):
            ar.niveles(ar.raizarbol(),i)
            print("")
    elif(op==6):
        p = ar.raizarbol()
        q = None
        dato = int(input("Digite numero a borrar del arbol: "))
        
        while p!=None:
            if dato<p.info():
                q = p
                p = p.rIzq()
            elif dato>p.info():
                q = p
                p = p.rDer()
            else: break
        
        if p==None:
            print("No existe número: "+str(dato))
        else:
            ar.borrarNodo(q,p)
    elif(op==7):
        root.mainloop()
    elif(op==0):
        print("Calabaza, calabaza")