#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
# ...

class EndMessage(pygame.sprite.Sprite):
    def __init__(self, screen, win:bool, value:int, x=339, y=100, game_end=False):

        pygame.sprite.Sprite.__init__(self)

        self.surface = screen 

        self.image = pygame.image.load('./img/endbox.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        if game_end:

            if win:
                text = """Tu as gagné, tu as réussi à amasser 
100'000'000'000 jetons, félicitations !"""

            else:
                text = """Le jeu est fini, tu n'as plus de jetons
Tu peux relancer une partie ou quitter le jeu"""

            title = "GAME OVER"

        else:

            if win:
                title = "Félicitations !" 
                word = "gagné"

            else:
                title = "Dommage..."
                word = "perdu"

            text = f"""Tu as {word} {value} jetons\x1fTu peux rejouer ou tenter ta chance sur un autre jeu"""


        title_color = (140, 106, 0)
        text_color = (191, 144, 0)

        self.font_title = pygame.font.SysFont('Consolas', 30)
        self.title = self.font_title.render(title, True, title_color)

        self.font_text = pygame.font.SysFont('Consolas', 17)

        self.surface.blit(self.image, self.rect)
        self.surface.blit(self.title, self.__adjustTitlePos())

        height = self.rect.y + 45
        text_splitted = text.splitlines()
        for line in text_splitted:
            self.text = self.font_text.render(line, True, text_color)
            self.surface.blit(self.text, (self.__adjustLinePos(), height))
            height += 30
            
    def __adjustTitlePos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche du titre de l'objet
        x = (self.rect.x + self.rect.width / 2) - self.title.get_width() / 2
        y = self.rect.y + 5
        return (x, y)        
    
    def __adjustLinePos(self):
    #|-_    Ajuste l'abscisse et l'ordonnée du coin supérieur gauche d'une ligne pour qu'elle soit au milieu du cadre et juste en dessous de la ligne précédente
        return self.rect.x + self.rect.width / 2 - self.text.get_width() / 2
             