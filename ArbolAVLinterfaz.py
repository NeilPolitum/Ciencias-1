arbolAlumno = []
arbolMateria = []


import Tkinter as tk
import tkMessageBox

root = tk.Tk()
root.title("Arboles AVL")
root.geometry("750x700")
tf = []
var = []
label = []
frame=tk.Frame(root,width=720,height=380)
frame.pack(expand=True,fill="both")
lienzo = tk.Canvas(frame,width=720,height=380,background="#fafad2", scrollregion=(0,0,1500,1500))
barra_h = tk.Scrollbar(frame, orient="horizontal")
barra_h.pack(side="bottom", fill="x")
barra_h.config(command=lienzo.xview)
barra_v = tk.Scrollbar(frame, orient="vertical")
barra_v.pack(side="right", fill="y")
barra_v.config(command=lienzo.yview)
lienzo.config(xscrollcommand=barra_h.set, yscrollcommand=barra_v.set)
lienzo.config(width=720,height=380)
lienzo.pack(side="left",expand=True)
lienzo.place(x=10,y=300)

for i in range(6):
    tf.append(tk.Entry(root, width = 20))

for i in range(9):
    var.append(tk.StringVar())
    label.append(tk.Label(root, textvariable = var[i], borderwidth = 2))

tf[0].pack()
tf[0].place(x=222,y=61)

tf[1].pack()
tf[1].place(x=222,y=86)

tf[2].pack()
tf[2].place(x=222,y=111)

tf[3].pack()
tf[3].place(x=222,y=161)

tf[4].pack()
tf[4].place(x=222,y=186)

tf[5].pack()
tf[5].place(x=222,y=211)

label[0].pack()
label[0].place(x=0,y=0)
var[0].set("Entidad Relacion con arboles AVL")
label[0].config(font = ("Courier",14), relief = "groove", width=40)

label[3].pack()
label[3].place(x=0,y=30)
var[3].set("Alumnos")
label[3].config(font = ("Courier",14), relief = "groove", width=15)

label[1].pack()
label[1].place(x=0,y=59)
var[1].set("Ingrese el nombre del arbol de alumnos")

label[2].pack()
label[2].place(x=0,y=84)
var[2].set("Ingrese el codigo del alumno")

label[4].pack()
label[4].place(x=0,y=109)
var[4].set("Ingrese el nombre del alumno")

label[5].pack()
label[5].place(x=0,y=159)
var[5].set("Ingrese el nombre del arbol de materias")

label[6].pack()
label[6].place(x=0,y=134)
var[6].set("Materias")
label[6].config(font = ("Courier",14), relief = "groove", width=15)

label[7].pack()
label[7].place(x=0,y=184)
var[7].set("Ingrese el codigo de la materia")

label[8].pack()
label[8].place(x=0,y=209)
var[8].set("Ingrese el nombre de la materia")

##################################################################################################

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.__izq, self.__der, self.__padre = None, None, None
        self.peso = 0
        
    def cambiar_dato(self,num):
        self.dato = num
        
    def izq(self):
        return self.__izq
    
    def cambiar_izq(self, direcc):
        if direcc is not None:
            direcc.__padre = self
            self.__izq = direcc
    
    def der(self):
        return self.__der
        
    def cambiar_der(self, direcc):
        if direcc is not None:
            direcc.__padre = self
            self.__der = direcc
    
    def padre(self):
        return self.__padre
        
    def cambiar_padre(self, direcc):
        if direcc is not None:
            self.__padre = direcc
            self.peso = self.padre.peso + 1
        else:
            self.peso = 0
    
    def cambiar_peso(self, num):
        self.peso = num
            
