import sys
import pygame
from pygame.locals import *
from clases import *
from Preferente_amplitud import *

class Interfaz:
	def tipo_imagen(self,num):

		flor = pygame.image.load('img/flor.png')
		mario = pygame.image.load('img/mario.png')
		muro = pygame.image.load('img/ladrillo.png')
		koopa = pygame.image.load('img/koopatroopa.jpg')
		reina = pygame.image.load('img/peach.jpg')
		
		if num==1:
			return muro
		elif num==2:
			return mario
		elif num==3:
			return flor
		elif num==4:
			return koopa
		elif num==5:
			return reina
		else:
			return 0

	def leerEntrada(self,namefile):
		self.entrada = []
		#lectura de la entrada
		file  = open(namefile, "r") 
		for line in file:
			line_clean=line.rstrip().split(" ");
			self.entrada.append(line_clean)

		

	def ambInicial(self,namefile):

		self.leerEntrada(namefile)
		#init pygame
		pygame.init()
		#variables iniciales para creacion de grilla

		color=(255,255,255)#blanco
		colorDos=pygame.Color(0,0,0)#negro
		#dimensiones para la grilla
		largo=60
		alto=60
		margen=2
		x=0
		y=0
		#

		#lienzo
		ventana=pygame.display.set_mode((1000, 600))
		#titulo para el lienzo
		pygame.display.set_caption("init")

		ventana.fill(color)
		#definimos nodo inicial donde se encuentra mario
		self.nodo_inicial=nodo()

		for fila in range(0,10):
			for columna in range(0,10):
				#pygame.draw.rect(ventana, color, (x,y,alto,largo),margen)
				if int(self.entrada[fila][columna])==0:
					pygame.draw.rect(ventana, colorDos, (x,y,alto,largo),margen)
				else:
					#calcula la posicion del nodo inicial
					if (int(self.entrada[fila][columna])==2):
						self.nodo_inicial.x=columna
						self.nodo_inicial.y=fila

					ventana.blit(self.tipo_imagen(int(self.entrada[fila][columna])),(x,y))
				x=x+60
			y=y+60
			x=0

		pygame.draw.rect(ventana, colorDos, (700,100,100,30),margen)
		pygame.draw.rect(ventana, colorDos, (700,200,100,30),margen)

		tipo_algoritmo = 1
		self.calcular(tipo_algoritmo)

		while True:
		#pintar de X color  el lienzo
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

		
	def calcular(self,tipo_algoritmo):

		#preferente por amplitud
		if tipo_algoritmo == 1:
			algoritmo = Preferente_amplitud(self.entrada)

		algoritmo.expandirNodo(self.nodo_inicial)
