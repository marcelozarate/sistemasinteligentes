# -*- coding: utf-8 -*-
import sys
import time


class Nodo(object):

    def __init__(self):
        self.estado = []  # Los posibles arreglos de n reinas
        self.nivel = 1  # Nivel del arbol en el que nos encontramos
        self.padre = False  # Puntero Identificador del nodo padre
        self.accion = []  # Acción que el padre ejecutó para llegar al nodo
        self.costo = 1

    def expandir(self):
        pass

    def es_solucion(self):
        pass


class NodoReina(Nodo):
    tablero_tamano = 4

    def __init__(self, tamano):
        Nodo.__init__(self)
        self.tablero_tamano = tamano
        self.caslibres = 0

    # EJ: estado = [[2,1], [0,2]] y pos = [3,3]
    def sin_ataque(self, estado, pos):
        # print (estado)
        for reina in estado:
            x = reina[0]
            y = reina[1]

            # COMPRUEBO FILAS
            if((pos[0]) == x):
                return False

            # COMPRUEBO COLUMNAS
            if((pos[1]) == y):
                return False

            # COMPRUEBO DIAGONAL ASCENDENTE
            if (x + y == pos[0] + pos[1]):
                return False

            # COMPRUEBO DIAGONAL ASCENDENTE
            if (x - y == pos[0] - pos[1]):
                return False

        return True

    def expandir(self):
        sucesores = []
        for col in range(0, self.tablero_tamano):
            for fila in range(0, self.tablero_tamano):
                posachequear = [fila, col]
                valida = self.sin_ataque(self.estado, posachequear)
                if valida:
                    nodohijo = NodoReina(self.tablero_tamano)
                    nodohijo.estado = self.estado + [posachequear]
                    nodohijo.nivel = self.nivel + 1
                    nodohijo.padre = self
                    nodohijo.accion = posachequear
                    #nodohijo.costo = self.costo + costodeeste
                    sucesores.append(nodohijo)
        self.caslibres = len(sucesores)
        return sucesores

    def es_solucion(self):
        if (len(self.estado) == self.tablero_tamano):
            return True
        else:
            return False


class Estado(object):

    def __init__(self):
        pass


class Busqueda(object):

    def __init__(self):
        self.cerrados = []
        self.abiertos = []
        self.nodosgen = 1
        self.tiempo = 0

    def insertar(self, nodos):
        pass

    def buscar(self, tamano):
        tiempo_inicial = time.time()
        self.__init__()
        primer_reina = NodoReina(tamano)
        # primer_reina.estado = []
        self.abiertos.append(primer_reina)
        while (len(self.abiertos) > 0) and not(self.abiertos[0].es_solucion()):

            # print (("el 1er abierto actual es", self.abiertos[0].estado))

            nodoactual = self.abiertos.pop(0)

            self.insertar(nodoactual.expandir())

            self.cerrados.append(nodoactual)

        self.tiempo = time.time() - tiempo_inicial
        if len(self.abiertos) == 0:
            print ("No hay solucion")
        else:
            self.mostrar_solucion()

    def mostrar_solucion(self):
        print ("\n============")
        print ("Hay solucion")
        print ("============\n")

        for fila in range(0, self.abiertos[0].tablero_tamano):
            for col in range(0, self.abiertos[0].tablero_tamano):
                hayreina = False
                for reinas in self.abiertos[0].estado:
                    if reinas[0] == fila and reinas[1] == col:
                        hayreina = True

                if hayreina:
                    sys.stdout.write("R")
                else:
                    sys.stdout.write("#")
            print((" "))
        print(("Profundidad de la solucion: ", self.abiertos[0].nivel))
        print(("Cantidad de estados generados: ", self.nodosgen))
        print(("Cantidad de nodos abiertos: ", len(self.abiertos)))
        print(("Cantidad de nodos cerrados: ", len(self.cerrados)))
        print(("Tiempo de procesamiento (segundos): ", self.tiempo))


class BusquedaDF(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = nodos + self.abiertos
            self.nodosgen += len(nodos)


class BusquedaBF(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = self.abiertos + nodos
            self.nodosgen += len(nodos)


class BusquedaUC(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = self.abiertos + nodos
            self.abiertos.sort(key=lambda x: x.costo)
            self.nodosgen += len(nodos)


class BusquedaDFI(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            nodos.sort(key=lambda x: x.caslibres, reverse=True)
            self.abiertos = nodos + self.abiertos
            self.nodosgen += len(nodos)


class BusquedaBestF(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = nodos + self.abiertos
            self.abiertos.sort(key=lambda x: x.caslibres, reverse=True)
            self.nodosgen += len(nodos)
