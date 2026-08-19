import random

import pygame

from code.Const import SCREEN_WIDTH, GROUND_Y


class GameOverRain:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load(
            './asset/raindropgameover.png'
        ).convert_alpha()

        self.drops = []

        # Create decorative raindrops
        for _ in range(15):
            self.drops.append({
                "x": random.randint(
                    15,
                    SCREEN_WIDTH - 15
                ),
                "y": random.randint(
                    -300,
                    GROUND_Y
                ),
                "speed": random.randint(
                    70,
                    110
                )
            })

    def update(self, dt):
        for drop in self.drops:
            drop["y"] += drop["speed"] * dt

            # Restart the raindrop from the top
            if drop["y"] >= GROUND_Y:
                drop["y"] = random.randint(-100, -10)
                drop["x"] = random.randint(
                    15,
                    SCREEN_WIDTH - 15
                )
                drop["speed"] = random.randint(
                    70,
                    110
                )

    def draw(self):
        for drop in self.drops:
            rect = self.image.get_rect(
                center=(
                    drop["x"],
                    drop["y"]
                )
            )

            self.screen.blit(
                self.image,
                rect
            )