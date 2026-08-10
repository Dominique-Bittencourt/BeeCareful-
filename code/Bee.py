#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT

class Bee:
    def __init__(self, screen):
        self.screen = screen

        #Bee position
        self.x = 300
        self.y = 280

        #Bee movement speed
        self.speed = 3

        #Bee image
        self.image = pygame.image.load(
            './asset/bee.png'
        ).convert_alpha()

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
        )

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed

        # Keep the bee inside the playable area
        self.x = max(
            self.rect.width // 2,
            min(
                self.x,
                SCREEN_WIDTH - self.rect.width // 2
            )
        )

        self.y = max(
            self.rect.height // 2,
            min(
                self.y,
                320 - self.rect.height // 2
            )
        )

    def draw(self):
        self.rect.center = (self.x, self.y)

        self.screen.blit(
            self.image,
            self.rect
        )

    def collide(self, other):
        return self.rect.colliderect(other.rect)