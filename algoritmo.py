from clases import nodo
from time import time
class Algoritmo:
	
	lista_nodos = []
	camino_final = []
	cant_nodos_expandidos = 1
	tiene_flor = False
	profundidad_arbol = 0

	def __init__(self,entrada):
		self.tiempo_inicial = time()
		self.entrada = entrada

	def crear_nodo(self,x,y,peso_anterior,nodo_padre):
		
		#crea el nodo si es diferente a muro
		if int(self.entrada[y][x])!=1:			
		#if int(self.entrada[y][x])!=1:			
			n=nodo()
			n.x=x
			n.y=y
			n.padre=nodo_padre
			n.profundidad = nodo_padre.profundidad + 1
			self.save_profundidad_arbol(n.profundidad)
			if(self.tiene_flor==False):
				n.peso=self.peso_casilla(x,y)+peso_anterior
			else:
				n.peso=1+peso_anterior
			return n
		else:
			return False

	def expansion_disponible(self,x,y):
		if x<0 or x >9 or y<0 or y>9:
			return False
		else:
			return True

	def expandirNodo(self,nodo):
		hijos = []

		if int(self.entrada[nodo.y][nodo.x]) == 3:
			self.tiene_flor = True
			print "TIENE FLOR***********************************"
		
		#expArriba
		if(self.expansion_disponible(nodo.x,nodo.y-1)):
			result=self.crear_nodo(nodo.x,nodo.y-1,nodo.peso,nodo)
			if(result!=False):
				hijos.append(result)
		#expAbajo
		if(self.expansion_disponible(nodo.x,nodo.y+1)):
			result=self.crear_nodo(nodo.x,nodo.y+1,nodo.peso,nodo)
			if(result!=False):
				hijos.append(result)
		#expDerecha
		if(self.expansion_disponible(nodo.x+1,nodo.y)):
			result=self.crear_nodo(nodo.x+1,nodo.y,nodo.peso,nodo)
			if(result!=False):
				hijos.append(result)
		#expIzquierda
		if(self.expansion_disponible(nodo.x-1,nodo.y)):
			result=self.crear_nodo(nodo.x-1,nodo.y,nodo.peso,nodo)
			if(result!=False):
				hijos.append(result)

		print "numero de hijos expandidos ", len(hijos)
		return hijos

	def peso_casilla(self,x,y):
		if int(self.entrada[y][x])!=4:
			return 1
		else:	
			return 8

	def camino_destino(self,nodo_final,nodo_raiz,camino):
		if nodo_final.x==nodo_raiz.x and nodo_final.y==nodo_raiz.y:
			camino.append(nodo_final)
			return
		else:
			camino.append(nodo_final)
			self.camino_destino(nodo_final.padre,nodo_raiz,camino)

	def tiempo_ejecucion(self):
		return time() - self.tiempo_inicial

	def mostrar_lista(self):
		print "--------------------------------------"
		for x in self.lista_nodos:
			print "elementos lista nodo ",x.x," ",x.y

	
	def save_profundidad_arbol(self,profundidad_nodo):
		if  profundidad_nodo > self.profundidad_arbol:
			self.profundidad_arbol = profundidad_nodo


	def resumen(self,index):
		print "----------------------------------------------------------------"
		print "el nodo meta esta ",self.lista_nodos[index].x," ",self.lista_nodos[index].y
		#Recuperar el camino de llegada
		print "el peso del camino es", self.lista_nodos[index].peso
		self.camino_destino(self.lista_nodos[index],self.nodo_inicial,self.camino_final)

		print "Se expandieron un total de", self.cant_nodos_expandidos," nodos"
		#CORREGIR!
		print "El arbol tiene una profundidad de", self.profundidad_arbol

		print "Tiempo de ejecucion ", self.tiempo_ejecucion()

			