#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(600, 480))
        pygame.display.set_caption("BeeCareful!")
        self.running = True
        self.score = None
        self.timer = None
        self.menu = Menu(self.screen)

    def start(self):
        while self.running:
            self.menu.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((180,220,255))
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
