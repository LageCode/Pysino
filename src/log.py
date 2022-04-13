#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
# ...

#Modules de Pypi
import pygame

#Modules de l'application
# ...

class Log:
    def __init__(self):
    #|-_    Texte mis en forme pour la création de logs
        self.yellow = '\033[1;33m'  #Yellow
        self.brightRed = '\033[1;91m'
        self.reset = '\033[0;37m'   #Reset color
    
    def place(self, place):
    #|-_    Texte mis en forme pour les étapes du jeu
        return self.yellow + "[{0:4}]  ".format(place.capitalize()) + self.reset
    
    def value(self, value):
    #|-_    Texte mis en forme pour les valeurs
        return self.brightRed + f"{value} " + self.reset 
    