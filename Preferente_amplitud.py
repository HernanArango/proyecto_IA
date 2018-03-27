from algoritmo import *
class Preferente_amplitud(Algoritmo):


	def __init__(self,entrada,nodo_inicial,nodo_meta):
		Algoritmo.__init__(self,entrada)
		# agregamos los nuevos atributos
		self.entrada = entrada
		self.nodo_inicial = nodo_inicial
		self.nodo_meta = nodo_meta
		self.lista_nodos.append(self.nodo_inicial)
		print "nodo inicial",self.nodo_inicial.x," ",self.nodo_inicial.y
		print "nodo meta",self.nodo_meta.x," ",self.nodo_meta.y
		self.calcular()

	
	def calcular(self):
		i = 0
		self.mostrar_lista()
		#inicializamos la lista con los tres primeros hijos
		while True:						
			if self.es_nodo_meta(self.lista_nodos[0]) is True:
				self.resumen(0)
				break

			print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y

			
			hijos = self.expandirNodo(self.lista_nodos[0])			
			self.cant_nodos_expandidos = self.cant_nodos_expandidos + len(hijos);


			for nodo_hijo in hijos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo_hijo)


			#borra el primer elemento
			self.lista_nodos.pop(0)

			self.mostrar_lista()
						

			i = i + 1		
			if i == 100:
				#break
				pass
		
			
	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False