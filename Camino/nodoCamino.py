# -*- coding: utf-8 -*-
import sys
import copy
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


class NodoCamino(Nodo):
    tablero_tamano = 0

    def __init__(self, tamano):
        Nodo.__init__(self)
        self.tablero_tamano = tamano

    # ESQUEMA DE REPRESENTACIÓN
    # --------------------------

    # PEON = [peonF, peonC]
    # START= [startF, startC]
    # GOAL = [goalF, goalC]
    # BLOQUEADOS = [[2,2],[2,3]]
    # CAMINO = []

    # ejemplo

    # ESTADO = [[2,2],[2,2],[0,1], [[1,1],[1,2],[1,3]],  []  ]
    # ESTADO = [PEON, START, GOAL,      BLOQUEADOS    ,CAMINO]
    # ESTADO = [  0 ,   1  ,  2  ,      3             ,   4  ]

    def es_solucion(self):
        """La posición del peon sea igual a la posición  de GOAL"""

        if (self.estado[0] == self.estado[2]):
            return True
        else:
            return False
    #pos[FILA,COL] NO [X,Y] !!!!!!!!!!

    def moverArriba(self):
        pos = [self.estado[0][0] - 1, self.estado[0][1]]
        nodohijo = False
        if self.estado[0][0] > 0 and pos not in self.estado[3] and pos not in \
        self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre = self
            # Si no sigo en la misma columna varía el costo
            if(self.estado[0][1] != pos[1]):
                nodohijo.costo += 0.2
            nodohijo.nivel = nodohijo.padre.nivel + 1
            nodohijo.estado[0][0] -= 1
            nodohijo.estado[4].append(pos)
        return nodohijo

    def moverIzquierda(self):
        pos = [self.estado[0][0], self.estado[0][1] - 1]
        nodohijo = False
        if self.estado[0][1] > 0 and pos not in self.estado[3] and pos not in \
        self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre = self
            # Si no sigo en la misma fila varía el costo
            if(self.estado[0][0] != pos[0]):
                nodohijo.costo += 0.2
            nodohijo.nivel = nodohijo.padre.nivel + 1
            nodohijo.estado[0][1] -= 1
            nodohijo.estado[4].append(pos)
        return nodohijo

    def moverAbajo(self):
        pos = [self.estado[0][0] + 1, self.estado[0][1]]
        nodohijo = False
        if self.estado[0][0] <= (self.tablero_tamano - 2) and pos not in \
        self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre = self
            # Si no sigo en la misma columna varía el costo
            if(self.estado[0][1] != pos[1]):
                nodohijo.costo += 0.2
            nodohijo.nivel = nodohijo.padre.nivel + 1
            nodohijo.estado[0][0] += 1
            nodohijo.estado[4].append(pos)
        return nodohijo

    def moverDerecha(self):
        pos = [self.estado[0][0], self.estado[0][1] + 1]
        nodohijo = False
        if self.estado[0][1] <= (self.tablero_tamano - 2) and pos not in \
        self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre = self
            # Si no sigo en la misma fila varía el costo
            if(self.estado[0][0] != pos[0]):
                nodohijo.costo += 0.2
            nodohijo.nivel = nodohijo.padre.nivel + 1
            nodohijo.estado[0][1] += 1
            nodohijo.estado[4].append(pos)
        return nodohijo

    def expandir(self):
        # Acordate que es como sucesores, aca van las reglas
        sucesores = []

        nodo = self.moverArriba()
        if nodo:
            sucesores.append(nodo)

        nodo = self.moverIzquierda()
        if nodo:
            sucesores.append(nodo)

        nodo = self.moverAbajo()
        if nodo:
            sucesores.append(nodo)

        nodo = self.moverDerecha()
        if nodo:
            sucesores.append(nodo)

        return sucesores


class Busqueda(object):

    def __init__(self):
        self.cerrados = []
        self.abiertos = []
        self.nodosgen = 1
        self.tiempo = 0

    def insertar(self, nodos, lista):
        pass

    def buscar(self, tamano):
        #start=[2, 2]
        startf = int(raw_input("Fila de Start: "))
        startc = int(raw_input("Columna de Start: "))
        start = [startf, startc]
        peon = [start[0], start[1]]
        goalf = int(raw_input("Fila de Goal: "))
        goalc = int(raw_input("Columna de Goal: "))
        goal = [goalf, goalc]
        cant_bloq = int(raw_input("Cantidad de Bloqueados: "))
        bloqueados = []
        for i in range(0, cant_bloq):
            bloqueados.append([int(raw_input("Fila Bloq[%d]: " % i)),
            int(raw_input("Columna Bloq[%d]: " % i))])
        print(bloqueados)
        tiempo_inicial = time.time()
        self.__init__()
        primer_camino = NodoCamino(tamano)
        primer_camino.estado = [peon, start, goal, bloqueados, [start]]
        self.abiertos.append(primer_camino)
        while (len(self.abiertos) > 0) and not(self.abiertos[0].es_solucion()):

            # print (("el 1er abierto actual es", self.abiertos[0].estado))

            nodoactual = self.abiertos.pop(0)

            self.insertar(nodoactual.expandir())

            self.cerrados.append(nodoactual)
        self.tiempo = time.time() - tiempo_inicial
        if len(self.abiertos) == 0:
            print ("No hay solucion")
        else:
            print("Encontre una solucion")
            print((self.abiertos[0].estado))
            self.mostrar_solucion()

    def mostrar_solucion(self):
        print ("\n============")
        print ("Hay solucion")
        print ("============\n")

        for fila in range(0, self.abiertos[0].tablero_tamano):
            for col in range(0, self.abiertos[0].tablero_tamano):
                # Si está en bloqueados
                if [fila, col] in self.abiertos[0].estado[3]:
                    sys.stdout.write("[X]")
                # Si está en camino
                elif [fila, col] in self.abiertos[0].estado[4]:
                    if [fila, col] != self.abiertos[0].estado[1]:
                        if [fila, col] != self.abiertos[0].estado[2]:
                            sys.stdout.write("[-]")
                        else:
                            sys.stdout.write("[G]")
                    else:
                        sys.stdout.write("[S]")

                else:
                    sys.stdout.write("[ ]")
            print("\n")

        print(("Profundidad de la solucion: " + str(self.abiertos[0].nivel)))
        print(("Cantidad de estados generados: " + str(self.nodosgen)))
        print(("Cantidad de nodos abiertos: " + str(len(self.abiertos))))
        print(("Cantidad de nodos cerrados: " + str(len(self.cerrados))))
        print(("Tiempo de procesamiento (segundos): " + str(self.tiempo)))


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