#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
from constants import DIR

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, unprsd_img='btn_unprsd.png', prssd_img='btn_prssd.png', x=0, y=0, text_txt="TITLE", caption_txt="caption", text_color=(140, 106, 0), caption_color=(191, 144, 0)):
    #|-_    Bouton composé d'un texte et d'une légende qui renvoie une valeur en cas d'interaction
        
        pygame.sprite.Sprite.__init__(self)
        
        self.surface = screen
        self.surface_width, self.surface_height = self.surface.get_size()
        
        self.image = pygame.image.load(DIR + "\\img\\btn_unprsd.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.__adjustPos(x, y)
        
        self.action = text_txt.lower().replace(" ", "")
        if self.action == "flashback":
            self.action = "flsb"
        elif self.action.startswith("save") and self.action[-1].isdigit():
            self.action = self.action[-1]
        
        self.text_font = pygame.font.SysFont('Consolas', 25)
        self.text = self.text_font.render(text_txt, True, text_color)
        
        self.caption_font = pygame.font.SysFont('Consolas', 15)
        self.caption = self.caption_font.render(caption_txt, True, caption_color)
        
        self.__editImg(prssd_img)
        self.blit()
        
    def __adjustPos(self, easting, northing):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche de l'objet
        
        return (self.__adjustHorizontally(easting), self.__adjustVertically(northing))
    
    def __adjustHorizontally(self, easting):
    #|-_    Vérifie si l'abscisse est définie et renvoie une valeur dans le cas contraire
        
        return easting or self.surface_width / 2 - self.rect.width / 2
            
    def __adjustVertically(self, northing):
    #|-_    Vérifie si l'ordonnée est définie et renvoie une valeur dans le cas contraire
        
        return northing or self.surface_height / 2 - self.rect.height / 2

    def __adjustTextPos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du texte compris dans le bouton
        
        width, height = self.text.get_size()
        return (self.rect.x + self.rect.width / 2 - width / 2, self.rect.y + self.rect.height / 2 - height / 2)
    
    def __adjustCaptionPos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche de la légende comprise dans le bouton
        
        width, height = self.caption.get_size()
        return (self.rect.x + self.rect.width / 2 - width / 2, self.rect.y + self.rect.height / 2 - height / 2 + 20)
    
    def __editImg(self, img):
    #|-_    Modifie l'image de fond du bouton si la souris le survole
        
        self.image = pygame.image.load(DIR + '\\img\\btn_prssd.png').convert_alpha() if self.checkHover() else self.image
    
    def blit(self):
    #|-_    Affiche l'objet à l'écran soit l'image de fond du bouton, son texte et sa légende
        
        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.__adjustTextPos())
        self.surface.blit(self.caption, self.__adjustCaptionPos())
        
    def checkHover(self):
    #|-_    Vérifie si la souris survole le bouton
        
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def checkClick(self, mouse_click):
    #|-_    Renvoie une valeur si l'utilisateur clique sur le bouton
        
        return self.action if self.checkHover() and mouse_click else None
    