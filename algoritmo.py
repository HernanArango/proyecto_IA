from clases import nodo
class Algoritmo:
	
	pos_pasada_x = None
	pos_pasada_y = None
	tiene_flor = False

	def __init__(self,entrada):
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
			