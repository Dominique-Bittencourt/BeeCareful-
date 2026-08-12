#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import (
SCREEN_WIDTH,
GROUND_Y,
BEE_MIN_Y,
MAX_LIVES
)

class Bee:
    def __init__(self, screen):
        self.screen = screen

        #Bee position
        self.x = 300
        self.y = 280

        #Bee movement speed
        self.speed = 3

        # Health
        self.lives = MAX_LIVES
        self.invulnerability_time = 0

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

        # Keep the bee inside the horizontal playable area
        self.x = max(
            self.rect.width // 2,
            min(
                self.x,
                SCREEN_WIDTH - self.rect.width // 2
            )
        )

        # Keep the bee inside the vertical playable area
        self.y = max(
            BEE_MIN_Y + self.rect.height // 2,
            min(
                self.y,
                GROUND_Y - self.rect.height // 2
            )
        )

        # Update the collision rectangle
        self.rect.center = (
            self.x,
            self.y
        )

    def draw(self):
        # Blink while invulnerable
        if self.invulnerability_time > 0:
            blink = pygame.time.get_ticks() // 100

            if blink % 2 == 0:
                return

        self.screen.blit(
            self.image,
            self.rect
        )

    def collide(self, other):
        return self.rect.colliderect(other.rect)

    def update(self, dt):
        if self.invulnerability_time > 0:
            self.invulnerability_time -= dt

    def take_damage(self):
        if self.invulnerability_time > 0:
            return False

        self.lives -= 1
        self.invulnerability_time = 1.0

        return True