class ArbolAVL:
    def __init__(self, nombreA):
        self.raiz = None
        self.tamano = 0
        self.nombreArbol = nombreA
        self.codigo = []
        self.nombre = []
        
        
    def insertarNodo(self, num, nom):
        longitud = len(self.codigo)
        for i in range(longitud):
            if num == self.codigo[i]:
                print("El código ya existe.")
                return
        
        self.codigo.append(num)
        self.nombre.append(nom)
        nodo = Nodo(num)
        if self.raiz is None:
            self.raiz = nodo
            self.raiz.cambiar_peso(0)
            self.tamano = 1
            print("Agregado correctamente")
            tkMessageBox.showinfo("prekauzion", "Agregado correctamente")
        else:
            padreNodo = None
            nodoActual = self.raiz
            
            while True:
                if nodoActual is not None:
                    padreNodo = nodoActual
                    if nodo.dato<nodoActual.dato:
                        nodoActual = nodoActual.izq()
                    else:
                        nodoActual = nodoActual.der()
                else:
                    nodo.cambiar_peso(padreNodo.peso)
                    padreNodo.cambiar_peso(padreNodo.peso+1)
                    if nodo.dato < padreNodo.dato:
                        padreNodo.cambiar_izq(nodo)
                    else:
                        padreNodo.cambiar_der(nodo)
                    self.rebalancear(nodo)
                    print("Agregado correctamente")
                    tkMessageBox.showinfo("prekauzion", "Agregado correctamente")
                    self.tamano += 1
                    break
    
    def eliminarNodo(self, codA):
        nodoActual = self.getRaiz()
        padreNodo = None
        nodo = Nodo(codA)
        
        while nodoActual.dato != None:
            if nodo.dato<nodoActual.dato:
                padreNodo = nodoActual
                nodoActual = nodoActual.izq()
            elif nodo.dato>nodoActual.dato:
                padreNodo = nodoActual
                nodoActual = nodoActual.der()
            else: break
            
        if nodoActual == None:
            print("No existe el codigo.")
            tkMessageBox.showinfo("prekauzion", "No existe el codigo")
        else:
            if nodoActual.izq() == None:
                r = nodoActual.der()
            elif nodoActual.der() == None:
                r = nodoActual.izq()
            else:
                s = nodoActual
                r = nodoActual.der()
                t = r.izq()
                while t != None:
                    s = r
                    r = t
                    t = t.izq()
                
                if nodoActual != s:
                    s.cambiar_izq(r.der())
                    r.cambiar_der(nodoActual.der())
                r.cambiar_izq(nodoActual.izq())
        
            if padreNodo==None:
                self.raiz = r
            elif nodoActual == padreNodo.izq():
                padreNodo.cambiar_izq(r)
            else:
                padreNodo.cambiar_der(r)
            """
            longitud = len(self.codigo)
            
            for i in range(longitud):
                if nodoActual.dato == self.codigo[i]:
                    del(self.codigo[i])
                    del(self.nombre[i])
                    break
            """
            self.rebalancear(nodo)
            nodoActual = None
    
    def rebalancear(self,nodo):
        n = nodo
        while n is not None:
            pesoDerecha = n.peso
            pesoIzquierda = n.peso
            
            if n.der() is not None:
                pesoDerecha = n.der().peso
                
            if n.izq() is not None:
                pesoIzquierda = n.izq().peso
                
            if abs(pesoIzquierda - pesoDerecha) > 1:
                if pesoIzquierda > pesoDerecha:
                    hijoIzquierda = n.izq()
                    if hijoIzquierda is not None:
                        pDer = (hijoIzquierda.der().peso
                                if (hijoIzquierda.der() is not None) else 0)
                        pIzq = (hijoIzquierda.izq().peso
                                if (hijoIzquierda.izq() is not None) else 0)
                    if (pIzq > pDer):
                        self.rotarIzquierda(n)
                        break
                    else:
                        self.dobleRotarDerecha(n)
                        break
                else:
                    hijoDerecha = n.der()
                    if hijoDerecha is not None:
                        pDer = (hijoDerecha.der().peso
                                if (hijoDerecha.der() is not None) else 0)
                        pIzq = (hijoDerecha.izq().peso
                                if (hijoDerecha.izq() is not None) else 0)
                    if (pIzq > pDer):
                        self.dobleRotarIzquierda(n)
                        break
                    else:
                        self.rotarDerecha(n)
                        break
            n = n.padre()
            
    def rotarIzquierda(self, nodo):
        aux = nodo.padre().dato
        nodo.padre().cambiar_dato(nodo.dato)
        nodo.padre().cambiar_der(Nodo(aux))
        nodo.padre().der().cambiar_peso(nodo.padre().peso + 1)
        nodo.padre().cambiar_izq(nodo.der())
        
    def rotarDerecha(self, nodo):
        aux = nodo.padre().dato
        nodo.padre().cambiar_dato(nodo.dato)
        nodo.padre().cambiar_izq(Nodo(aux))
        nodo.padre().izq().cambiar_peso(nodo.padre().peso + 1) 
        nodo.padre().cambiar_der(nodo.der())
        
    def dobleRotarIzquierda(self, nodo):
        self.rotarDerecha(nodo.der().der())
        self.rotarIzquierda(nodo)
    
    def dobleRotarDerecha(self, nodo):
        self.rotarIzquierda(nodo.izq().izq())
        self.rotarDerecha(nodo)
        
    def vacio(self):
        if self.raiz is None:
            return True
        return False
    
    def mostrar(self, nodoActual):
        if nodoActual is not None:
            self.mostrar(nodoActual.izq())
            longi = len(self.codigo)
            for i in range(longi):
                if nodoActual.dato == self.codigo[i]:
                    aux = i
            print("Código: "+str(nodoActual.dato)+", Nombre: "+self.nombre[aux]+", Peso: "+str(nodoActual.peso))
            self.mostrar(nodoActual.der())
            
    def preordenar(self, nodoActual):
        if nodoActual is not None:
            self.mostrar(nodoActual.izq())
            self.mostrar(nodoActual.der())
            print(nodoActual.dato)
            
    def getRaiz(self):
        return self.raiz
    
    def getNombre(self):
        return self.nombreArbol
    
