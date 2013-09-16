# -*- coding: utf-8 -*-
import sys
import copy

class Nodo(object):

    def __init__(self):
        self.estado = []  # Los posibles arreglos de n reinas
        self.nivel = 1  # Nivel del arbol en el que nos encontramos
        self.padre = False  # Puntero Identificador del nodo padre
        self.accion = []  # Acción que el padre ejecutó para llegar al nodo

    def expandir(self):
        pass

    def es_solucion(self):
        pass


class NodoCamino(Nodo):
    tablero_tamano=0

    def __init__(self,tamano):
        Nodo.__init__(self)
        self.tablero_tamano = tamano
        #self.estado=[ start, start, goal, bloqueados, [] ]

    
    #  ESTADO INICIAL                         ESTADO FINAL
    #    o G o o        se puede mostrar asi    w w o o
    #    o - - -                                w - - -
    #    o o S o                                w w w o 
    #    o o o o                                o o o o
    
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
        # Es necesario pasar el nodo para trabajar con el estado del mismo?? Para mi no..
        
        if (self.estado[0] == self.estado[2]):
            return True
        else:
            return False
    #pos[FILA,COL] NO [X,Y] !!!!!!!!!!

    def moverArriba(self):
        pos = [self.estado[0][0]-1, self.estado[0][1]]
        nodohijo = False
        if self.estado[0][0] > 0 and pos not in self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre=self
            nodohijo.nivel= nodohijo.padre.nivel + 1
            nodohijo.estado[0][0] -= 1
            nodohijo.estado[4].append(self.estado[0])
        return nodohijo


    def moverIzquierda(self):
        pos = [self.estado[0][0], self.estado[0][1]-1]
        nodohijo = False
        if self.estado[0][1] > 0 and pos not in self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre=self
            nodohijo.nivel= nodohijo.padre.nivel + 1
            nodohijo.estado[0][1] -= 1
            nodohijo.estado[4].append(self.estado[0])
        return nodohijo

    def moverAbajo(self):
        pos = [self.estado[0][0]+1, self.estado[0][1]]
        nodohijo = False
        if self.estado[0][0] <= (self.tablero_tamano - 2) and pos not in self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre=self
            nodohijo.nivel= nodohijo.padre.nivel + 1
            nodohijo.estado[0][0] += 1
            nodohijo.estado[4].append(self.estado[0])
        return nodohijo

    def moverDerecha(self):
        pos = [self.estado[0][0], self.estado[0][1]+1]
        nodohijo = False
        if self.estado[0][1] <= (self.tablero_tamano -2) and pos not in self.estado[3] and pos not in self.estado[4]:
            nodohijo = copy.deepcopy(self)
            nodohijo.padre=self
            nodohijo.nivel= nodohijo.padre.nivel + 1
            nodohijo.estado[0][1] += 1
            nodohijo.estado[4].append(self.estado[0])
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

    def insertar(self, nodos, lista):
        pass

    def buscar(self, tamano):
        start=[2,2]
        peon=[2,2]
        goal=[0,1]
        bloqueados=[[1,1],[1,2],[1,3]]
        primer_camino = NodoCamino(tamano)
        #primer_camino.tablero_tamano=tamano
        primer_camino.estado = [peon,start,goal,bloqueados,[]]   
        # primer_reina.estado = []
        self.abiertos.append(primer_camino)
        while (len(self.abiertos) > 0) and not(self.abiertos[0].es_solucion()):

            # print (("el 1er abierto actual es", self.abiertos[0].estado))

            nodoactual = self.abiertos.pop(0)

            self.insertar(nodoactual.expandir())

            self.cerrados.append(nodoactual)

        if len(self.abiertos) == 0:
            print ("No hay solucion")
        else:
            
            print("Encontre una solucion")
            print(self.abiertos[0].estado)
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
                elif [fila,col] in self.abiertos[0].estado[4]:
                    sys.stdout.write("[-]")
                # Si está en start    
                elif [fila,col] in self.abiertos[0].estado[1]:
                    sys.stdout.write("[S]")
                # Si está en goal    
                elif [fila,col] in self.abiertos[0].estado[2]:
                    sys.stdout.write("[G]")
                
                else:
                    sys.stdout.write("[ ]")
            print("\n")
                    #hayreina = False
                #for reinas in self.abiertos[0].estado:
                    #if reinas[0] == fila and reinas[1] == col:
                        #hayreina = True

                #if hayreina:
                    #sys.stdout.write("R")
                #else:
                    #sys.stdout.write("#")
            #print((" "))


class BusquedaDF(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = nodos + self.abiertos


class BusquedaBF(Busqueda):

    def insertar(self, nodos):
        if (nodos != []):
            self.abiertos = self.abiertos + nodos

#class BusquedaCU(Busqueda):
#   """ Expande el nodo de menor costo """
