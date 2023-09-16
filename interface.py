import pygame
class Image:
    def __init__(self,x,y,image,scale,screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self,posx,posy):
        self.screen.blit(self.image, (self.rect.x+posx ,self.rect.y+posy))

class Button:
    def __init__(self,x,y,image,scale,screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self,x1,y1):
        self.screen.blit(self.image, (self.rect.x+x1, self.rect.y+y1))
        pygame.display.update()
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action
    
    def desenho(self,x1,y1):
        self.screen.blit(self.image, (self.rect.x+x1, self.rect.y+y1))
