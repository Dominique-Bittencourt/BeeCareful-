#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame


class Background:
    def __init__(self, screen):
        self.screen = screen

        # Sky
        self.sky = pygame.image.load(
            './asset/sky.png'
        ).convert()

        self.sky_rect = self.sky.get_rect(
            left=0,
            top=0
        )

        # Mountains
        self.mountains = pygame.image.load(
            './asset/mountain.png'
        ).convert_alpha()

        mountain_width = 600
        mountain_height = int(
            self.mountains.get_height()
            * mountain_width
            / self.mountains.get_width()
        )

        self.mountains = pygame.transform.scale(
            self.mountains,
            (mountain_width, mountain_height)
        )

        self.mountains_rect = self.mountains.get_rect(
            left=0,
            bottom=400
        )

        # Ground
        self.ground = pygame.image.load(
            './asset/ground.png'
        ).convert_alpha()

        self.ground_rect = self.ground.get_rect(
            left=0,
            bottom=400
        )

    def draw(self):
        # Draw sky
        self.screen.blit(
            self.sky,
            self.sky_rect
        )

        # Draw mountains
        self.screen.blit(
            self.mountains,
            self.mountains_rect
        )

        # Draw ground
        self.screen.blit(
            self.ground,
            self.ground_rect
        )