#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
import constants as const

class Medal(pygame.sprite.Sprite):
    def __init__(self, screen, x:int=0, y:int=0, width:int=120, color_out=(140, 106, 0), color_in=(255, 223, 125), nbr:int=0, win_nbr:int=False, turn:int=0):
    #|-_    Médaille du flashback 
        self.surface = screen
        self.nbr = nbr
        
        self.rect = pygame.Rect(x - (width / 2 - turn / 2), y - width / 2, width - turn, width)
        self.screen_width, self.creen_height = self.surface.get_width(), self.surface.get_height()
            
        self.color_in = color_in
        self.color_out = color_out    
            
        if self.checkHover() and not turn:
            self.color_in = (255, 231, 156)
            
        if turn >= 121:
            if win_nbr == nbr:
                self.color_in = (147, 196, 125)
                self.color_out = (56, 118, 29)
            else:
                self.color_in = (224, 102, 102)
                self.color_out = (153, 0, 0)   
                
        self.blit()     
         
    def blit(self):     
    #|-_    Affiche l'objet soit une ellipse et son contour
        pygame.draw.ellipse(self.surface, self.color_out, self.rect, 5)
        pygame.draw.ellipse(self.surface, self.color_in, self.rect, 0)
        
    def getNbr(self):
    #|-_    Renvoie le numéro de la médaille
        return self.nbr         
         
    def checkHover(self):
    #|-_    Vérifie si la souris survole la médaille
        return self.rect.collidepoint(pygame.mouse.get_pos())
    