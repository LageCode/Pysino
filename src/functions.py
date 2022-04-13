#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modules de la librairie par défaut de Python
import random
import json

# Modules de Pypi
import pygame

# Modules de l application
import constants as const
import button as bt
import roll as rl
import flashback as fl

SCREEN = const.SCREEN
Button = bt.Button
Roll = rl.Roll
Medal = fl.Medal


# ||----- Fonctions relatives aux boutons -----||
def _calculate_btn_pos(screen: pygame.Surface = SCREEN,
                       nbr: int = 0,
                       img: pygame.image = const.BUTTON_IMG) -> list[int]:
    """
    Renvoie une liste d'entiers (int) qui sont les valeurs de chacune des abscisses des coins supérieurs gauches des
    boutons afin qu'ils soient parfaitement espacés lors de l'affichage.

    @param screen: pygame.Surface = SCREEN
    @param nbr: int = 0
    @param img: pygame.image = const.BUTTON_IMG
    @return: list[int]
    """
    screen_width = screen.get_width()
    btn_width = img.get_width()

    btn_width_total = nbr * btn_width
    screen_width_free = screen_width - btn_width_total

    space_width = screen_width_free // (nbr + 1)

    return [(btn_id + 1) * space_width + btn_id * btn_width for btn_id in range(nbr)]


def check_button_list(btn_list: list or Button, mouse_click: bool = False) -> str or None:
    """
    Renvoie l'action du bouton sur lequel la souris est si l'utilisateur clique sur le bouton gauche de la souris sinon
    renvoie False
    @param btn_list: list or Button
    @param mouse_click: bool = False
    @return: str or None
    """
    if type(btn_list) == list:
        # bt: Button
        for btn in btn_list:
            if btn.checkHover():
                return btn.checkClick(mouse_click)
    elif type(btn_list) == Button:
        return btn_list.checkClick(mouse_click)

    return None


def menu__create_main_buttons(screen: pygame.Surface = SCREEN,
                              height: int = 325,
                              img: pygame.image = const.BUTTON_IMG) -> list[Button]:
    """
    Crée et affiche les 3 boutons du menu principal et les renvoie sous forme de liste
    @param screen: pygame.Surface = SCREEN
    @param height: int = 325
    @param img: pygame.image = const.BUTTON_IMG
    @return: list[Button]
    """
    btn_pos_list = _calculate_btn_pos(screen, 3, img)
    text_list = ["Roll", "Flashback", "Save"]

    return [
        bt.Button(
            screen,
            x=btn_pos_list[text_list.index(text)],
            y=height,
            text_txt=f"{text}",
            caption_txt=""
        )
        for text in text_list
    ]


def menu__create_end_buttons(screen: pygame.Surface = SCREEN,
                             height: int = 620,
                             img: pygame.image = const.BUTTON_IMG) -> list[Button]:
    """
    Crée et affiche les 2 boutons de fin de partie et les renvoie sous forme de liste
    @param screen: pygame.Surface = SCREEN
    @param height: int = 620
    @param img: pygame.image = const.BUTTON_IMG
    @return: list[Button]
    """

    btn_pos_list = _calculate_btn_pos(screen, 2, img)
    text_list = ["Replay", "Exit"]

    return [
        bt.Button(
            screen,
            x=btn_pos_list[text_list.index(text)],
            y=height,
            text_txt=f"{text}",
            caption_txt=""
        )
        for text in text_list
    ]


def roll__create_buttons(screen: pygame.Surface = SCREEN, img: pygame.image = const.ROLL_BUTTON_IMG) -> list[Button]:
    """
    Crée une liste qui contient les boutons de placement de mise de la roulette
    @param: screen: pygame.Surface = SCREEN
    @param: img: pygame.image = const.ROLL_BUTTON_IMG
    @return: list[Button]
    """

    btn_pos_list = _calculate_btn_pos(screen, 3, img)
    color_list = ["red", "green", "black"]

    return [
        bt.Button(
            screen,
            f'roll_{color}_btn_unprsd.png',
            f'roll_{color}_btn_prssd.png',
            btn_pos_list[color_list.index(color)],
            360,
            f"{color.capitalize()}",
            "",
            (255, 255, 255),
        )
        for color in color_list
    ]


