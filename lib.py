import sys
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import pygame
import time as t
from pygame.locals import *
from clases import *
from Preferente_amplitud import *
from Preferente_profundidad import *
from Costo_uniforme import *
from Avara import *
from A import *
from algoritmo import *

class Interfaz:

	def __init__(self):
		self.algoritmo=""
		self.execute=0

	

	#Lee la matriz del archivo de texto
	def leerEntrada(self,namefile):
		self.entrada = []
		#lectura de la entrada
		file  = open(namefile, "r") 
		for line in file:
			line_clean=line.rstrip().split(" ");
			self.entrada.append(line_clean)

	#Retorna el tipo de imagen que debe pintar segun la lectura del archivo
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

	#Se encarga de pintar el ambiente inicial (Ambiente y menu principal)
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
		pygame.display.set_caption("Proyecto#1-Inteligencia Artificial")

		ventana.fill(color)
		#definimos nodo inicial donde se encuentra mario
		self.nodo_inicial=nodo()
		#definimos nodo inicial donde se encuentra mario
		self.nodo_meta=nodo()
		try:
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

			self.nodo_inicial.heuristica=self.calcular_heuristica(self.nodo_inicial,self.nodo_meta)
			self.nodo_inicial.heuristica_peso=self.nodo_inicial.heuristica+self.nodo_inicial.peso
			button = pygame.Rect(640,200,100,30)
			button2 = pygame.Rect(750,200,100,30)
			button3 = pygame.Rect(860,200,100,30)
			button4 = pygame.Rect(690,280,100,30)
			button5 = pygame.Rect(800,280,100,30)
			button6 = pygame.Rect(750,550,100,30)
			button7 = pygame.Rect(870,550,120,30)
			self.menu_principal(ventana,button,button2,button3,button4,button5,button6,button7)
			
			while True:
				
				for evento in pygame.event.get():
					camino_final=""
					if evento.type == QUIT:
						pygame.quit()
						sys.exit()
					if evento.type == pygame.MOUSEBUTTONDOWN:
						mouse_pos = evento.pos  # gets mouse position
						
						# checks if mouse position is over the button
						if button.collidepoint(mouse_pos):
							if self.execute==0:
								tipo_algoritmo = 1
								camino = self.calcular(tipo_algoritmo)
								self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		   
								self.informe_algoritmo(str(self.algoritmo.cant_nodos_expandidos),str(self.algoritmo.profundidad_arbol),str(self.algoritmo.tiempo_ejecucion),ventana)
								self.execute=1
							else:
								self.reset_interfaz_please(ventana,"***por favor reinicie la interfaz")
						if button2.collidepoint(mouse_pos):
							if self.execute==0:
								tipo_algoritmo = 2
								camino = self.calcular(tipo_algoritmo)
								self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		   
								self.informe_algoritmo(str(self.algoritmo.cant_nodos_expandidos),str(self.algoritmo.profundidad_arbol),str(self.algoritmo.tiempo_ejecucion),ventana)
								self.execute=1
							else:
								self.reset_interfaz_please(ventana,"***por favor reinicie la interfaz")
						if button3.collidepoint(mouse_pos):
							if self.execute==0:
								tipo_algoritmo = 3
								camino = self.calcular(tipo_algoritmo)
								self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		   
								self.informe_algoritmo(str(self.algoritmo.cant_nodos_expandidos),str(self.algoritmo.profundidad_arbol),str(self.algoritmo.tiempo_ejecucion),ventana)
								self.execute=1
							else:
								self.reset_interfaz_please(ventana,"***por favor reinicie la interfaz")
						if button4.collidepoint(mouse_pos):
							if self.execute==0:
								tipo_algoritmo = 4
								camino = self.calcular(tipo_algoritmo)
								self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		   
								self.informe_algoritmo(str(self.algoritmo.cant_nodos_expandidos),str(self.algoritmo.profundidad_arbol),str(self.algoritmo.tiempo_ejecucion),ventana)
								self.execute=1
							else:
								self.reset_interfaz_please(ventana,"***por favor reinicie la interfaz")
						if button5.collidepoint(mouse_pos):
							if self.execute==0:
								tipo_algoritmo = 5
								camino = self.calcular(tipo_algoritmo)
								self.pintar_camino(ventana,camino,self.nodo_inicial,self.nodo_meta)		   
								self.informe_algoritmo(str(self.algoritmo.cant_nodos_expandidos),str(self.algoritmo.profundidad_arbol),str(self.algoritmo.tiempo_ejecucion),ventana)
								self.execute=1
							else:
								self.reset_interfaz_please(ventana,"***por favor reinicie la interfaz")
						if button6.collidepoint(mouse_pos):
							self.reset_map(ventana)
							self.menu_principal(ventana,button,button2,button3,button4,button5,button6,button7)
							self.execute=0
						if button7.collidepoint(mouse_pos):
							self.change_file(ventana,button,button2,button3,button4,button5,button6,button7)
							self.execute=0
							

					pygame.display.update()
		
		except Exception as e: 
			print e
			
	
	#Recibe el tipo de algoritmo que desea ejecutar el usuario, y retorna la solucion
	def calcular(self,tipo_algoritmo):
		
		#preferente por amplitud
		if tipo_algoritmo == 1:
			self.algoritmo = Preferente_amplitud(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(self.algoritmo.camino_final))
			return camino
		elif tipo_algoritmo == 2:
			self.algoritmo = Costo_uniforme(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(self.algoritmo.camino_final))
			return camino

		elif tipo_algoritmo == 3:
			self.algoritmo = Preferente_profundidad(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(self.algoritmo.camino_final))
			return camino
		elif tipo_algoritmo == 4:
			self.algoritmo = Avara(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(self.algoritmo.camino_final))
			return camino
		elif tipo_algoritmo == 5:
			self.algoritmo = A(self.entrada,self.nodo_inicial,self.nodo_meta)
			camino=list(reversed(self.algoritmo.camino_final))
			return camino

	#Recibe el ambiente, el camino ganador y pinta en el ambiente la animacion del recorrido
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

	#Pinta el menu principal
	def menu_principal(self,ventana,b_1,b_2,b_3,b_4,b_5,b_6,b_7):
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
		text_b7=font.render("Cambiar Entrada", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_6)
		pygame.draw.rect(ventana, [170, 170, 170], b_7)
		ventana.blit(text_b6,(780,557))
		ventana.blit(text_b7,(878,557))

	#Deja el ambiente en su estado inicial
	def reset_map(self, ventana):
		pygame.mixer.music.stop()
		#dimensiones para la grilla
		color=(255,255,255)#blanco
		colorDos=pygame.Color(0,0,0)#negro
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

		self.algoritmo=None
		self.informe_algoritmo("","","",ventana)
		pygame.display.update()


	#Pintar el informe de la ejecucion del algoritmo
	def informe_algoritmo(self, nodos_expandidos,profundidad,timpo_ejecucion,ventana):
		font = pygame.font.SysFont("comicsansms", 30)
		#Crear Textos Resumen
		cant_nodos=font.render(nodos_expandidos, True, (0, 0, 0))
		prof=font.render(profundidad, True, (0, 0, 0))
		tiempo=font.render(timpo_ejecucion, True, (0, 0, 0))
		#Pintar Resumenes
		ventana.blit(cant_nodos,(660,375))
		ventana.blit(prof,(660,435))
		ventana.blit(tiempo,(660,495))
		pygame.display.update()


	def reset_interfaz_please(self, ventana,error):
		font = pygame.font.SysFont("comicsansms", 20)
		msj=font.render(error, True, (100, 0, 0))
		ventana.blit(msj,(660,580))

	def change_file(self,ventana,b_1,b_2,b_3,b_4,b_5,b_6,b_7):
		root = Tk()
		root.filename = tkFileDialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
		path=root.filename
		root.destroy()
		self.leerEntrada(str(path))
		self.reset_map(ventana)
		self.menu_principal(ventana,b_1,b_2,b_3,b_4,b_5,b_6,b_7)

	def calcular_heuristica(self,nodo_base,nodo_meta):
		x=abs(nodo_base.x-nodo_meta.x)
		
		y=abs(nodo_base.y-nodo_meta.y)
		return x+y