class ManejoArbol:
    def __init__(self):
        self.__posicion = None

    def ingresarArbol(self, nombre, tipo):
        if tipo == 1:  
            longi = len(arbolAlumno)
            if longi == 0:
                arbol = ArbolAVL(nombre)
                arbolAlumno.append(arbol)
                print("Ingresado correctamente")
                tkMessageBox.showinfo("PREKAUZION", "Ingresado correctamente")
            else:   
                for i in range(longi):
                    if nombre == arbolAlumno[i].getNombre():
                        print("Ya existe un arbol con ese nombre")
                        tkMessageBox.showinfo("prekauzion", "Ya existe un arbol con ese nombre")
                        return
                    arbol = ArbolAVL(nombre)
                    arbolAlumno.append(arbol)
                    print("Ingresado correctamente")
                    tkMessageBox.showinfo("prekauzion", "Ingresado correctamente")
        else:
            longi = len(arbolMateria)
            if longi == 0:
                arbol = ArbolAVL(nombre)
                arbolMateria.append(arbol)
                print("Ingresado correctamente")
                tkMessageBox.showinfo("prekauzion", "Ingresado correctamente")
            else:   
                for i in range(longi):
                    if nombre == arbolMateria[i].getNombre():
                        print("Ya existe un arbol con ese nombre")
                        tkMessageBox.showinfo("Ya existe un arbol con ese nombre", "Ingresado correctamente")
                        return
                    arbol = ArbolAVL(nombre)
                    arbolMateria.append(arbol)
                    print("Ingresado correctamente")
                    tkMessageBox.showinfo("prekauzion", "Ingresado correctamente")
            
    def existeArbol(self, nombre, tipo):
        if tipo == 1:
            longi = len(arbolAlumno)
            if longi == 0:
                print("No existe el arbol.")
                tkMessageBox.showinfo("No existe el arbol", "Ingresado correctamente")
                return False
            else:   
                for i in range(longi):
                    if nombre == arbolAlumno[i].getNombre():
                        self.__posicion = i
                        return True
                    print("No existe el arbol")
                    tkMessageBox.showinfo("prekauzion", "No existe el arbol")
                    return False
        else:
            longi = len(arbolMateria)
            if longi == 0:
                print("No existe el arbol.")
                tkMessageBox.showinfo("prekauzion", "No existe")
                return False
            else:   
                for i in range(longi):
                    if nombre == arbolMateria[i].getNombre():
                        self.__posicion = i
                        return True
                    print("No existe el arbol")
                    tkMessageBox.showinfo("prekauzion", "No existe el arbol")
                    return False
    
    def getPosicion(self):
        return self.__posicion
    

