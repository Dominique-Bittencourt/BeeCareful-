import pygame


class Cloud:
    def __init__(self, screen, image_path, x, y, speed):
        self.screen = screen

        # Cloud image
        self.image = pygame.image.load(
            image_path
        ).convert_alpha()

        # Cloud position
        self.x = x
        self.y = y

        # Cloud movement speed
        self.speed = speed

        self.rect = self.image.get_rect(
            center=(self.x, self.y)
        )

    def update(self, dt):
        self.x += self.speed * dt

        if self.x - self.rect.width / 2 > 600:
            self.x = -self.rect.width / 2

        self.rect.center = (
            self.x,
            self.y
        )

    def draw(self):
        self.rect.center = (
            self.x,
            self.y
        )

        self.screen.blit(
            self.image,
            self.rect
        )

    def get_rain_position(self):
        return (
            self.rect.centerx,
            self.rect.bottom
        )