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

        # Background clouds
        self.clouds = pygame.image.load(
            './asset/backgroundcloud.png'
        ).convert_alpha()

        self.clouds.set_alpha(150)

        self.clouds_rect = self.clouds.get_rect(
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

        self.ground_y = self.ground_rect.top

        # Parallax
        self.mountain_x = 0
        self.ground_x = 0

        self.mountain_speed = 8
        self.ground_speed = 25

    def draw(self):
        # Draw sky
        self.screen.blit(
            self.sky,
            self.sky_rect
        )

        # Draw background clouds
        self.screen.blit(
            self.clouds,
            self.clouds_rect
        )

        # Draw mountains
        mountain_x = (
                             self.mountain_x
                             % self.mountains.get_width()
                     ) - self.mountains.get_width()

        self.screen.blit(
            self.mountains,
            (mountain_x, self.mountains_rect.y)
        )

        self.screen.blit(
            self.mountains,
            (
                mountain_x + self.mountains.get_width(),
                self.mountains_rect.y
            )
        )

        # Draw ground
        ground_x = (
                           self.ground_x
                           % self.ground.get_width()
                   ) - self.ground.get_width()

        self.screen.blit(
            self.ground,
            (ground_x, self.ground_rect.y)
        )

        self.screen.blit(
            self.ground,
            (
                ground_x + self.ground.get_width(),
                self.ground_rect.y
            )
        )

    def update(self, dt):
        # Move mountains slowly
        self.mountain_x -= self.mountain_speed * dt

        # Move ground faster
        self.ground_x -= self.ground_speed * dt

