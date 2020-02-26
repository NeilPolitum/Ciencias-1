import Tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")
root.title("Dibujar Lineas")
p = []
lienzo = tk.Canvas(root,width=800,height=9000,background="#fafad2")
lienzo.pack()
lienzo.place(x=0,y=0)


var = []
label = []
tf = []

for i in range(6):
    tf.append(tk.Entry(root, width = 20))

tf[0].pack()
tf[0].place(x=173,y=31)

tf[1].pack()
tf[1].place(x=174,y=101)

tf[2].pack()
tf[2].place(x=174,y=124)

tf[3].pack()
tf[3].place(x=174,y=201)

tf[4].pack()
tf[4].place(x=174,y=224)

tf[5].pack()
tf[5].place(x=174,y=301)

class Nodo:
    def __init__(self, info):
        self.__info = info
        self.__sig = None
        self.__abajo = None
        
    def info(self):
        return self.__info
        
    def sig(self):
        return self.__sig
        
    def abajo(self):
        return self.__abajo
        
    def cambiar_sig(self, direcc):
        self.__sig = direcc
            
    def cambiar_abajo(self, direcc):
        self.__abajo = direcc
            
class Multilista:
    __cab = None
    
    __var1 = []
    __label1 = []
    __pos = 0
    __var2 = []
    __label2 = []
    __pos2 = 0
    def __init__(self):
        self.__cab = None
    def ingresar_materia(self, materia):
        if self.__cab == None:
            self.__cab = materia
            print("Ingresada la materia")
            return
        
        q = None
        p = self.__cab
        while p != None and p.info() != materia.info():
            q = p
            p = p.sig()
            
        if p != None and p.info() == materia.info():
            print ("Ya esta en la lista")
            return
        
        q.cambiar_sig(materia)
        
    def ingresar_alumno(self, materia, nombre):
        p = self.__cab
        
        while p != None and p.info() != materia.info():
            p = p.sig()
        
        if p == None:
            print("No existe la materia")
            return
            
        q = p.abajo()
        s = p
        while q != None:
            s = q
            q = s.abajo()
        s.cambiar_abajo(nombre)
        print("Ingresado el alumno") 
        
    def retirar_materia(self, materia):
        p = self.__cab
        q = None
        while p != None and p.info() != materia.info():
            q = p
            p = p.sig()
            
        if p.abajo() != None:
            print("No se puede eliminar materia, hay estudiantes matriculados")
            return
            
        if p != None and q == None:
            self.__cab = p.sig()
            print ("Eliminada correctamente")
            return
        
        if p != None and q != None:
            q.cambiar_sig(p.sig())
            print("Eliminada correctamente")
            return
        
        print("No se encontró la materia")
        
    def retirar_alumno(self, materia, alumno):
        p = self.__cab
        
        while p != None and p.info() != materia.info():
            p = p.sig()
        
        if p == None:
            print("No existe la materia")
            return
        
        q = p.abajo()
        
        while q.info() != alumno.info() and q!= None:
            p = q
            q = q.abajo()
        
        if q == None:
            print("No existe el alumno")
            return 
        
        p.cambiar_abajo(q.abajo())
        print("Eliminado correctamente")
        
    def imprimir(self):
        for i in range(self.__pos):
            self.__var1[i].set("")
            self.__var2[i].set("")
        s = self.__cab
        contx = 100
        while s != None:
            conty = 600
            conty2 = 630
            self.__var1.append(tk.StringVar())
            self.__label1.append(tk.Label(root, textvariable = self.__var1[self.__pos], bg = "lightblue"))
            self.__var1[self.__pos].set(str(s.info()))
            self.__label1[self.__pos].pack()
            self.__label1[self.__pos].place(x = contx, y = conty)
            
            self.__var2.append(tk.StringVar())
            self.__label2.append(tk.Label(root, textvariable = self.__var2[self.__pos2], bg = "#CF83B6"))
            self.__var2[self.__pos2].set("---->")
            self.__label2[self.__pos2].pack()
            self.__label2[self.__pos2].place(x = contx+50, y = conty)
            
            q = s.abajo()
            self.__pos += 1
            self.__pos2 +=1
            while q!= None:
                self.__var1.append(tk.StringVar())
                self.__label1.append(tk.Label(root, textvariable = self.__var1[self.__pos], bg = "white"))
                self.__var1[self.__pos].set(str(q.info()))
                self.__label1[self.__pos].pack()
                self.__label1[self.__pos].place(x = contx, y = 100+conty)
                
                self.__var2.append(tk.StringVar())
                self.__label2.append(tk.Label(root, textvariable = self.__var2[self.__pos2], bg = "#CF83B6"))
                self.__var2[self.__pos2].set("|\n|\n|")
                self.__label2[self.__pos2].pack()
                self.__label2[self.__pos2].place(x = contx+18, y = conty2)
                
                conty += 100
                conty2 += 100
                q = q.abajo()
                self.__pos += 1
                self.__pos2 += 1
            contx += 100
            s = s.sig()

