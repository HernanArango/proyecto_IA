from clases import nodo
from time import time
class Algoritmo:
	
	lista_nodos = []
	camino_final = []
	cant_nodos_expandidos = 1
	pos_pasada_x = None
	pos_pasada_y = None
	tiene_flor = False

	def __init__(self,entrada):
		self.tiempo_inicial = time()
		self.entrada = entrada

	def crear_nodo(self,x,y,peso_anterior,nodo_padre):
		
		#crea el nodo si es diferente a muro o tortuga, si es tortuga y tiene flor pasa
		if int(self.entrada[y][x])!=1 and (int(self.entrada[y][x])!= 4 or self.tiene_flor == True):			
		#if int(self.entrada[y][x])!=1:			
			n=nodo()
			n.x=x
			n.y=y
			n.padre=nodo_padre
			if(self.tiene_flor==False):
				n.peso=self.peso_casilla(x,y)+peso_anterior
			else:
				n.peso=1+peso_anterior
			return n
		else:
			return False

	def expansion_disponible(self,x,y):
		if x<0 or x >9 or y<0 or y>9 or (x == self.pos_pasada_x and y == self.pos_pasada_y):
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
		self.pos_pasada_x = nodo.x
		self.pos_pasada_y = nodo.y
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

	def resumen(self,index):
		print "----------------------------------------------------------------"
		print "el nodo meta esta ",self.lista_nodos[index].x," ",self.lista_nodos[index].y
		#Recuperar el camino de llegada
		print "el peso es", self.lista_nodos[index].peso
		self.camino_destino(self.lista_nodos[index],self.nodo_inicial,self.camino_final)
		
		#Imprimir el camino:
		"""
		for nodo in self.camino_final:
			print nodo.x," ",nodo.y
		"""
		print "Se expandieron un total de", self.cant_nodos_expandidos," nodos"
		print "El arbol tiene una profundidad de", len(self.camino_final)

		print "Tiempo de ejecucion ", self.tiempo_ejecucion()

			