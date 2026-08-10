#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.music.load(
            './asset/Galaxy Productions -Voyager cut.wav'
        )
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("BeeCareful!")

        self.running = True
        self.score = None
        self.timer = None

        self.menu = Menu(self.screen)

    def start(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.menu.draw()

            pygame.display.flip()

        pygame.quit()

    def update(self, ):
        pass

    def draw(self, ):
        pass

    def events(self, ):
        pass

    def checkVictory(self, ):
        pass

    def checkGameOver(self, ):
        pass
