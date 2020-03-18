# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:55:58 2020

@author: danie
"""

class notacionPolaca:
    __infija = None
    __posfija = None
    def __init__(self):
        self.__infija = None
        
    def getInFija(self):
        opIn = " ".join(self.__infija)
        return opIn
        
    def ingresarOperacion(self, opera):
        quitarEspacios = opera.replace(" ","")
        self.__infija = list(quitarEspacios)
        print("Operacion ingresada correctamente")
        
    def pasarInPos(self):
        signos = [[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,1,1,1,0]]
        pila = []
        posfijo = []
        operacion = self.__infija
        
        longitud = len(self.__infija)
        
        for i in range(longitud):
            if operacion[i].isdigit() == True:
                posfijo.append(operacion[i])
            elif not pila:
                pila.append(operacion[i])
            else:
                longitudPila = len(pila) - 1
                if operacion[i]=="+":
                    a = 0
                elif operacion[i]=="-":
                    a = 1
                elif operacion[i]=="*":
                    a = 2
                elif operacion[i]=="/":
                    a = 3
                elif operacion[i]=="^":
                    a = 4
                    
                if pila[longitudPila]=="+":
                    b = 0
                elif pila[longitudPila]=="-":
                    b = 1
                elif pila[longitudPila]=="*":
                    b = 2
                elif pila[longitudPila]=="/":
                    b = 3
                elif pila[longitudPila]=="^":
                    b = 4
                    
                if signos[a][b] == 0:
                    posfijo.append(pila[longitudPila])
                    pila[longitudPila] = operacion[i]
                else: 
                    pila.append(operacion[i])
        
        pilaR = pila[::-1]
        for i in range(len(pilaR)):
            if pilaR[i]!=None:
                posfijo.append(pilaR[i])
                
        opPos = " ".join(posfijo)
        print(opPos)
            
notPol = notacionPolaca()
op = 1
while op!=0:
    print("\n¿Qué desea hacer?\n"
          "1. Ingresar operación\n"
          "2. Pasar de infija a posfija\n"
          "0. Salir")
    op = int(input("Digite opcion: "))
    
    if op == 1:
        opera = raw_input("Ingrese la operacion con numeros: ")
        notPol.ingresarOperacion(opera)
    elif op == 2:
        print("\nOperación InFija:")
        print(notPol.getInFija())
        print("\nOperación PosFija:")
        notPol.pasarInPos()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    