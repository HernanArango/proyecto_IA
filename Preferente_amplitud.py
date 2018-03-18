from algoritmo import *
class Preferente_amplitud(Algoritmo):
	lista_nodos = []
	def __init__(self,entrada,nodo_inicial,nodo_meta):
		Algoritmo.__init__(self,entrada)
		# agregamos los nuevos atributos
		self.entrada = entrada
		self.nodo_inicial = nodo_inicial
		self.nodo_meta = nodo_meta
		self.lista_nodos.append(self.nodo_inicial)
		self.calcular()

	
	def calcular(self):
		#inicializamos la lista con los tres primeros hijos
		for x in self.lista_nodos:

			if self.es_nodo_meta(x) is True:
				print "el nodo meta esta ",x.x," ",x.y
				break
			hijos = self.expandirNodo(x)
			
			for nodo_hijo in hijos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo_hijo)

			#borra el primer elemento
			self.lista_nodos.pop(0)
			print len(self.lista_nodos)

			
	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False