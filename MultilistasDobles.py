import Tkinter as tk

root = tk.Tk()
root.title("Multilistas dobles")
root.geometry("750x700")
tf = []
var = []
label = []
lienzo = tk.Canvas(root,width=720,height=380,background="#fafad2")
lienzo.pack()
lienzo.place(x=10,y=300)

for i in range(5):
    tf.append(tk.Entry(root, width = 20))

for i in range(8):
    var.append(tk.StringVar())
    label.append(tk.Label(root, textvariable = var[i], borderwidth = 2))

tf[0].pack()
tf[0].place(x=174,y=31)

tf[1].pack()
tf[1].place(x=174,y=56)

tf[2].pack()
tf[2].place(x=174,y=131)

tf[3].pack()
tf[3].place(x=174,y=154)

tf[4].pack()
tf[4].place(x=174,y=231)

label[0].pack()
label[0].place(x=0,y=0)
var[0].set("Materias")
label[0].config(font = ("Courier",14), relief = "groove", width=15)

label[1].pack()
label[1].place(x=0,y=29)
var[1].set("Ingrese el nombre de la materia")

label[2].pack()
label[2].place(x=0,y=54)
var[2].set("Ingrese el salon de la materia")

label[3].pack()
label[3].place(x=0,y=100)
var[3].set("Alumnos")
label[3].config(font = ("Courier",14), relief = "groove", width=15)

label[4].pack()
label[4].place(x=0,y=129)
var[4].set("Ingrese el nombre de la materia")

label[5].pack()
label[5].place(x=0,y=152)
var[5].set("Ingrese el nombre del alumno")

label[6].pack()
label[6].place(x=0,y=200)
var[6].set("Salones")
label[6].config(font = ("Courier",14), relief = "groove", width=15)

label[7].pack()
label[7].place(x=0,y=229)
var[7].set("Ingrese el codigo del salon")



class Nodo_Dobles:
    def __init__(self, info):
        self.__info = info
        self.__sig = None
        self.__ant = None
        self.__abajo = None
        
    def info(self):
        return self.__info

    def sig(self):
        return self.__sig
    
    def ant(self):
        return self.__ant
    
    def abajo(self):
        return self.__abajo
    
    def cambiar_sig(self, direcc):
        self.__sig = direcc
        
    def cambiar_ant(self, direcc):
        self.__ant = direcc
        
    def cambiar_abajo(self, direcc):
        self.__abajo = direcc
        
