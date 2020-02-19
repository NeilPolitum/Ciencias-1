# -*- coding: utf-8 -*-
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
            
        if p != None and p.info() == nodo.info():
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
        while q != alumno.info() and q!= None:
            p = q
            q = q.abajo()
        
        if q == None:
            print("No existe el alumno")
        
        s.cambiar_abajo(q.abajo())
        print("Eliminado correctamente")
        
    def imprimir(self):
        s = self.__cab
        while s != None:
            print(s.info())
            q = s.abajo()
            while q!= None:
                print("",q.info())
                q = q.abajo()
            s = s.sig()

multi = Multilista()

op = 1
while op != 0:
    op = int(input("Qué desea hacer?:\n"
               "1. Insertar materia en la multilista\n"
               "2. Insertar alumno en la multilista\n"
               "3. Retirar materia de la multilista\n"
               "4. Retirar alumno de la multilista\n"
               "5. Ver la multilista\n"
               "6. Dibujar la lista\n"
               "0. Salir\n"))
    
    if op == 1:
        mat = raw_input("Escriba la materia a insertar: ")
        nodo = Nodo(mat)
        multi.ingresar_materia(nodo)
    elif op == 2:
        mat = raw_input("Escriba la materia: ")
        alu = raw_input("Escriba el nombre del alumno: ")
        nodoMat = Nodo(mat)
        nodoAlu = Nodo(alu)
        multi.ingresar_alumno(nodoMat, nodoAlu)
    elif op == 3:
        mat = raw_input("Escriba la materia a eliminar: ")
        nodo = Nodo(mat)
        multi.retirar_materia(nodo)
    elif op == 4:
        mat = raw_input("Escriba la materia donde se encuentra: ")
        alu = raw_input("Escriba el nombre del alumno a eliminar: ")
        nodoMat = Nodo(mat)
        nodoAlu = Nodo(alu)
        multi.retirar_alumno(nodoMat, nodoAlu)
    elif op == 5:
        print("\n")
        multi.imprimir()