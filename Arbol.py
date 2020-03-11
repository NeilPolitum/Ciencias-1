# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:40:06 2020

@author: estudiantes
"""

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
        self.__def = direcc
        
class Arbol:
    __raiz = None
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
            
    def insertar(self,nodo):
        if self.__raiz == None:
            self.__raiz = None
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
        print("Eliminado: "+p.info())
        p = None
    
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
    
op = 99
ar = Arbol()
while op != 0:
    print("\n¿Qué desea hacer?\n"
          "1. Insertar un número\n"
          "2. Listar en inorden\n"
          "3. Listar en preorden\n"
          "4. Listar en postorden\n"
          "5. Listar por niveles\n"
          "6. Eliminar un nodo\n"
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
        p = ar.raizarbol()
        cola = CCola()
        
        if p!=None:
            cola.ins_cola(p)
        
        while cola.vacia()==False:
            p = cola.retirar_cola()
            print(str(p.info()))
            if p.rIzq()!=None:
                cola.ins_cola(p.rIzq())
            if p.rDer!=None:
                cola.ins_cola(p.rDer())
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
            
    elif(op==0):
        print("Calabaza, calabaza, cada quien pa su gran puta mierda")
        