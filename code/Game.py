#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MENU_MUSIC,
    GAME_MUSIC
)

from code.Menu import Menu
from code.GameState import GameState
from code.Background import Background
from code.Flower import Flower
from code.Bee import Bee
from code.Pollen import Pollen

class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("BeeCareful!")

        self.clock = pygame.time.Clock()

        self.running = True
        self.score = None
        self.timer = None

        self.menu = Menu(self.screen)
        self.background = Background(self.screen)
        self.flowers = [
            Flower(
                self.screen,
                './asset/pansy.png',
                55,
                310
            ),
            Flower(
                self.screen,
                './asset/tulip.png',
                180,
                310
            ),
            Flower(
                self.screen,
                './asset/sunflower.png',
                300,
                310
            ),
            Flower(
                self.screen,
                './asset/lily.png',
                425,
                310
            ),
            Flower(
                self.screen,
                './asset/rose.png',
                550,
                310
            )
        ]
        self.bee = Bee(self.screen)

        self.pollens = [
            Pollen(self.screen, 100, 250),
            Pollen(self.screen, 200, 180),
            Pollen(self.screen, 350, 230),
            Pollen(self.screen, 480, 170),
        ]

    def start(self):
        while self.running:

            self.clock.tick(60)

            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def change_music(self):
        pygame.mixer.music.load(GAME_MUSIC)
        pygame.mixer.music.play(-1)

    def update(self):
        if self.menu.state == GameState.PLAYING:
            self.bee.move()

            for pollen in self.pollens:
                if not pollen.is_collected():
                    if self.bee.collide(pollen):
                        pollen.collect()

    def draw(self):
        if self.menu.state == GameState.MENU:
            self.menu.draw()

        elif self.menu.state == GameState.PLAYING:
            self.background.draw()

            for flower in self.flowers:
                flower.draw()

            for pollen in self.pollens:
                pollen.draw()

            self.bee.draw()

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif self.menu.state == GameState.MENU:
                if self.menu.startGame(event):
                    self.change_music()

    def checkVictory(self, ):
        pass

    def checkGameOver(self, ):
        pass
