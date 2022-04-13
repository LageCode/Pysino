#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
import os

#Modules de Pypi
import pygame

#Modules de l'application
# ...

WIDTH = 1280                                        #Largeur de l'écran
HEIGHT = 720                                        #Hauteur de l'écran
RESOLUTION = (WIDTH, HEIGHT)                        #Résolution de l'écran
SCREEN = pygame.display.set_mode(RESOLUTION)        #Ecran

DIR = os.path.dirname(os.path.abspath(__file__))

ICON = pygame.image.load(DIR + "\\img\\icon.png").convert_alpha()
TITLE = "Casino Python by Calvleo 6tb"                                      #Titre de la fenêtre
BACKGROUND = pygame.image.load(os.path.join(DIR + "\\img\\background.jpg")).convert_alpha()      #Image de fond

CLOCK = pygame.time.Clock()     #Rafraîchissement de l'écran 
FPS = 60                        #Nombre d'images par seconde

BALANCE_MAX = 100000000000

BUTTON_IMG = pygame.image.load(DIR + '\\img\\btn_unprsd.png').convert_alpha()                      #Image par défaut des boutons
BUTTON_WIDTH = BUTTON_IMG.get_width()
ROLL_BUTTON_IMG = pygame.image.load(DIR + '.\\img\\roll_black_btn_unprsd.png').convert_alpha()      #Image par défaut du bouton noir de la roulette
BALANCE_IMG = pygame.image.load(DIR + '\\img\\balance.png').convert_alpha()                        #Image par défaut du solde
INPUT_IMG = pygame.image.load(DIR + '\\img\\input.png').convert_alpha()                            #Image par défaut de la zone de texte

#Texte d'aide pour la roulette
ROLL_TIP_TXT = """
1.  Entre une mise valide dans la zone de texte
2.  Choisis sur quelle couleur tu veux miser à l'aide des boutons
3.  Probabilités : RED & BLACK => 7/15 | GREEN => 1/15
4.  Multiplicateur : RED & BLACK => x2 | GREEN => x14
"""

FLSB_TIP_TXT = """
1.  Entre une mise valide dans la zone de texte
2.  Choisis sur quelle médaille tu veux miser en cliquant dessus
3.  Probabilités : 1/3
4.  Multiplicateur : x2 
5.  Si après avoir joué et perdu une mise x, tu rejoues une mise y
    qui vaut le double de la mise x et gagnes, tu gagnes non seulement 
    le double de la mise y ainsi que la mise x initialement perdue
"""