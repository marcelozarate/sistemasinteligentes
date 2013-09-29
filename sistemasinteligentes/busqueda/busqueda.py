# -*- coding: utf-8 -*-


class Nodo(object):

    def __init__(self):
        self.estado = []  # Los posibles estados
        self.nivel = 1  # Nivel del arbol en el que nos encontramos
        self.padre = False  # Puntero Identificador del nodo padre
        self.accion = []  # Acción que el padre ejecutó para llegar al nodo
        self.costo = 1

    def expandir(self):
        pass

    def es_solucion(self):
        pass