class Lista_Doble():
    __cablista = None
    def __init__(self):
        self.__cablista = None
        
    def insertar_Salon(self, salon):
        if self.__cablista == None:
            self.__cablista = salon
            print("Ingresado el salon {}".format(salon.info()))
            return
        
        q = None
        p = self.__cablista
        
        while p!=None and p.info()!=salon.info():
            q = p
            p = p.sig()
            
        if p!=None and p.info()==salon.info():
            print("El salon {} ya esta en la lista".format(salon.info()))
            return
        
        q.cambiar_sig(salon)
        salon.cambiar_ant(q)
        print("Ingresado el salon {}".format(salon.info()))
        
                
    def insertar_Materia(self, salon, materia):
        p = self.__cablista
        
        while p!=None and p.info()!=salon.info():
            p = p.sig()
        
        if p==None:
            print("No existe el salón {}".format(salon.info()))
            return
            
        q = p.abajo()
        s = p
        while q!=None and q.info()!=materia.info():
            s = q
            q = s.abajo()
        
        if q!=None and q.info()==materia.info():
            print("La materia {} ya esta en la lista".format(materia.info()))
            return
            
        s.cambiar_abajo(materia)
        print("Ingresada la materia {}".format(materia.info())) 
    
    def insertar_Estudiante(self, salon, materia, estudiante):
        p = self.__cablista
        
        while p!=None and p.info()!=salon.info():
            p = p.sig()
        if p==None:
            print("No existe el salón {}".format(salon.info()))
            return
        
        while p!=None and p.info()!=materia.info():
            p = p.abajo()
        if p==None:
            print("No existe la materia {}".format(materia.info()))
            return
        
        
        if p.sig()==None:
            p.cambiar_sig(estudiante)
            print("Ingresado el estudiante {}".format(estudiante.info()))
            return
        
        q = p.sig()
        while q!=None and q.info()!=estudiante.info():
            p = q
            q = p.abajo()
        if q!=None and q.info()==estudiante.info():
            print("El estudiante {} ya esta en la lista".format(materia.info()))
            return
        
        p.cambiar_abajo(estudiante)
        print("Ingresado el estudiante {}".format(estudiante.info()))
            
            
    def buscar_Salon(self, salon):
        comprobar = False
        p = self.__cablista
        
        while p!=None:
            if p.info()==salon.info():
                comprobar = True
                break
            p = p.sig()
        
        if comprobar:
            print(salon.info()+" si existe")
        else:
            print(salon.info()+" no existe")
    
    def buscar_Materia(self, salon, materia):
        comprobarS = False
        comprobarM = False
        p = self.__cablista
        
        while p!=None:
            if p.info()==salon.info():
                comprobarS = True
                break
            p = p.sig()
        if comprobarS==False:
            print(salon.info()+" no existe")
            return
        
        q = p.abajo()
        while q!=None:
            if q.info()==materia.info():
                comprobarM = True
                break
            q = q.abajo()
        
        if comprobarM:
            print(materia.info()+" si existe")
        else:
            print(materia.info()+" no existe")
            
    def buscar_Estudiante(self, salon, materia, estudiante):
        comprobarS = False
        comprobarM = False
        comprobarE = False
        p = self.__cablista
        
        while p!=None:
            if p.info()==salon.info():
                comprobarS = True
                break
            p = p.sig()
        if comprobarS==False:
            print(salon.info()+" no existe")
            return
        
        q = p.abajo()
        while q!=None:
            if q.info()==materia.info():
                comprobarM = True
                break
            q = q.abajo()
        if comprobarM == False:
            print(materia.info()+" no existe")
            return
            
        r = q.sig()
        while r!=None:
            if r.info()==estudiante.info():
                comprobarE = True
                break
            r = r.abajo()
        
        if comprobarE:
            print(estudiante.info()+" si existe")
        else:
            print(estudiante.info()+" no existe")
    
    def retirar_Salon(self, salon):
        if self.__cablista==None:
            print("Lista Vacia")
            return
        p = self.__cablista
        
        if p.sig()==None and p.ant()==None:
            if p.info()==salon.info():
                if p.abajo()!=None:
                    print("Existen materias registradas, no se puede eliminar")
                    return
                else: 
                    self.__cablista = None
                    print("Retirado el salon {}".format(salon.info()))
                    return
            else:
                print ("No existe el salon {}".format(salon.info()))
                return
        
        q = None
        
        while p!=None and p.info()!=salon.info():
            q = p
            p = p.sig()
            
        if p==None:
            print("No existe el salon {}".format(salon.info()))
            return
            
        if p.abajo()!=None:
            print("Existen materias registradas, no se puede eliminar")
            return
        
        if q!=None:
            q.cambiar_sig(p.sig())
            s = p.sig()
            if s!=None:
                s.cambiar_ant(q)
            p = None
        else:
            s = p.sig()
            self.__cablista = p.sig()
            s.cambiar_ant(None)
            p = None
            
        print("Retirado el salon {}".format(salon.info()))
    
    def retirar_Materia(self, salon, materia):
        if self.__cablista==None:
            print("Lista Vacia")
            return
        p = self.__cablista
        
        while p!=None and p.info()!=salon.info():
            p = p.sig()
        
        if p==None:
            print("No existe el salon {}".format(salon.info()))
            return
        
        q = p.abajo()
        
        while q!=None and q.info()!=materia.info():
            p = q
            q = q.abajo()
        
        if q==None:
            print("No existe la materia {}".format(materia.info()))
            return
            
        if q.sig()!=None:
            print("Existen estudiantes registrados, no se puede eliminar")
            return
        
        p.cambiar_abajo(q.abajo())
        print("Retirada la materia {}".format(materia.info()))
        
    def retirar_Estudiante(self, salon, materia, estudiante):
        if self.__cablista==None:
            print("Lista Vacia")
            return
        p = self.__cablista
        
        while p!=None and p.info()!=salon.info():
            p = p.sig()
        
        if p==None:
            print("No existe el salon {}".format(salon.info()))
            return
        p = p.abajo()
        
        while p!=None and p.info()!=materia.info():
            p = p.abajo()
            
        if p==None:
            print("No existe la materia {}".format(materia.info()))
            return
            
        q = p.sig()
        if q!=None and q.info()==estudiante.info():
            p.cambiar_sig(q.abajo())
            print("Retirado el estudiante {}".format(estudiante.info()))
            return
        
        while q!=None and q.info()!=estudiante.info():
            p = q
            q = q.abajo()
            
        if q==None:
            print("No existe el estudiante {}".format(estudiante.info()))
            return
        
        p.cambiar_abajo(q.abajo())
        print("Retirado el estudiante {}".format(estudiante.info()))
    
    def imprimir_Lista(self):
        s = self.__cablista
        while s != None:
            print(s.info())
            q = s.abajo()
            while q!= None:
                print("",q.info())
                r = q.sig()
                while r!=None:
                    print("     ",r.info())
                    t = r.abajo()
                    while t!=None:
                        print("     ",t.info())
                        t = t.abajo()
                    r = r.sig()
                q = q.abajo()
            s = s.sig()

lista=Lista_Doble()

def inMat():
    salon=tf[1].get()
    materia =tf[0].get()
    nodoS = Nodo_Dobles(salon)
    nodoM = Nodo_Dobles(materia)
    lista.insertar_Materia(nodoS, nodoM)
    tf[0].delete(0,'end')
    tf[1].delete(0,'end')
    
