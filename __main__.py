# -*- coding: utf-8 -*-

import sys
sys.path.append('D:\GitHub')

from sistemasinteligentes.camino import camino
from sistemasinteligentes.nreinas import nreinas

print ("Bienvenidos")

opcion = 0
while(opcion!=2):
    if opcion not in range(0,3):
        print("Opcion no valida")
    else:
        print("==============")
        print("Menu Principal")
        print("==============")
        print("<1> Encontrar el camino")
        print("<2> N-reinas")
        print("<3> Salir")
        opcion = input("Ingrese opcion: ")
        opcion -= 1

        if (opcion!=2):
            tamano = input("Ingrese tamano tablero: ")

            if (opcion==1):
                print("========")
                print("N-Reinas")
                print("========")
            if (opcion==0):
                print("================")
                print("Encontrar camino")
                print("================")

            opcionbusq=0
            while(opcionbusq!=6):
                if opcionbusq not in range(0,7):
                    print("Opcion no valida")
                print("================")
                print("Tipo de Busqueda")
                print("================")
                print("<1> Busqueda Depth First")
                print("<2> Busqueda Breadth First")
                print("<3> Busqueda Uniform Cost")
                print("<4> Busqueda Informed Depth First")
                print("<5> Busqueda Best First")
                print("<6> Busqueda A*")
                print("<7> Volver")
                opcionbusq = input("Ingrese opcion: ")
                opcionbusq -= 1

                if (opcionbusq==0) and (opcion==1):
                    busq = nreinas.BusquedaDF()
                elif(opcionbusq==1) and (opcion==1):
                    busq = nreinas.BusquedaBF()
                elif(opcionbusq==2) and (opcion==1):
                    busq = nreinas.BusquedaUC()
                elif(opcionbusq==3) and (opcion==1):
                    busq = nreinas.BusquedaDFI()
                elif(opcionbusq==4) and (opcion==1):
                    busq = nreinas.BusquedaBestF()
                elif(opcionbusq==5) and (opcion==1):
                    busq = nreinas.BusquedaAStar()

                if (opcionbusq==0) and (opcion==0):
                    busq = camino.BusquedaDF()
                elif(opcionbusq==1) and (opcion==0):
                    busq = camino.BusquedaBF()
                elif(opcionbusq==2) and (opcion==0):
                    busq = camino.BusquedaUC()
                elif(opcionbusq==3) and (opcion==0):
                    busq = camino.BusquedaDFI()
                elif(opcionbusq==4) and (opcion==0):
                    busq = camino.BusquedaBestF()
                elif(opcionbusq==5) and (opcion==0):
                    busq = camino.BusquedaAStar()

                if opcionbusq in range(0,6) and (opcion==1):
                    busq.buscar(tamano) #Es la busqueda solo para n-reinas

                if opcionbusq in range(0,6) and (opcion==0):
                    busq.buscar(tamano) #busqueda solo camino


