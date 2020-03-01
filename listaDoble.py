# -*- coding: utf-8 -*-
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
        