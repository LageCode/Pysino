#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
# import constants as const


# DIR = const.DIR

class Tip(pygame.sprite.Sprite):
    def __init__(self, screen, text, color=(255, 230, 153), height=10, img='tip.png'):
        """Crée un bouton qui affiche de l'aide différente en fonction du jeu auquel on joue quand on passe la souris dessus

        Args:
            screen (surface): Ecran de jeu
            text (str): Texte d'aide
            color (tuple, optional): Valeur RGB de la couleur du texte. Defaults to (255, 230, 153).
            height (int, optional): Hauteur de départ du texte. Defaults to 0.
            img (str, optional): Image du bouton. Defaults to 'tip.png'.
        """
        pygame.sprite.Sprite.__init__(self)
   
        self.surface = screen
        self.surface_width = self.surface.get_width()
        
        self.image = pygame.image.load(f'.\\img\\{img}').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (1220, 10)
        
        if self.checkHover():
            self.font = pygame.font.SysFont('Consolas', 20)
            text_splitted = text.splitlines()
            
            for line in text_splitted:
                
                self.text = self.font.render(line, True, color)
                self.surface.blit(self.text, (self.__adjustEasting(), height))
                height += self.text.get_height()
        
        else:
            self.blit()
        
    def __adjustEasting(self):
        """Calcule la valeur de l'absisse nécessaire pour que le texte soit collé à droite

        Returns:
            int: Valeur de la'bscisse
        """
        
        return self.surface_width - self.text.get_width() - 10
    
    def blit(self):
        """Affiche le bouton sur l'écran
        """
        
        self.surface.blit(self.image, self.rect)
    
    def checkHover(self):
        """Vérifie si l'utilisateur passe sur le bouton avec sa souris

        Returns:
            bool: Booléen correspondant à la condition notée ci dessus
        """
        
        return self.rect.collidepoint(pygame.mouse.get_pos())
          