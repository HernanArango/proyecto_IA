import sys

import pygame
import time as t
from pygame.locals import *
from clases import *
from Preferente_amplitud import *
from Preferente_profundidad import *
from Costo_uniforme import *

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
		#lienzo
		ventana=pygame.display.set_mode((1000, 600))
		#titulo para el lienzo
		pygame.display.set_caption("init")

		ventana.fill(color)
		#definimos nodo inicial donde se encuentra mario
		self.nodo_inicial=nodo()
		#definimos nodo inicial donde se encuentra mario
		self.nodo_meta=nodo()

		for fila in range(0,10):
			for columna in range(0,10):
				#pygame.draw.rect(ventana, color, (x,y,alto,largo),margen)
				if int(self.entrada[fila][columna])==0:
					pygame.draw.rect(ventana, colorDos, (x,y,alto,largo),margen)
				else:
					#calcula la posicion del nodo inicial donde se encuentra mario
					if (int(self.entrada[fila][columna]) == 2):
						self.nodo_inicial.x=columna
						self.nodo_inicial.y=fila
					#nodo meta donde se encuentra la princesa
					elif (int(self.entrada[fila][columna]) == 5):
						self.nodo_meta.x=columna
						self.nodo_meta.y=fila

					ventana.blit(self.tipo_imagen(int(self.entrada[fila][columna])),(x,y))
				x=x+60
			y=y+60
			x=0
		
		while True:
			button = pygame.Rect(640,200,100,30)
			button2 = pygame.Rect(750,200,100,30)
			button3 = pygame.Rect(860,200,100,30)
			button4 = pygame.Rect(690,280,100,30)
			button5 = pygame.Rect(800,280,100,30)
			button6 = pygame.Rect(750,550,100,30)
			self.menu_principal(ventana,button,button2,button3,button4,button5,button6)
			for evento in pygame.event.get():
				camino_final=""
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
				if evento.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = evento.pos  # gets mouse position

					# checks if mouse position is over the button
					if button.collidepoint(mouse_pos):
						# prints current location of mouse
						print('button was pressed at {0}'.format(mouse_pos))
						tipo_algoritmo = 1
						camino = self.calcular(tipo_algoritmo)
						self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		                

					if button2.collidepoint(mouse_pos):
						# prints current location of mouse
						print('button was pressed at {0}'.format(mouse_pos))
						tipo_algoritmo = 2
						camino = self.calcular(tipo_algoritmo)
						self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		                

					if button3.collidepoint(mouse_pos):
						# prints current location of mouse
						print('button was pressed at {0}'.format(mouse_pos))
						tipo_algoritmo = 3
						camino = self.calcular(tipo_algoritmo)
						self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)	
				pygame.display.update()

		
	def calcular(self,tipo_algoritmo):
		
		#preferente por amplitud
		if tipo_algoritmo == 1:
			algoritmo = Preferente_amplitud(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(algoritmo.camino_final))
			return camino
		elif tipo_algoritmo == 2:
			algoritmo = Costo_uniforme(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(algoritmo.camino_final))
			return camino

		elif tipo_algoritmo == 3:
			algoritmo = Preferente_profundidad(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(algoritmo.camino_final))
			return camino

	def pintar_camino(self,ventana,camino,nodo_inicial,nodo_final):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.init()
		pygame.mixer.music.load('sound/mario.wav')
		pygame.mixer.music.play(0)
		img_camino = pygame.image.load('img/camino.jpg')
		img_end = pygame.image.load('img/end.png')
		mario = pygame.image.load('img/mario.png')
		for nodo in camino:
			pos=camino.index(nodo)
			if pos != 0:
				nodo_anterior=camino[pos-1]
				ventana.blit(img_camino,(nodo_anterior.x*60,nodo_anterior.y*60))
			ventana.blit(mario,(nodo.x*60,nodo.y*60))
			pygame.time.wait(250)
			pygame.display.update()
		pygame.mixer.music.stop()
		pygame.mixer.music.load('sound/win.wav')
		pygame.mixer.music.play(0)
		ventana.blit(img_end,(nodo_final.x*60,nodo_final.y*60))


	def menu_principal(self,ventana,b_1,b_2,b_3,b_4,b_5,b_6):
		#Titulo
		font = pygame.font.SysFont("comicsansms", 50)
		title = font.render("Proyecto #1", True, (107, 107, 107))
		ventana.blit(title,(650+(title.get_width()/3),30))
		#------------------------------------------------------
		#Nombres
		font = pygame.font.SysFont("comicsansms", 30)
		name1 = font.render("Hernan Arango-1710060", True, (0, 0, 0))
		name2 = font.render("Daniel Gaviria-1710145", True, (0, 0, 0))
		ventana.blit(name1,(605,90))
		ventana.blit(name2,(605,120))
		#------------------------------------------------------
		#Busqueda No Informada
		subtitle1 = font.render("Busqueda No Informada", True, (170, 170, 170))
		ventana.blit(subtitle1,(650+(subtitle1.get_width()/6),160))
		#Botones
		font = pygame.font.SysFont("comicsansms", 20)
		text_b1=font.render("Amplitud", True, (0, 0, 0))
		text_b2=font.render("Costo U.", True, (0, 0, 0))
		text_b3=font.render("Profundidad", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_1)
		pygame.draw.rect(ventana, [170, 170, 170], b_2)
		pygame.draw.rect(ventana, [170, 170, 170], b_3)
		ventana.blit(text_b1,(645+(text_b1.get_width()/3),207))
		ventana.blit(text_b2,(755+(text_b2.get_width()/3),207))
		ventana.blit(text_b3,(860+(text_b3.get_width()/6),207))
		#------------------------------------------------------
		#Busqueda Informada
		font = pygame.font.SysFont("comicsansms", 30)
		subtitle2 = font.render("Busqueda Informada", True, (170, 170, 170))
		ventana.blit(subtitle2,(650+(subtitle2.get_width()/4),250))
		#Botones
		font = pygame.font.SysFont("comicsansms", 20)
		text_b4=font.render("Avara", True, (0, 0, 0))
		text_b5=font.render("A*", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_4)
		pygame.draw.rect(ventana, [170, 170, 170], b_5)
		ventana.blit(text_b4,(720,288))
		ventana.blit(text_b5,(840,288))
		#------------------------------------------------------
		#Informes de Busqueda
		font = pygame.font.SysFont("comicsansms", 40)
		subtitle3 = font.render("Resumen", True, (170, 170, 170))
		ventana.blit(subtitle3,(650+(subtitle3.get_width()/1.5),320))
		font = pygame.font.SysFont("comicsansms", 20)
		subtitle4=font.render("# Nodos Expandidos:", True, (170, 170, 170))
		subtitle5=font.render("Profundidad del arbol:", True, (170, 170, 170))
		subtitle6=font.render("Tiempo de Ejecucion:", True, (170, 170, 170))
		ventana.blit(subtitle4,(660,360))
		ventana.blit(subtitle5,(660,420))
		ventana.blit(subtitle6,(660,480))
		#Boton de reset Interfaz
		text_b6=font.render("Reset", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_6)
		ventana.blit(text_b6,(780,557))