from algoritmo import *
class Avara(Algoritmo):

	
	def __init__(self,entrada,nodo_inicial,nodo_meta):
		Algoritmo.__init__(self,entrada)
		# agregamos los nuevos atributos
		self.entrada = entrada
		self.nodo_inicial = nodo_inicial
		self.nodo_meta = nodo_meta
		self.name="avara"
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
			
			if self.nodo_fue_expandido(self.lista_nodos[index].padre,self.lista_nodos[index]) == False:
				hijos = self.expandirNodo(self.lista_nodos[index],self.nodo_meta)			
			else:
				print "no expande"
				hijos = []
				
			self.cant_nodos_expandidos=self.cant_nodos_expandidos + len(hijos);


			for nodo_hijo in hijos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo_hijo)


			#borra el elemento que se expandio elemento
			self.lista_nodos.pop(index)

			self.mostrar_lista()
						

			i = i + 1		
			if i == 5:
				#break
				pass

	#Evalua si el nodo pasado por parametro es igual al nodo meta
	def es_nodo_meta(self,nodo):
		if nodo.x == self.nodo_meta.x  and nodo.y == self.nodo_meta.y:
			return True
		else:
			return False

	#evita ciclos
	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		#si es igual a algun nodo padre 
		elif nodo_a_verificar.x == nodo_padre.x and nodo_a_verificar.y == nodo_padre.y and nodo_a_verificar.flor == nodo_padre.flor:
			print "ya se ha expandido no expande"
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido(nodo_padre.padre,nodo_a_verificar)

	#En la lista de nodos expandidos busca cual es el nodo con menor h(n)
	def index_nodo_a_expandir(self):
		flag = self.lista_nodos[0]
		#se busca el menor peso entre los nodos
		for nodo in self.lista_nodos:
			if flag.heuristica > nodo.heuristica:
				flag = nodo

		#retornamos el index de dicho nodo
		return self.lista_nodos.index(flag)




		