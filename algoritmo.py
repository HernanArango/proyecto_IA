from clases import nodo
class Algoritmo:
	
	def __init__(self,entrada):
		self.entrada = entrada

	def crear_nodo(self,x,y,peso_anterior):
		if(int(self.entrada[y][x])!=1):
			n=nodo()
			n.x=x
			n.y=y
			n.peso=self.peso_casilla(x,y)+peso_anterior
			return n
		else:
			return False

	def expansion_disponible(self,x,y):
		if x<0 or x >9 or y<0 or y>9:
			return False
		else:
			return True

	def expandirNodo(self,nodo):
		#expArriba
		if(self.expansion_disponible(nodo.x,nodo.y-1)):
			result=self.crear_nodo(nodo.x,nodo.y-1,nodo.peso)
			if(result!=False):
				nodo.hijos.append(result)
		#expAbajo
		if(self.expansion_disponible(nodo.x,nodo.y+1)):
			result=self.crear_nodo(nodo.x,nodo.y+1,nodo.peso)
			if(result!=False):
				nodo.hijos.append(result)
		#expDerecha
		if(self.expansion_disponible(nodo.x+1,nodo.y)):
			result=self.crear_nodo(nodo.x+1,nodo.y,nodo.peso)
			if(result!=False):
				nodo.hijos.append(result)
		#expIzquierda
		if(self.expansion_disponible(nodo.x-1,nodo.y)):
			result=self.crear_nodo(nodo.x-1,nodo.y,nodo.peso)
			if(result!=False):
				nodo.hijos.append(result)

		return nodo.hijos

	def peso_casilla(self,x,y):
		if int(self.entrada[y][x])==0 or int(self.entrada[y][x])==2 or int(self.entrada[y][x])==3 or int(self.entrada[y][x])==5:
			return 1
		else:	
			return 7