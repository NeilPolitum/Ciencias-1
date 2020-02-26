# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 08:36:34 2020

@author: estudiantes
"""
import Tkinter as tk

#Interfaz

root = tk.Tk()
root.geometry("1000x1000")
root.title("Listas dobles")
lienzo = tk.Canvas(root,width=800,height=9000,background="#fafad2")
lienzo.pack()
lienzo.place(x=0,y=0)
tf = tk.Entry(root,width = 20)
var = tk.StringVar(value="Ingrese el numero:")
label = tk.Label(root,textvariable = var)
label.pack()
label.place(x=0,y=30)
tf.pack()
tf.place(x=110,y=32)



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
            return
        
        q = None
        p = self.__cablista_doble
        
        while p!=None and p.info()<nodo.info():
            q = p
            p = p.sig()
            
        if p!=None and p.info()==nodo.info():
            print("{nodo.info()} ya esta en la lista")
            return
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
        p = self.__cablista_doble = None
        
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

root.mainloop()

"""
op=1    
lista = None
while op!=0:
    print("¿Qué desea hacer?\n"
          "1. Crear Lista\n"
          "2. Insertar numero\n"
          "3. Retirar numero\n"
          "4. Buscar numero\n"
          "5. Listar\n"
          "0. Salir\n")
    op = int(input("Digite opcion: "))

    if op==1:
        lista = Lista_Doble()
        print("Lista creada vacia\n")
    elif op==2:
        if lista!=None:
            dato = int(input("Digite numero a insertar: "))
            nodo = Nodo_Dobles(dato)
            lista.insertar_Doble(nodo)
    elif op==3:
        if lista!=None:
            dato = int(input("Digite numero a retirar: "))
            lista.retirar_lista_Doble(dato)
    elif op==4:
        if lista!=None:
            dato = int(input("Digite numero a buscar: "))
            lista.buscar_lista_Doble(dato)
    elif op==5:
        if lista!=None:
            lista.escribir_lista_Doble()
            
"""
            