multi = Multilista()

def ingM():
    mat = tf[0].get()
    nodo = Nodo(mat)
    multi.ingresar_materia(nodo)
def ingA():
    mat = tf[1].get()
    alu = tf[2].get()
    nodoMat = Nodo(mat)
    nodoAlu = Nodo(alu)
    multi.ingresar_alumno(nodoMat, nodoAlu)
def retA():
    mat = tf[3].get()
    alu = tf[4].get()
    nodoMat = Nodo(mat)
    nodoAlu = Nodo(alu)
    multi.retirar_alumno(nodoMat, nodoAlu)
def retM():
    mat = tf[5].get()
    nodo = Nodo(mat)
    multi.retirar_materia(nodo)

for i in range(10):
    var.append(tk.StringVar())
    label.append(tk.Label(root, textvariable = var[i], borderwidth = 2))

#labels
label[0].pack()
label[0].place(x=0,y=0)
var[0].set("Materias")
label[0].config(font = ("Courier",14), relief = "groove", width=15)

label[1].pack()
label[1].place(x=0,y=29)
var[1].set("Ingrese el nombre de la materia")

label[2].pack()
label[2].place(x=0,y=70)
var[2].set("Alumnos")
label[2].config(font = ("Courier",14), relief = "groove", width=15)

label[3].pack()
label[3].place(x=0,y=99)
var[3].set("Ingrese el nombre de la materia")

label[4].pack()
label[4].place(x=0,y=122)
var[4].set("Ingrese el nombre del alumno")

label[5].pack()
label[5].place(x=0,y=170)
var[5].set("Retirar alumnos")
label[5].config(font = ("Courier",14), relief = "groove", width=15)

label[6].pack()
label[6].place(x=0,y=199)
var[6].set("Ingrese el nombre de la materia")

label[7].pack()
label[7].place(x=0,y=222)
var[7].set("Ingrese el nombre del alumno")

label[8].pack()
label[8].place(x=0,y=270)
var[8].set("Retirar materia")
label[8].config(font = ("Courier",14), relief = "groove", width=15)

label[9].pack()
label[9].place(x=0,y=299)
var[9].set("Ingrese el nombre de la materia")



bt1 = tk.Button(root,text="Insertar materia", command=ingM)
bt1.pack()
bt1.place(x=340,y=27)

bt2 = tk.Button(root,text="Insertar alumno", command=ingA)
bt2.pack()
bt2.place(x=340,y=110)

bt3 = tk.Button(root,text="Retirar alumno",command=retA)
bt3.pack()
bt3.place(x=340,y=210)

bt4 = tk.Button(root,text="Retirar materia",command=retM)
bt4.pack()
bt4.place(x=340,y=297)

bt5 = tk.Button(root,text="Listar",command=multi.imprimir, height = 2, width = 10)
bt5.pack()
bt5.place(x=500,y=170)

root.mainloop()