op = 99
manejoArbol = ManejoArbol()
'''
while op != 0:
    print("\n¿Qué desea hacer pirobo hpta?\n"
          "1. Crear arbol de estudiantes\n"
          "2. Insertar un estudiante\n"
          "3. Retirar un estudiante\n"
          "4. Listar los estudiantes\n"
          "5. Crear arbol de materias\n"
          "6. Insertar una materia\n"
          "7. Retirar una materia\n"
          "8. Listar las materias\n"
          "0. Salir")
    op = int(input("Digite la opcion: "))
    
    if op == 1:
        nombre = raw_input("Ingrese el nombre del arbol: ")
        manejoArbol.ingresarArbol(nombre,1)
    
    elif op == 2:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,1):
            pos = manejoArbol.getPosicion()
            codA = int(input("Ingrese el codigo del alumno: "))
            nomA = raw_input("Ingrese el nombre del alumno: ")
            arbolAlumno[pos].insertarNodo(codA,nomA)
        
    elif op == 3:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,1):
            pos = manejoArbol.getPosicion()
            codA = int(input("Ingrese el codigo del alumno: "))
            arbolAlumno[pos].eliminarNodo(codA)
    
    elif op == 4:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,1):
            pos = manejoArbol.getPosicion()
            arbolAlumno[pos].mostrar(arbolAlumno[pos].getRaiz())
            
    elif op == 5:
        nombre = raw_input("Ingrese el nombre del arbol: ")
        manejoArbol.ingresarArbol(nombre,2)
    
    elif op == 6:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,2):
            pos = manejoArbol.getPosicion()
            codM = int(input("Ingrese el codigo del alumno: "))
            nomM = raw_input("Ingrese el nombre del alumno: ")
            arbolMateria[pos].insertarNodo(codM,nomM)
            
    elif op == 7:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,2):
            pos = manejoArbol.getPosicion()
            codM = int(input("Ingrese el codigo de la materia: "))
            arbolMateria[pos].eliminarNodo(codM)
    
    elif op == 8:
        arbol = raw_input("Ingrese el nombre del arbol: ")
        if manejoArbol.existeArbol(arbol,2):
            pos = manejoArbol.getPosicion()
            arbolMateria[pos].mostrar(arbolMateria[pos].getRaiz())
'''
#######################################################################################################

def inArA():
    nombre = tf[0].get()
    manejoArbol.ingresarArbol(nombre,1)

def inAl():
    arbol = tf[0].get()
    if manejoArbol.existeArbol(arbol,1):
        pos = manejoArbol.getPosicion()
        codA = tf[1].get()
        nomA = tf[2].get()
        arbolAlumno[pos].insertarNodo(codA,nomA)

def reAl():
    arbol = tf[0].get()
    if manejoArbol.existeArbol(arbol,1):
        pos = manejoArbol.getPosicion()
        codA = tf[1].get()
        arbolAlumno[pos].eliminarNodo(codA)
    
def liAl():
    return
    
def inArM():
    nombre = tf[3].get()
    manejoArbol.ingresarArbol(nombre,2)
    
def inMa():
    arbol = tf[3].get()
    if manejoArbol.existeArbol(arbol,2):
        pos = manejoArbol.getPosicion()
        codM = tf[4].get()
        nomM = tf[5].get()
        arbolMateria[pos].insertarNodo(codM,nomM)
    
def reMa():
    arbol = tf[3].get()
    if manejoArbol.existeArbol(arbol,2):
        pos = manejoArbol.getPosicion()
        codM = tf[4].get()
        arbolMateria[pos].eliminarNodo(codM)
    
def liMa():
    return
    


insArA = tk.Button(root,text="Crear arbol(alumnos)", width=16, command=inArA)
insArA.pack()
insArA.place(x=360,y=60)

insAl = tk.Button(root,text="Insertar alumno", width=16, command=inAl)
insAl.pack()
insAl.place(x=490,y=60)

retAl = tk.Button(root,text="Retirar alumno", width=16, command=reAl)
retAl.pack()
retAl.place(x=490,y=95)

lisAl = tk.Button(root,text="Listar alumnos", width=16, command=liAl)
lisAl.pack()
lisAl.place(x=360,y=95)

insArM = tk.Button(root,text="Crear arbol(materias)", width=16, command=inArM)
insArM.pack()
insArM.place(x=360,y=160)

insMa = tk.Button(root,text="Insertar materia", width=16, command=inMa)
insMa.pack()
insMa.place(x=490,y=160)

retMa = tk.Button(root,text="Retirar materia", width=16, command=reMa)
retMa.pack()
retMa.place(x=490,y=195)

lisMa = tk.Button(root,text="Listar materias", width=16, command=liMa)
lisMa.pack()
lisMa.place(x=360,y=195)

root.mainloop()