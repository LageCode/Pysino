#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Modules de la librairie par défaut de Python
import random
import json
import datetime

#Modules de Pypi
import pygame

#Modules de l'application
import constants as const
import functions as fnct
import balance as blnc
import inputbox as ipbx
import roll as rl
import end
import tip
import button
import log

#Initialisation du module Pygame
pygame.init()

#Création fenêtre 
SCREEN = const.SCREEN

#Instauration Icône
pygame.display.set_icon(const.ICON)

#Instauration du titre 
pygame.display.set_caption(const.TITLE)

#Instauration image de fond
BACKGROUND = const.BACKGROUND

#Rafraîchissement écran
CLOCK = const.CLOCK

#Instauration boucle principale
game_running = True

#Instauration variable endroit où on se trouve dans le code
game_place = "menu"

#Instauration variable victoire d'une partie
game_win = False

#Instauration solde départ
balance_value = 10000

#Initialisation des variables de jeux
roll_step = 0
flsb_step = 0
flsb_user_replay = False
save_step = 0

# --[logs]--
logGen = log.Log()

print(logGen.place(game_place) + "Démarrage du jeu")       #[log]

#   ||----- Boucle Principale -----||
while game_running:     

    #   ||----- Réinitialisation variables d'évênements -----||
    mouse_click = False     #Variable souris
    keyB_backspace = keyB_enter = keyB_digit = keyB_digit_value = False     #Variables clavier
        
    #   ||----- Boucle d'évênements -----||
    for event in pygame.event.get():        #Récupération évênements
        
        if event.type == pygame.QUIT:       #Clic croix
            game_running = False                #Arrêt du jeu
        
        elif event.type == pygame.MOUSEBUTTONDOWN:      #Clic souris
            
            if event.button == 1:       #Gauche
                mouse_click = True
        
        elif event.type == pygame.KEYDOWN:      #Appui touche
            
            if event.key == 8:      #Retour arrière
                keyB_backspace = True
                
            elif event.key == 13:       #Entrée
                keyB_enter = True
                
            elif event.key in range(48, 58):        #Chiffre
                keyB_digit = True if event.unicode.isdigit() else False     #Vérifie si l'entrée est bien un chiffre
                keyB_digit_value = event.unicode
            
    #   ||----- Jeu -----||
    SCREEN.blit(BACKGROUND, (0, 0))     #Actualisation image de fond
    
    # |---------------------------------------------------------------------------------------|
    balance = blnc.Balance(SCREEN, str(balance_value))      #Création case solde
       
    if game_place in ["roll", "flsb", "save"] and roll_step != 3 and flsb_step != 2 and save_step == 0:     #Vérification game_place
        menu_btn = button.Button(SCREEN, x=64, y=620, text_txt="Menu", caption_txt="")      #Création bouton retour au menu       
        menu_btn_result = fnct.check_button_list(menu_btn, mouse_click)      #Récupération interaction bouton
        if menu_btn_result:     #Vérification interaction
            print(logGen.place(game_place) + "Mise à jour place => " + logGen.value(menu_btn_result))     #[log]
            game_place = menu_btn_result        #Actualisation game_place
    
    if game_place == "save" and save_step != 0:     #Vérification game_place
        back_btn = button.Button(SCREEN, x=64, y=620, text_txt="Back", caption_txt="")      #Création bouton retour arrière
        back_btn_result = fnct.check_button_list(back_btn, mouse_click)      #Récupération interaction bouton
        if back_btn_result:     #Vérification interaction
            print(logGen.place(game_place) + "Retour arrière")      #[log]
            save_step = 0       #Actualisation étape sauvegarde
            
    
    if game_place == "end":     #Vérification game_place
        game_end_message = end.EndMessage(SCREEN, game_win, balance_value, game_end=True)       #Création message Game Over

        end_btn_list = fnct.menu__create_end_buttons(SCREEN)       #Création boutons fin du jeu
        end_btn_list_result = fnct.check_button_list(end_btn_list, mouse_click)      #Récupération interaction boutons
        if end_btn_list_result == "replay":     #Vérification interaction 
            balance_value = 10000       #Réinitialisation solde
            print(logGen.place(game_place) + "Solde mis à jour => " + logGen.value(str(balance_value)))       #[log]
            print(logGen.place(game_place) + "Mise à jour place => " + logGen.value("menu"))      #[log]
            game_place = "menu"     #Actualisation game_place
            
        elif end_btn_list_result == "exit":     #Vérification interaction 
            print(logGen.place(game_place) + "Arrêt du jeu")       #[log]      
            game_running = False        #Arrêt du jeu
    
    if game_place == "menu":        #Vérification game_place
        roll_step = flsb_step = save_step = 0       #Réinitialisation variables jeux
        menu_btn_list = fnct.menu__create_main_buttons(SCREEN)     #Création boutons menu
        menu_btn_list_result = fnct.check_button_list(menu_btn_list, mouse_click)        #Récupération interaction boutons
        if menu_btn_list_result:        #Vérification interaction                         
            print(logGen.place(game_place) + "Mise à jour place => " + logGen.value(menu_btn_list_result))        #[log]
            game_place = menu_btn_list_result       #Actualisation game_place
                  
    elif game_place == "roll":      #Vérification game_place                       
        roll_tip = tip.Tip(SCREEN, const.ROLL_TIP_TXT)      #Création astuce roulette
        
        if roll_step == 0:      #Première étape roulette
            
            print(logGen.place(game_place) + "Initialisation roulette")        #[log]
            #   ||----- Ré-initialisation variables roulette -----||
            roll_input_active = False       #Etat zone d'entrée de texte
            roll_user_bet_value = 1000      #Somme misée par le joueur
            roll_user_bet_color = None      #Couleur sur laquelle le joueur a misé
            
            roll_user_bet_withdrawn = False     #Retranchement somme misée par le joueur
            roll_roll = None        #Objet roulette
            roll_win_nbr = None     #Nombre gagnant
            roll_win_color = None       #Couleur gagnante
            
            roll_turn_count = 0     #Nombre tours effectués par la roulette
            
            roll_user_win = False       #Victoire du joueur
            roll_user_gain_given = False        #Ajout du gain au solde en cas de victoire
            roll_log_printed = False        #Variable 
            roll_user_gain_value = 0        #Valeur du gain en cas de victoire

            roll_step = 1       #Actualisation étape roulette
            
        elif roll_step == 1:        #Deuxième étape roulette
            roll_ipbx = ipbx.Inputbox(SCREEN, balance_value, roll_user_bet_value)       #Zone d'entrée de texte                          
            if roll_ipbx.checkHover():      #Vérification survolement bouton
                if mouse_click:     #Vérification clic souris
                    roll_input_active = True        #Actualisation état zone d'entrée de texte
            
            if roll_input_active:       #Vérification état zone d'entrée de texte
                if keyB_digit:      #Vérification entrée chiffre
                    roll_ipbx.input(keyB_digit_value)       #Ajout chiffre zone de texte
                    
                elif keyB_backspace:        #Vérification touche retour arrière
                    roll_ipbx.input(bSpace=True)        #Retranchement dernier chiffre zone de texte
                    
                elif keyB_enter:        #Vérification touche entrée
                    roll_input_active = False       #Actualisation état zone d'entrée de texte              
                    
            roll_user_bet_value = roll_ipbx.getValue()      #Récupération valeur mise
            
            roll_btn_list = fnct.roll__create_buttons(SCREEN)     #Création boutons mise roulette
            roll_user_bet_color = roll_btn_list_result = fnct.check_button_list(roll_btn_list, mouse_click)      #Récupération interaction boutons
            if roll_user_bet_color and roll_user_bet_value:     #Vérification interaction
                print(logGen.place(game_place) + "Mise de " + logGen.value(str(roll_user_bet_value)) + "sur la couleur " + logGen.value(roll_user_bet_color))        #[log]
                roll_step = 2       #Actualisation étape roulette                    
        
        elif roll_step == 2:        #Troisième étape roulette
            if not roll_user_bet_withdrawn:     #Vérification retranchement mise
                balance_value -= roll_user_bet_value        #Retranchement mise au solde
                roll_user_bet_withdrawn = True      #Actualisation variable vérification retranchement mise
            
            roll_roll = rl.Roll(SCREEN)     #Création objet roulette
            roll_win_nbr = fnct.roll__set_win_nbr(roll_roll)       #Initialisation nombre gagnant roulette
            roll_win_color = roll_roll.getCorrColor(roll_win_nbr)       #Initialisation couleur gagnante roulette
            print(logGen.place(game_place) + "Lancement de la roulette")       #[log]
            roll_step = 3       #Actualisation étape roulette
        
        elif roll_step == 3:        #Quatrième étape roulette
            roll_roll.moveLeft()        #Déplacement roulette
            roll_roll.showRoll()        #Affichage roulette
            
            if fnct.roll__is_win_tile_mid(roll_roll, roll_win_nbr) and roll_turn_count > 1:     #Vérification tile gagnante au milieu
                print(logGen.place(game_place) + "Tuile gagnante => " + logGen.value(roll_win_nbr))       #[log]
                roll_step = 4       #Actualisation étape roulette
                
            elif fnct.roll_turned(roll_roll):       #Vérification tour roulette
                roll_turn_count += 1        #Actualisation nombre de tour roulette
        
        elif roll_step == 4:        #Cinquième étape roulette
            roll_roll.showRoll()        #Affichage roulette
            
            if roll_win_color == roll_user_bet_color:       #Vérification victoire joueur
                roll_user_win = True        #Actualisation variable victoire joueur
                
                if not roll_user_gain_given:        #Vérification ajout gain au solde
                    roll_user_gain_value = roll_user_bet_value * roll_roll.getMult(roll_win_nbr)        #Initialisation valeur gain joueur en cas de victoire
                    balance_value += roll_user_gain_value       #Ajout gain au solde du joueur
                    roll_user_gain_given = True     #Actualisation ajout gain au solde
                    
            if not roll_log_printed:
                    print(logGen.place(game_place) + logGen.value("Victoire" if roll_user_win else "Défaite"))        #[log]
                    print(logGen.place(game_place) + (f"Gain de " if roll_user_win else "Perte de ") + (logGen.value(str(roll_user_gain_value) if roll_user_win else str(roll_user_bet_value))))      #[log]  
                    roll_log_printed = True     #[log]
                    
            if balance_value >= const.BALANCE_MAX or not balance_value:     #Vérification solde
                game_place = "end"      #Actualisation game_place
                game_win = False if not balance_value else True     #Actualisation variable victoire jeu
                print(logGen.place(game_place) + (("Victoire, solde d'au moins " + logGen.value(str(const.BALANCE_MAX))) if game_win else ("Défaite, solde " + logGen.value("nul"))))        #[log]
                
            else:
                roll_end_message = end.EndMessage(SCREEN, roll_user_win, roll_user_gain_value or roll_user_bet_value)       #Création message fin de partie   
                replay_btn = button.Button(SCREEN, x=const.WIDTH - const.BUTTON_WIDTH - 64, y=620, text_txt="Replay", caption_txt="")       #Création bouton rejouer
                replay_btn_result = fnct.check_button_list(replay_btn, mouse_click)      #Récupération interaction bouton
                if replay_btn_result:       #Vérification interaction bouton
                    print(logGen.place(game_place) + "Relancement de la roulette")     #[log]
                    roll_step = 0       #Actualisation étape roulette
            
    elif game_place == "flsb":      #Vérification game_place
        flsb_tip = tip.Tip(SCREEN, const.FLSB_TIP_TXT)      #Création astuce Flashback
        
        if flsb_step == 0:      #Vérification étape  
            print(logGen.place(game_place) + "Initialisation flash back")      #[log]
            #   ||----- Ré-initialisation variables roulette -----||
            flsb_user_bet_value = 2 * flsb_user_bet_value if flsb_user_replay and balance_value >= 2 * flsb_user_bet_value else 1000        #Mise par défaut proposée au joueur
            flsb_user_last_bet_value = flsb_user_bet_value // 2 if flsb_user_replay else None       #Ancienne mise jouée par le joueur
            flsb_input_active = False       #Etat zone d'entrée de texte
            flsb_user_bet_withdrawn = False     #Mise retirée du solde
            flsb_user_bet_nbr = None        #Nombre sur lequel le joueur mise
            flsb_win_nbr = None     #Nombre gagnant tiré aléatoirement
            
            flsb_medal_turn = 0     #Phase de rotation des médailles
            
            flsb_user_win = False       #Victoire du joueur
            flsb_user_gain_value = None     #Gain du joueur en cas de victoire
            flsb_user_gain_given = False        #Gain donné au joueur
            flsb_log_printed = False        #Affichage log 
            
            flsb_step = 1       #Etape du jeu
                 
        elif flsb_step == 1:        #Vérification étape du jeu
            flsb_ipbx = ipbx.Inputbox(SCREEN, balance_value, flsb_user_bet_value)       #Création zone d'entrée de texte de la mise
            if flsb_ipbx.checkHover():      #Souris passe sur le bouton
                if mouse_click:     #Clic sur la souris
                    flsb_input_active = True        #Actualisation état zone d'entrée de texte
                    
            if flsb_input_active:       #Vérification état zone d'entrée de texte    
                if keyB_digit:      #Vérification Chiffre
                    flsb_ipbx.input(keyB_digit_value)       #Ajout chiffre
                    
                elif keyB_backspace:        #Vérification retour arrière
                    flsb_ipbx.input(bSpace=True)        #Retour arrière
                    
                elif keyB_enter:        #Vérification entrée
                    flsb_input_active = False       #Actualisation état zone d'entrée de texte
                                     
            flsb_user_bet_value = flsb_ipbx.getValue()      #Valeur mise dans zone d'entrée de texte

            flsb_medal_list = fnct.flsb__create_medals(SCREEN)        #Liste de médailles
            for medal in flsb_medal_list:       #Listing médaille dans liste de médailles
                if medal.checkHover():      #Vérification souris passe sur la médaille
                    if mouse_click:     #Vérification clic souris
                        if not flsb_user_bet_withdrawn:     #Vérification retrait mise du solde
                            balance_value -= flsb_user_bet_value        #Retrait mise du solde
                            flsb_user_bet_withdrawn = True      #Actualisation variable retrait
                            
                        flsb_user_bet_nbr = medal.getNbr()      #Nombre sur lequel le joueur mise   
                        flsb_win_nbr = random.randrange(3)      #Nombre gagnant 
                        flsb_step = 2       #Actualisation étape jeu
                        print(logGen.place(game_place) + "Mise de " + logGen.value(str(flsb_user_bet_value)) + "sur la médaille n°" + logGen.value(str(flsb_user_bet_nbr + 1)))      #[log]
                        print(logGen.place(game_place) + "Médaille gagnante => " + logGen.value(str(flsb_win_nbr + 1)))       #[log]
                            
        elif flsb_step == 2:        #Vérification étape du jeu
            flsb_medal_list = fnct.flsb__create_medals(SCREEN, win_nbr=flsb_win_nbr, turn=flsb_medal_turn)        #Création liste médaille
            flsb_medal_turn += 1        #Incrémentation variable rotation médailles
            
            if flsb_medal_turn >= 240:      #Vérification variable rotation
                flsb_step = 3       #Actualisation étape jeu
                
        elif flsb_step == 3:        #Vérification étape du jeu
            for medal in flsb_medal_list:   
                medal.blit()        #Affichage médaille
                
            if flsb_user_bet_nbr == flsb_win_nbr:       #Vérification égalité nbr joué et nombre gagnant
                flsb_user_win = True        #Actualisation victoire du joueur

                if not flsb_user_gain_given:        #Gain non donné                                                                                                                       
                    flsb_user_gain_value = int(2.5 * flsb_user_bet_value) if flsb_user_replay and flsb_user_bet_value == 2 * flsb_user_last_bet_value else 2 * flsb_user_bet_value      #Gain donné au joueur
                    balance_value += flsb_user_gain_value       #Ajout du gain au solde
                    flsb_user_gain_given = True     #Actualisation variable gain donné au joueur  

            if not flsb_log_printed:        #Log non affichée
                print(logGen.place(game_place) + logGen.value("Victoire" if flsb_user_win else "Défaite"))        #[log]
                print(logGen.place(game_place) + (f"Gain de " if flsb_user_win else "Perte de ") + (logGen.value(str(flsb_user_gain_value) if flsb_user_win else str(flsb_user_bet_value))))      #[log]
                flsb_log_printed = True     #Actualisation variable affichage log

            flsb_user_replay = False        #Actualisation variable replay                  
                    
            if balance_value >= const.BALANCE_MAX or not balance_value:     #Vérification solde
                game_place = "end"      #Actualisation game_place
                game_win = False if not balance_value else True     #Actualisation variable victoire jeu
                print(logGen.place(game_place) + (("Victoire, solde d'au moins " + logGen.value(str(const.BALANCE_MAX))) if game_win else ("Défaite, solde " + logGen.value("nul"))))        #[log]
                
            else:
                flsb_end_message = end.EndMessage(SCREEN, flsb_user_win, flsb_user_gain_value or flsb_user_bet_value)       #Création message fin de partie   
            
                replay_btn = button.Button(SCREEN, x=const.WIDTH - const.BUTTON_WIDTH - 64, y=620, text_txt="Replay", caption_txt="")       #Création bouton rejouer
                replay_btn_result = fnct.check_button_list(replay_btn, mouse_click)      #Récupération interaction bouton
                if replay_btn_result:       #Vérification interaction bouton
                    flsb_user_replay = True if not flsb_user_win and balance_value >= 2 * flsb_user_bet_value else False        #Actualisation variable replay
                    flsb_step = 0       #Actualisation étape roulette
                    print(logGen.place(game_place) + "Relancement du flash back")      #[log]
                        
    elif game_place == "save":      #Vérification game_place                  
        if save_step == 0:      #Vérification étape
            
            save_btn_list = fnct.save__create_button_list(SCREEN)     #Création boutons de sauvegarde        
            save_btn_list_result = fnct.check_button_list(save_btn_list, mouse_click)        #Réception interaction boutons
            if save_btn_list_result:        #Vérification interaction
                save_step = int(save_btn_list_result)       #Définition étape en fonction de l'interaction
            
        elif save_step in [1, 2, 3, 4, 5]:      #Vérification interaction
            with open('./data/save.json', 'r') as file:      #Ouverture du fichier save.json
                data = json.load(file)      #Récupération des données

            save_balance_value_list = [dic['balanceValue'] for dic in data]         #Création liste avec les valeurs des soldes sauvegardés
            save_date_list = [dic['date'] for dic in data]      #Création liste avec les valeurs des dates sauvegardées

            save_balance_value = data[save_step - 1]['balanceValue']        #Récupération du solde ciblé
            save_date_text = data[save_step - 1]['date']        #Récupération de la date ciblée
            
            save_date_font = pygame.font.SysFont('Consolas', 15)        #Instauration police bouton sauvegarde
            save_date = save_date_font.render(save_date_text, True, (191, 144, 0))      #Création texte bouton
            
            save_balance = blnc.Balance(SCREEN, str(save_balance_value), const.BALANCE_IMG, const.WIDTH / 2 - const.BALANCE_IMG.get_width() / 2, 250, "Save" + str(save_step))      #Création zone d'affichage solde ciblé
            
            save_btn_choice_list = fnct.save__create_choice_buttons(SCREEN)        #Liste des boutons relatifs à la sauvegarde
            save_btn_choice_list_result = fnct.check_button_list(save_btn_choice_list, mouse_click)        #Résultat interactions avec boutons
            if save_btn_choice_list_result == "ecraser":        #Si interaction = écraser                    
            
                save_date_list[save_step - 1] = datetime.datetime.today().strftime('%d-%m-%Y')      #Remplacement date visée par celle d'aujourd'hui
                save_balance_value_list[save_step - 1] = balance_value      #Remplacement solde ciblé par le nouveau
                
                new_data = [{"balanceValue" : save_balance_value_list[_], "date" : save_date_list[_]} for _ in range(5)]        #Réécriture des données pour le fichier json
                
                with open('./data/save.json', 'w') as file:        #Ouverture du fichier json en écriture 
                    json.dump(new_data, file, indent=4)     #Ecrasement des données de sauvegarde par les nouvelles
                    
                print(logGen.place(game_place) + "Ecrasement sauvegarde n° " + logGen.value(str(save_step)))      #[log]
                    
            elif save_btn_choice_list_result == "charger":      #Si interaction = charger
                print(logGen.place(game_place) + "Chargement sauvegarde N° " + logGen.value(str(save_step)))      #[log]
                balance_value = save_balance_value          #Remplacement valeur solde par la sauvegarde
                    
            SCREEN.blit(save_date, (const.WIDTH / 2 - save_date.get_width() / 2, 285))      #Affichage de la date sous le solde       
    
    # |---------------------------------------------------------------------------------------|
    
    #   ||----- Rafraîchissement écran avec nouveaux éléments -----||
    pygame.display.flip()
    CLOCK.tick(const.FPS)

#Fermeture fenêtre
pygame.quit()
    