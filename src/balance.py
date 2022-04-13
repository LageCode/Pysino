#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
import constants as const

class Balance(pygame.sprite.Sprite):
    def __init__(self, screen, value:str, img=const.BALANCE_IMG, x=0, y=0, title="Balance"):
    #|-_    Zone d'affichage de texte non modifiable composée d'un titre
        
        pygame.sprite.Sprite.__init__(self)
        
        self.surface = screen
        self.surface_width, self.surface_height = self.surface.get_size()
        
        self.image = img
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = self.__adjustPos(x, y)
        
        self.value = value
        
        self.title_font = pygame.font.SysFont('Consolas', 25)
        self.title = self.title_font.render(title, True, (255, 230, 153))
        
        self.text_font = pygame.font.SysFont('Consolas', 20)
        self.text = self.text_font.render(self.value, True, (140, 106, 0))
        
        self.blit()
        
    def __adjustPos(self, easting, northing):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du cadre de l'objet
        
        return (self.__adjustHorizontally(easting), self.__adjustVertically(northing))
    
    def __adjustHorizontally(self, easting):
    #|-_    Vérifie si l'abscisse est définie et renvoie une valeur dans le cas contraire
        
        return easting or self.surface_width / 20
        
    def __adjustVertically(self, northing):
    #|-_    Vérifie si l'ordonnée est définie et renvoie une valeur dans le cas contraire
        
        return northing or self.surface_height / 20
    
    def __adjustTitlePos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du titre de l'objet

        return (self.rect.x + self.rect.width / 2 - self.title.get_width() / 2, self.rect.y - self.title.get_height())
    
    def __adjustTextPos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du texte compris dans le cadre
        
        return (self.rect.x + self.rect.width - self.text.get_width() - 5, self.rect.y + self.rect.height / 2 - self.text.get_height() / 2)
    
    def blit(self):
    #|-_    Affiche l'objet  à l'écran soit le titre, le cadre et le texte compris dedans.
        
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.title, self.__adjustTitlePos())
        self.surface.blit(self.text, self.__adjustTextPos())
        