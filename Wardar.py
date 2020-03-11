import pickle
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
        
    def cambiar_der(self, direcc):
        self.__der = direcc

class Arbol:
    __raiz = None
    def __init__(self):
        self.__raiz = None
    
    def raizArbol(self):
        return self.__raiz
    
    def inorden(self, raiz):
        if raiz != None:
            self.inorden(raiz.rIzq())
            print(str(raiz.info()))
            self.inorden(raiz.rDer())
    def insertar(self, nodo):
        if self.__raiz == None:
            self.__raiz = nodo
            return
        p = self.__raiz
        while p != None:
            q = p
            if nodo.info() < p.info():
                p = p.rIzq()
            elif nodo.info() > p.info():
                p = p.rDer()
            else:
                print("Numero repetido: " + str(nodo.info()))
                return
        if nodo.info() < q.info():
            q.cambiar_izq(nodo)
        else:
            q.cambiar_der(nodo)
            
tree = Arbol()
tree.insertar(Nodo(10))
tree.insertar(Nodo(1))
tree.insertar(Nodo(5))
tree.insertar(Nodo(3))
tree.insertar(Nodo(15))
tree.insertar(Nodo(16))
tree.insertar(Nodo(14))
tree.inorden(tree.raizArbol)


guardado = open("arbol.pickle", "wb")
pickle.dump(tree, guardado)
guardado.close()
print("Objeto arbol gaurdado..................")

