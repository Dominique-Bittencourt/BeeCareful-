#!/usr/bin/python

# -*- coding: utf-8 -*-

import pygame

from code.Const import GROUND_Y


class Raindrop:
    def __init__(self, screen, x, y, cloud):
        self.screen = screen

        # Raindrop origin
        self.cloud = cloud

        # Raindrop position
        self.x = x
        self.y = y

        # Raindrop movement
        self.speed = 95

        # Raindrop image
        self.image = pygame.image.load(
            './asset/raindrop.png'
        ).convert_alpha()

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
        )

        self.active = True

    def update(self, dt):
        # Move downward
        self.y += self.speed * dt

        self.rect.center = (
            self.x,
            self.y
        )

        # Remove the raindrop when it reaches the ground
        if self.rect.bottom >= GROUND_Y:
            self.active = False

    def draw(self):
        if self.active:
            self.screen.blit(
                self.image,
                self.rect
            )