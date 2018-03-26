from algoritmo import *
class Costo_uniforme(Algoritmo):

	
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
			index=self.index_nodo_a_expandir()
			if self.es_nodo_meta(self.lista_nodos[index]) is True:
				self.resumen(index)
				break

			print "nodo a expandir",self.lista_nodos[index].x," ",self.lista_nodos[index].y
			print "el peso es:",self.lista_nodos[index].peso
			
			
			
			hijos = self.expandirNodo(self.lista_nodos[index])			
			self.cant_nodos_expandidos=self.cant_nodos_expandidos + len(hijos);


			for nodo_hijo in hijos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo_hijo)


			#borra el primer elemento
			self.lista_nodos.pop(index)

			self.mostrar_lista()
						

			i = i + 1		
			if i == 10:
				#break
				pass
			
			#print self.lista_nodos
		print "termino for"
		return self.camino_final

	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False

	def index_nodo_a_expandir(self):
		flag = self.lista_nodos[0]
		#se busca el menor peso entre los nodos
		for nodo in self.lista_nodos:
			if flag.peso > nodo.peso:
				flag = nodo

		#retornamos el index de dicho nodo
		return self.lista_nodos.index(flag)




		