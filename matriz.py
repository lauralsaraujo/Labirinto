import time
import pygame

def read_labirinto_do_arquivo_txt(arquivo_txt):
    with open(arquivo_txt, 'r') as arquivo:
        lines = arquivo.readlines()

    matrix = [list(map(int, line.strip().split())) for line in lines]

    return matrix

def createSquare(x,y,x1,y1,color,gridDisplay):
   pygame.draw.rect(gridDisplay,color,[x,y,x1,y1])

def createLine(x,y,x1,y1,color,gridDisplay):
   pygame.draw.line(gridDisplay,color,[x,y],[x1,y1])

def createplayer(x,y,color,gridDisplay):
   pygame.draw.circle(gridDisplay,color,[x,y],10)

def visualizeMatrix(mazematrix,gridDisplay):
  y = 0
  for row in range (10):
    x = 35
    for column in range (10):
        if (mazematrix[row][column]) == 0:
            if (column>=1):
               if (mazematrix[row][column-1] == 1):
                  createLine(x,y-1,x,y+34,(0,0,0),gridDisplay)
            if (row>=1):
               if (mazematrix[row-1][column] == 1):
                  createLine(x,y-1,x+35,y-1,(0,0,0),gridDisplay)
        if (mazematrix[row][column]) == 1:
            #createSquare(x,y,35,35,(255,255,255),gridDisplay)
            if (column>=1):
               if (mazematrix[row][column-1] == 0):
                  createLine(x,y-1,x,y+34,(0,0,0),gridDisplay)
            if (row>=1):
               if (mazematrix[row-1][column] == 0):
                  createLine(x,y-1,x+35,y-1,(0,0,0),gridDisplay)
            if (row == 0):
               createLine(x,0,x+35,0,(0,0,0),gridDisplay)
            if (row == 9):
               createLine(x,y+35,x+35,y+35,(0,0,0),gridDisplay)
            if (column == 0):
               createLine(35,y,35,y+35,(0,0,0),gridDisplay)
        if (mazematrix[row][column]) == 2:
            for j in range (row*35,(row*35)+35,5):
                for i in range ((column+1)*35,((column+1)*35)+35,5):
                    if ((i+j)%2 != 0):
                       createSquare(i,j,5,5,(227,86,131),gridDisplay)
            #createSquare(row+35,column,35,35,(255,0,0),gridDisplay)
        if (mazematrix[row][column]) == 3:
             for j in range (row*35,(row*35)+35,5):
                for i in range ((column+1)*35,((column+1)*35)+35,5):
                    if ((i+j)%2 != 0):
                        createSquare(i,j,5,5,(110,191,145),gridDisplay)
        x += 35
    y += 35

def visualizeShape(mazematrix,gridDisplay):
   y = 0
   for row in mazematrix:
      x = 0
      for item in row:
         if item == 1:
            if (row>1):
               if (mazematrix[x-1][y]) == 0:
                  createLine(x,y,x,y+35,(255,0,0),gridDisplay)
         x += 35
      y += 35

def updatePosition(x,y,screen1):
   if(y==0 and x==0):
      return
   createplayer(((y)+1)*(35)+17,((x))*(35)+17,(50,177,204),screen1)
   pygame.display.update()
   time.sleep(0.5)
   createSquare(((y)+1)*(35)+1,((x)*35) +1,30,30,(255,255,255),screen1)