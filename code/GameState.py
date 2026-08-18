#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    VICTORY = 3
    GAME_OVER = 4
    PAUSED = 5
