# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

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
            
    def buscar(self, n):
        p = self.__cab
        q = p
        while q != None :
            if q.info()==n:
                return True
            else:
                q=q.sig()
        return False
    
    
lista = Lista()
dato = int(input("Digite numero a insertar. (-1) para terminar: "))
while dato != -1:
    nodo = Nodo(dato)
    lista.insertar(nodo)
    dato = int(input("Digite numero a insertar. (-1) para terminar: "))
    
lista.escribir_lista()
if lista.buscar(58):
    print("Se encontró el número")
else:
    print("No se encontró el número")