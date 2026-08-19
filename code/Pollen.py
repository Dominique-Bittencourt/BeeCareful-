import math

import pygame

class Pollen:
    def __init__(self, screen, x, y, flower):
        self.screen = screen

        # Pollen origin
        self.flower = flower

        # Pollen position
        self.x = x
        self.y = y

        # Pollen movement
        self.speed = 15
        self.time = 0

        # Pollen image
        self.image = pygame.image.load(
            './asset/pollen.png'
        ).convert_alpha()

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
        )

        self.collected = False

    def update(self, dt):
        self.time += dt

        # Move upward
        self.y -= self.speed * dt

        # Horizontal floating movement
        offset_x = math.sin(self.time * 4) * 8

        # Follow the flower
        self.rect.center = (
            self.flower.rect.centerx + offset_x,
            self.y
        )

    def draw(self):
        if not self.collected:
            self.screen.blit(
                self.image,
                self.rect
            )

    def collect(self):
        self.collected = True

    def is_collected(self):
        return self.collected