def inSal():
    salon=tf[4].get()
    nodoS = Nodo_Dobles(salon)
    lista.insertar_Salon(nodoS)
    tf[4].delete(0,'end')
    
def inEst():
    estudiante=tf[2].get()
    nodoE = Nodo_Dobles(estudiante)
    lista.insertar_Estudiante()

def retMat():
    salon=tf[1].get()
    materia =tf[0].get()
    nodoS = Nodo_Dobles(salon)
    nodoM = Nodo_Dobles(materia)
    lista.retirar_Materia(nodoS, nodoM)
    tf[0].delete(0,'end')
    tf[1].delete(0,'end')
    

insmat = tk.Button(root,text="Insertar materia", width=15, command=inMat)
insmat.pack()
insmat.place(x=340,y=27)

insest = tk.Button(root,text="Insertar alumno", width=15)
insest.pack()
insest.place(x=340,y=140)

inssal = tk.Button(root,text="Insertar salon", width=15, command=inSal)
inssal.pack()
inssal.place(x=340,y=220)

retmat = tk.Button(root,text="Retirar materia", width=15, command=retMat)
retmat.pack()
retmat.place(x=460,y=27)

retest = tk.Button(root,text="Retirar alumno", width=15)
retest.pack()
retest.place(x=460,y=140)

retsal = tk.Button(root,text="Retirar salon", width=15)
retsal.pack()
retsal.place(x=460,y=220)

busmat = tk.Button(root,text="Buscar materia", width=15)
busmat.pack()
busmat.place(x=580,y=27)

busest = tk.Button(root,text="Buscar alumno", width=15)
busest.pack()
busest.place(x=580,y=140)

bussal = tk.Button(root,text="Buscar salon", width=15)
bussal.pack()
bussal.place(x=580,y=220)

lis = tk.Button(root,text="Listar", height = 2, width = 100)
lis.pack()
lis.place(x=20,y=260)

root.mainloop()

'''
op=1    
lista = Lista_Doble()
while op!=0:
    print("\n¿Qué desea hacer?\n"
          "1. Ingresar un salon\n"
          "2. Ingresar una materia\n"
          "3. Ingresar un alumno\n"
          "4. Buscar salon\n"
          "5. Buscar materia\n"
          "6. Buscar estudiante\n"
          "7. Retirar salon\n"
          "8. Retirar materia\n"
          "9. Retirar estudiante\n"
          "10. Listar\n"
          "0. Salir")
    op = int(input("Digite opcion: "))

    if op==1:
        salon = raw_input("Escriba el salon a ingresar: ")
        nodo = Nodo_Dobles(salon)
        lista.insertar_Salon(nodo)
    elif op==2:
        salon = raw_input("Escriba el salon donde ingresar la materia: ")
        materia = raw_input("Escriba la materia a ingresar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        lista.insertar_Materia(nodoS, nodoM)
    elif op==3:
        salon = raw_input("Escriba el salon donde ingresar el estudiante: ")
        materia = raw_input("Escriba la materia donde ingresar el estudiante: ")
        estudiante = raw_input("Escriba el alumno a ingresar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        nodoE = Nodo_Dobles(estudiante)
        lista.insertar_Estudiante(nodoS, nodoM, nodoE)
    elif op==4:
        salon = raw_input("Escriba el salon a buscar: ")
        nodo = Nodo_Dobles(salon)
        lista.buscar_Salon(nodo)
    elif op==5:
        salon = raw_input("Escriba el salon donde se encuentra la materia: ")
        materia = raw_input("Escriba la materia a buscar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        lista.buscar_Materia(nodoS, nodoM)
    elif op==6:
        salon = raw_input("Escriba el salon donde se encuentra el estudiante: ")
        materia = raw_input("Escriba la materia donde se encuentra el estudiante: ")
        estudiante = raw_input("Escriba el alumno a buscar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        nodoE = Nodo_Dobles(estudiante)
        lista.buscar_Estudiante(nodoS, nodoM, nodoE)
    elif op==7:
        salon = raw_input("Escriba el salon a retirar: ")
        nodo = Nodo_Dobles(salon)
        lista.retirar_Salon(nodo)
    elif op==8:
        salon = raw_input("Escriba el salon donde se encuentra la materia: ")
        materia = raw_input("Escriba la materia a eliminar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        lista.retirar_Materia(nodoS, nodoM)
    elif op==9:
        salon = raw_input("Escriba el salon donde se encuentra el estudiante: ")
        materia = raw_input("Escriba la materia donde se encuentra el estudiante: ")
        estudiante = raw_input("Escriba el alumno a eliminar: ")
        nodoS = Nodo_Dobles(salon)
        nodoM = Nodo_Dobles(materia)
        nodoE = Nodo_Dobles(estudiante)
        lista.retirar_Estudiante(nodoS, nodoM, nodoE)
    elif op==10:
        print("\n")
        lista.imprimir_Lista()
'''