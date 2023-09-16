import pygame
import interface
import labirinto
from matriz import read_labirinto_do_arquivo_txt
from labirinto import Labirinto
from matriz import createLine
from matriz import createSquare
from matriz import visualizeMatrix
from time import sleep
import random
import sys
from tkinter import filedialog

pygame.init()
screen1 = pygame.display.set_mode((400,400))
pygame.display.set_caption('Caio Pedrosa & Laura Araujo')


escolha = '-1'
fim = False
dfs_img = pygame.image.load('figuras/botao_dfs.PNG').convert_alpha()
bfs_img = pygame.image.load('figuras/botao_bfs.PNG').convert_alpha()
labirinto_img = pygame.image.load('figuras/escolha.PNG').convert_alpha()
logo_img = pygame.image.load('figuras/logo.PNG').convert_alpha()
logo = interface.Image(115,40,logo_img,0.5,screen1)
logo_game = interface.Image(115,40,logo_img,0.2,screen1)
dfs_button = interface.Button(40,160,dfs_img,0.5,screen1)
bfs_button = interface.Button(208,160,bfs_img,0.5,screen1)
escolha_button = interface.Button(58,260,labirinto_img,0.5,screen1)
labirinto =[]
running = True
caminho = -1
while running:
   screen1.fill((255,255,255))
   logo.draw(-60,0)
   bfs_button.desenho(0,0)
   dfs_button.desenho(0,0)
   escolha_button.desenho(0,0)
   pygame.display.update()
   
   if escolha_button.draw(0,0):
      fileName = filedialog.askopenfilename()
      matriz = read_labirinto_do_arquivo_txt(fileName)
      matriz_original = read_labirinto_do_arquivo_txt(fileName)
      labirinto = Labirinto(matriz)

   if dfs_button.draw(0,0):
      if not labirinto:
         fileName = 'labirintos/lab0' + str(random.randint(0,3)) +'.txt'
         matriz = read_labirinto_do_arquivo_txt(fileName)
         matriz_original = read_labirinto_do_arquivo_txt(fileName)
         labirinto = Labirinto(matriz)
      screen1.fill((255,255,255))
      logo_game.draw(150,320)
      visualizeMatrix(matriz_original,screen1)
      pygame.display.update()
      sleep(2)
      caminho = labirinto.DFS(screen1)
      labirinto =[]

   elif bfs_button.draw(0,0): 
      if not labirinto:
         fileName = 'labirintos/lab0' + str(random.randint(0,3)) +'.txt'
         matriz = read_labirinto_do_arquivo_txt(fileName)
         matriz_original = read_labirinto_do_arquivo_txt(fileName)
         labirinto = Labirinto(matriz)
      screen1.fill((255,255,255))
      logo_game.draw(150,320)
      visualizeMatrix(matriz_original,screen1)
      pygame.display.update()
      sleep(2)
      caminho = labirinto.DFS(screen1)
      labirinto =[]
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
   pygame.display.update()
   