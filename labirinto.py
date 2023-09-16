from queue import deque
import pygame
from matriz import createplayer,createSquare, updatePosition

import random
class No:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pai = None


class Labirinto:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.linhas = len(labirinto)
        self.colunas = len(labirinto[0])
        self.no_inicio = self.encontrar_no(2)
        self.no_fim = self.encontrar_no(3)

    def __getitem__(self, index):
        return self.labirinto[index]

    def encontrar_no(self, valor):
        for x in range(self.linhas):
            for y in range(self.colunas):
                if self.labirinto[x][y] == valor:
                    return No(x, y)
        return None

    def chegou_no_fim(self, x, y):
        return 0 <= x < self.linhas and 0 <= y < self.colunas and self.labirinto[x][y] != 0

    def sucessores(self, no):
        x, y = no.x, no.y
        passos_possiveis = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        passos_validos = []

        for passo_x, passo_y in passos_possiveis:
            if self.chegou_no_fim(passo_x, passo_y):
                passos_validos.append(No(passo_x, passo_y))
        random.shuffle(passos_validos)

        return passos_validos

    def DFS(self,screen1):
        pilha = []
        visitados = set()
        pilha.append(self.no_inicio)
        visitados.add((self.no_inicio.x, self.no_inicio.y))
        
        aux1 = self.no_inicio.x
        aux2 = self.no_inicio.y
        
        
        while pilha:
            
            pygame.display.update()
            no_atual = pilha.pop()
            if (no_atual.pai):
                aux = self.labirinto[no_atual.pai.x][no_atual.pai.y]
                self.labirinto[no_atual.pai.x][no_atual.pai.y] = 0
            
            updatePosition(no_atual.x,no_atual.y,screen1)
            if no_atual.x == self.no_fim.x and no_atual.y == self.no_fim.y:
                caminho = []
                while no_atual:
                    caminho.insert(0, (no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                return caminho

            for no_vizinho in self.sucessores(no_atual):
                #if (no_vizinho.x, no_vizinho.y) not in visitados:
                    no_vizinho.pai = no_atual
                    pilha.append(no_vizinho)
                    visitados.add((no_vizinho.x, no_vizinho.y))
            if (no_atual.pai):
                self.labirinto[no_atual.pai.x][no_atual.pai.y] = aux
        
        
                

    def BFS(self, screen1):
        fila = deque()
        visitados = set()

        fila.append(self.no_inicio)
        visitados.add((self.no_inicio.x, self.no_inicio.y))
        
        while fila:
        
            pygame.display.update()
            no_atual = fila.popleft()
            updatePosition(no_atual.x,no_atual.y,screen1)
            if no_atual.x == self.no_fim.x and no_atual.y == self.no_fim.y:
                caminho = []
                while no_atual:
                    caminho.insert(0, (no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                fila = []
                return caminho

            for no_vizinho in self.sucessores(no_atual):
                if (no_vizinho.x, no_vizinho.y) not in visitados:
                    no_vizinho.pai = no_atual
                    fila.append(no_vizinho)
                    visitados.add((no_vizinho.x, no_vizinho.y))


    def modificar_labirinto_com_caminho(self, caminho):
        for x, y in caminho:
            if self.labirinto[x][y] == 1:
                self.labirinto[x][y] = 7

    def imprimir_labirinto(self):
        for linha in self.labirinto:
            print(" ".join(map(str, linha)))