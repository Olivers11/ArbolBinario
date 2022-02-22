class Nodo:

    #Se encarga de inicializar los atributos de mi clase
    def __init__(self, valor):
        #Nodo:     valor, puntero izq, puntero der
        self.valor = valor
        self.izq = None
        self.der = None



class Arbol:

    def __init__(self):
        self.raiz = None
    

    def insertarNodo(self, nodoActual, valor):
        #valor = el valor que contendra el nuevo nodo
        if(self.raiz == None):
            #Esta vacio el arbol
            self.raiz = Nodo(valor)
        
        else:
            if(valor < nodoActual.valor):
                if(nodoActual.izq == None):
                    nodoActual.izq = Nodo(valor)
                else:
                    self.insertarNodo(nodoActual.izq, valor)
            else:
                if(nodoActual.der == None):
                    nodoActual.der = Nodo(valor)
                else:
                    self.insertarNodo(nodoActual.der, valor)
    


    def imprimirEnOrden(self, nodoActual):
        if(nodoActual != None):
            #si el arbol no esta vacio, lo imprimiremos        
            self.imprimirEnOrden(nodoActual.izq)
            print(nodoActual.valor)
            self.imprimirEnOrden(nodoActual.der)


arbol = Arbol()
arbol.insertarNodo(arbol.raiz, 7)
arbol.insertarNodo(arbol.raiz, 6)
arbol.insertarNodo(arbol.raiz, 10)
arbol.imprimirEnOrden(arbol.raiz)
