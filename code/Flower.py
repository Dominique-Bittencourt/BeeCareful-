#!/usr/bin/python

# -*- coding: utf-8 -*-

import pygame


class Flower:
    def __init__(self, screen, image_path, x, y):
        self.screen = screen

        self.image = pygame.image.load(
            image_path
        ).convert_alpha()

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.world_x = self.rect.x

    def draw(self):
        self.screen.blit(
            self.image,
            self.rect
        )

    def get_pollen_position(self):
        return (
            self.rect.centerx,
            self.rect.top
        )

    def update_position(self, offset_x):
        self.rect.x = self.world_x + offset_x
