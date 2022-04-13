#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
import constants as const

class Inputbox(pygame.sprite.Sprite):
    def __init__(self, screen, balance:int, value:int, img=const.INPUT_IMG, x=0, y=0):
    #|-_    Zone d’entrée de texte composée d’un titre
        
        pygame.sprite.Sprite.__init__(self)
        
        self.surface = screen
        self.surface_width, self.surface_height = self.surface.get_size()
        
        self.image = img
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = self.__adjustPos(x, y)
        
        self.value = value
        self.balance = balance
        self.__checkValue()
        
        self.title_font = pygame.font.SysFont('Consolas', 25)
        self.title = self.title_font.render("Bet", True, (255, 230, 153))
        
        self.text_font = pygame.font.SysFont('Consolas', 20)
        self.__updateText()
        
        self.blit()
        
    def getValue(self):
    #|-_    Renvoie la valeur comprise dans la zone d'entrée de texte
        return self.value
        
    def __adjustPos(self, easting, northing):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du cadre de l'objet
        
        return (self.__adjustHorizontally(easting), self.__adjustVertically(northing))
    
    def __adjustHorizontally(self, easting):
    #|-_    Vérifie si l'abscisse est définie et renvoie une valeur dans le cas contraire
        
        return easting or self.surface_width / 2 - self.rect.width / 2
        
    def __adjustVertically(self, northing):
    #|-_    Vérifie si l'ordonnée est définie et renvoie une valeur dans le cas contraire
        
        return northing or 200
    
    def __adjustTitlePos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du titre de l'objet
        
        return (self.rect.x + self.rect.width / 2 - self.title.get_width() / 2, self.rect.y - self.title.get_height())
    
    def __adjustTextPos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du texte compris dans le cadre
        
        return (self.rect.x + self.rect.width / 2 - self.text.get_width() / 2, self.rect.y + self.rect.height / 2 - self.text.get_height() / 2)
    
    def __checkValue(self):
    #|-_    Vérifie si la valeur entrée n'est pas supérieure au solde de l'utilisateur
        
        self.value = self.balance if self.value > self.balance else self.value
    
    def __updateText(self):
    #|-_    Actualise le texte affiché dans la zone d'entrée de texte
        
        self.text = self.text_font.render(str(self.value) if self.value > 0 else "", True, (140, 106, 0))
    
    def blit(self):
    #|-_    Affiche l'objet soit le cadre de la zone d'entrée de texte, le titre et la valeur entrée
        
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.title, self.__adjustTitlePos())  
        self.surface.blit(self.text, self.__adjustTextPos())  
    
    def checkHover(self):
    #|-_    Vérifie si la souris survole la zone d'entrée de texte
        
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def input(self, char="", bSpace=False):
    #|-_    Modifie la valeur entrée dans la zone d'entrée de texte en fonction des interactions de l'utilisateur avec le clavier
        
        value_list_char = list(str(self.value))
        
        if bSpace and value_list_char:
            value_list_char.pop(-1)
        elif char != "":
            value_list_char.append(char)
            
        self.value = int("".join(value_list_char)) if value_list_char else 0
        self.__updateText()
        self.blit()
        