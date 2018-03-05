from lib import *
camino=[]
#lectura de matriz
entrada = leerEntrada("Prueba1.txt")

#nodoInicial
nodo_init=nodoInicial(entrada)
expandirNodo(nodo_init,entrada)

ambInicial(entrada)