def roll__set_win_nbr(roll: Roll) -> int:
    """
    Sélectionne le nombre gagnant de la roulette
    @param: roll: Roll
    @return: int
    """

    return random.choice(roll.getNumberList())


def roll__get_tile_pos(roll: Roll, nbr: int) -> int:
    """
    Renvoie l'abscisse du coin supérieur gauche de la tuile correspondante au numéro entré
    @param: roll: Roll
    @param: nbr: int
    @return: int
    """

    tile = roll.getCorrTile(nbr)
    return tile.getAbs()


def roll__is_win_tile_mid(roll: Roll, nbr: int) -> bool:
    """
    Vérifie si la tuile gagnante de la roulette est au milieu de l'écran
    @param: roll: Roll
    @param: nbr: int
    @return: bool
    """

    return roll__get_tile_pos(roll, nbr) == 608


def roll_turned(roll: Roll) -> bool:
    """
    Vérifie si la roulette a effectué un tour complet
    @param: roll: Roll
    @return: bool
    """

    return roll__get_tile_pos(roll, 0) == 1280


def _calculate_medal_pos(nbr: int, screen_width: int = const.WIDTH) -> list[int]:
    """
    Renvoie les valeurs des abscisses des médailles du Flash back sous forme de liste pour qu'elles soient parfaitement
    alignées horizontalement sur l'écran
    @param: nbr: int
    @param: screen_width: int = const.WIDTH
    @return: list[int]
    """

    return [int((_ + 1) * screen_width / (nbr + 1)) for _ in range(nbr)]


def flsb__create_medals(screen: pygame.surface = SCREEN,
                        height: int = 350,
                        nbr: int = 3,
                        win_nbr: bool = False,
                        turn: int = 0) -> list[Medal]:
    """
    Crée et affiche les trois médailles du Flash back et renvoie ces médailles sous forme de liste
    @param: screen: pygame.surface = SCREEN
    @param: height: int = 350
    @param: nbr: int = 3
    @param: win_nbr: bool = False
    @param: turn: int = 0
    @return: list[Medal]
    """

    return [
        fl.Medal(
            screen,
            x=_calculate_medal_pos(nbr)[_],
            y=height,
            nbr=_,
            win_nbr=win_nbr,
            turn=turn
        )
        for _ in range(nbr)
    ]


def save__create_choice_buttons(screen: pygame.surface = const.SCREEN,
                                height: int = 325,
                                img: pygame.image = const.BUTTON_IMG) -> list[Button]:
    """
    Crée et affiche deux boutons relatifs aux sauvegardes (Ecraser ou Charger) et les renvoies sous forme de liste
    @param: screen: pygame.surface = const.SCREEN
    @param: height: int = 325
    @param: img: pygame.image = const.BUTTON_IMG
    @return list[Button]
    """

    btn_pos_list = _calculate_btn_pos(screen, 2, img)
    text_list = ["Ecraser", "Charger"]

    return [
        bt.Button(
            screen,
            x=btn_pos_list[text_list.index(_)],
            y=height,
            text_txt=_,
            caption_txt=""
        )
        for _ in text_list
    ]


def save__create_button_list(screen: pygame.surface = const.SCREEN,
                             nbr: int = 5,
                             height: int = 350,
                             img: pygame.image = const.BUTTON_IMG) -> list[Button]:
    """
    Crée et affiche les 5 boutons des sauvegardes et les renvoie sous forme de liste
    @param screen: pygame.surface = const.SCREEN
    @param nbr: int = 5
    @param height: int = 350
    @param img: pygame.image = const.BUTTON_IMG
    @return: list[Button]
    """

    pos_list = _calculate_btn_pos(screen, nbr, img)

    with open('./data/save.json', 'r') as file:
        data = json.load(file)

    text_list = range(1, 6)
    balance_value_list = [dic['balanceValue'] for dic in data]

    return [
        bt.Button(
            screen,
            x=pos_list[_ - 1],
            y=height,
            text_txt=f'SAVE{_}',
            caption_txt=str(balance_value_list[_ - 1]),
        )
        for _ in text_list
    ]
