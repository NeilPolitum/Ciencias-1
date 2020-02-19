class Nodo:    
    
    def __init__(self, info):
        self.__info =info
        self.__sig = None
    
    def cambiarSiguiente(self, siguiente):
        self.__sig = siguiente
        
    def getSiguiente(self):
        return self.__sig
    
    def getInfo(self):
        return self.__info
        
class Pila:
    
    def __init__(self):
        self.__cab = None
        
    def retirar(self):
        if self.__cab == None:
            print("La pila esta vacia")
        else:
            p = self.__cab.__info
            self.__cab = self.__cab.getSiguiente()
            return p

    def insertar (self, info):
        p = self.__cab
        self.__cab = Nodo (info)
        self.__cab.cambiarSiguiente(p)
            
    def imprimir(self):
        if self.__cab == None:
            print("La pila esta vacia")
        else:
            p=self.__cab
            while p.getSiguiente() != None:
                print("|"+p.__info+"|")
        
            
class Cola:
    
    def __init__(self):
        self.__cab = None
    
    def retirar(self):
        if self.__cab == None:
            print("La cola esta vacia")
        else:
            p = self.__cab.__info
            self.__cab = self.__cab.getSiguiente()
            return p
        
    def insertar(self, info):
        if self.__cab == None:
            print("La cola esta vacia")
        else:
            p=self.__cab
            while(p.getSiguiente()!=None):
                p=p.getSiguiente()
            p.cambiarSiguiente(Nodo (info))
            
    def imprimir(self):
        if self.__cab == None:
            print("La cola esta vacia")
        else:
            p=self.__cab
            while p.getSiguiente()!= None:
                print("|"+p.__info+"|")
                
                
a=0
while a!=-1:
    a=input("1.Crear pila\n2.Crear cola\n-1.Salir\nInserte la eleccion: ")        
    if a==1:
        pila = Pila()
        b=0
        while b!=-1:
            b=input("1.Insertar elemento a la pila\n2.Eliminar elemento de la pila\n3.Imprimir pila\n-1.Menu principal\nInserte la eleccion: ")
            if b==1:
                pila.insertar(input("Ingrese el elemento a insertar: "))
            elif b==2:
                print("Se elimino el elemento "+str(pila.retirar()))
            elif b==3:
                pila.imprimir()
    
    elif a==2:
        cola=Cola()
        b=0
        while b!=-1:
            b=input("1.Insertar elemento a la cola\n2.Eliminar elemento de la cola\n3.Imprimir cola\n-1.Menu principal\nInserte la eleccion: ")
            if b==1:
                cola.insertar(input("Ingrese el elemento a insertar: "))
            elif b==2:
                print("Se elimino el elemento "+str(cola.retirar()))
            elif b==3:
                cola.imprimir()