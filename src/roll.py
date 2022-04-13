#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
import random

#Modules de Pypi
import pygame

#Modules de l'application
# ...

class Tile(pygame.sprite.Sprite):
    def __init__(self, screen, number, x, y):
    #|-_    Tuile de la roulette numérotée
        pygame.sprite.Sprite.__init__(self)
        
        self.surface = screen
        
        self.green_list = [0]
        self.red_list = [1, 3, 5, 7, 9, 11, 13]
        self.black_list = [2, 4, 6, 8, 10, 12, 14]
        
        self.number = str(number)
        
        if int(number) in self.red_list:
            img = "roll_red_tile.png"
            self.color = "red"
        elif int(number) in self.black_list:
            img = "roll_black_tile.png"
            self.color = "black"
        else:
            img = "roll_green_tile.png"
            self.color = "green"
            
        self.image = pygame.image.load(f'./img/{img}').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        
        self.font = pygame.font.SysFont('Arial', 25)
        self.text = self.font.render(self.number, True, (255, 255, 255))

        self.blit()
        
    def __adjustNumberPos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du numéro composant la tuile pour qu'il soit centré
        
        return (self.rect.x + self.rect.width / 2 - self.text.get_width() / 2, self.rect.y + self.rect.height / 2 - self.text.get_height() / 2)
        
    def blit(self):
    #|-_    Affiche l'objet soit la tuile et son numéro
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.__adjustNumberPos())
        
    def getAbs(self):
    #|-_    Renvoie la valeur de l'abscisse du coin supérieur gauche de la tuile
        return self.rect.x 
    
    def getColor(self):
    #|-_    Renvoie la couleur de la tuile
        return self.color
    
    def setPos(self, nx, ny=350):
    #|-_    Modifie l'abscisse et l'ordonnée du coin supérieur gauche de la tuile
        self.rect.x = nx
        self.rect.y = ny
        
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen):
    #|-_    Barre latérale de la roulette qui représente la bille
        pygame.sprite.Sprite.__init__(self)
        
        self.surface = screen
        
        self.image = pygame.image.load('./img/roll_ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (638, 320)
        
        self.blit()
        
    def blit(self):
    #|-_    Affiche la barre
        self.surface.blit(self.image, self.rect)
        
class Roll(pygame.sprite.Sprite):
    #|-_    Roulette avec les tuiles et la barre
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.surface = screen
        
        self.number_list = []
        self.red_list = [1, 3, 5, 7, 9, 11, 13]
        self.black_list = [2, 4, 6, 8, 10, 12, 14]
        
        random.shuffle(self.red_list)
        random.shuffle(self.black_list)
        
        for i in range(7):       
            self.number_list.append(self.black_list[i])
            self.number_list.append(self.red_list[i])
            
        self.number_list.append(0)
        
        self.x = 0 
        self.y = 350
        
        self.roll_list = []
        
        for number in self.number_list:
            self.roll_list.append(Tile(self.surface, number, self.x, self.y))
            self.x += 70 + 300 / 14
            
        self.ball = Ball(self.surface)
            
    def getNumberList(self):
    #|-_    Renvoie la liste des numéros composants la roulette
        return self.number_list
    
    def getCorrTile(self, nbr:int):
    #|-_    Renvoie la tuile correspondante au numéro entré
        return self.roll_list[self.number_list.index(nbr)]
    
    def getCorrColor(self, nbr:int):
    #|-_    Renvoie la couleur de la tuile correspondante au numéro entré
        return self.getCorrTile(nbr).getColor()
    
    def getMult(self, nbr:int):
    #|-_    Renvoie le multiplicateur de mise relatif à la couleur de la tuile corespondante au numéro entré
        if self.getCorrColor(nbr) == "green":
            return 14
        else:
            return 2    
    
    def moveLeft(self):
    #|-_    Fait bouger toutes les tuiles vers la gauche
        for tile in self.roll_list:
            if tile.getAbs() <= -70:
                tile.setPos(1280 + 300 / 14)
            else:
                tile.setPos(tile.getAbs() - 7)
            
    def showRoll(self):
    #|-_    Affiche l'objet soit toutes les tuiles qui composent la roulette et la barre latérale
        for tile in self.roll_list:
            tile.blit()
        self.ball.blit()
        