import math

import pygame

from code.GameState import GameState

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.state = GameState.MENU

        # Background
        self.surf = pygame.image.load('./asset/sky.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        # Background clouds
        self.clouds = pygame.image.load(
            './asset/backgroundcloud.png'
        ).convert_alpha()

        self.clouds.set_alpha(150)

        self.clouds_rect = self.clouds.get_rect(
            left=0,
            top=25
        )

        # Cloud movement
        self.cloud_x = 0
        self.cloud_speed = 10

        # Bee
        self.bee = pygame.image.load(
            './asset/bee.png'
        ).convert_alpha()

        self.bee_base_y = 225

        self.bee_rect = self.bee.get_rect(
            center=(475, self.bee_base_y)
        )

        # Decorative pollen
        self.pollen = pygame.image.load(
            './asset/pollen.png'
        ).convert_alpha()

        self.pollen_positions = [
            (90, 210),
            (160, 180),
            (430, 190),
            (540, 250),
            (120, 285)
        ]

        # Mouse pollen
        self.mouse_pollen = []
        self.last_mouse_position = pygame.mouse.get_pos()
        self.last_pollen_time = 0

        # Fonts
        self.font_title = pygame.font.Font(
            './asset/fonts/PixelifySans-VariableFont_wght.ttf',
            32
        )

        self.font_subtitle = pygame.font.Font(
            './asset/fonts/PixelifySans-VariableFont_wght.ttf',
            20
        )

        self.font_button = pygame.font.Font(
            './asset/fonts/PixelifySans-VariableFont_wght.ttf',
            20
        )

        self.font_commands = pygame.font.Font(
            './asset/fonts/VT323-Regular.ttf',
            22
        )

        # Colors
        self.title_color = (255, 220, 90)  # honey yellow
        self.shadow_color = (92, 58, 35)  # brown
        self.text_color = (255, 248, 220)  # cream
        self.text_shadow = (80, 105, 110)  # blue-gray

        # Button
        self.button_rect = pygame.Rect(230, 180, 140, 48)
        self.button_hover = False
        self.button_pressed = False
        self.button_press_time = 0

    def draw_text_with_shadow(self, text, font, position, color):
        shadow = font.render(
            text,
            True,
            self.text_shadow
        )

        surface = font.render(
            text,
            True,
            color
        )

        rect = surface.get_rect(center=position)

        self.screen.blit(
            shadow,
            (rect.x + 2, rect.y + 2)
        )

        self.screen.blit(
            surface,
            rect
        )

    def draw(self):
        time = pygame.time.get_ticks() / 1000

        # Background
        self.screen.blit(
            self.surf,
            self.rect
        )

        # Clouds in movement
        self.cloud_x = -(time * self.cloud_speed % self.clouds.get_width())

        self.screen.blit(
            self.clouds,
            (self.cloud_x, 0)
        )

        self.screen.blit(
            self.clouds,
            (self.cloud_x + self.clouds.get_width(), 0)
        )

        # Floating pollens
        for i, (x, y) in enumerate(self.pollen_positions):
            pollen_y = y + math.sin(time * 1.5 + i) * 4

            pollen_rect = self.pollen.get_rect(
                center=(x, pollen_y)
            )

            self.screen.blit(
                self.pollen,
                pollen_rect
            )

        # Mouse pollen
        mouse_position = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        if (
                mouse_position != self.last_mouse_position
                and current_time - self.last_pollen_time > 70
        ):
            x, y = mouse_position

            self.mouse_pollen.append({
                "x": x,
                "y": y,
                "speed": 25,
                "life": 1.0
            })

            self.last_mouse_position = mouse_position
            self.last_pollen_time = current_time

        # Update mouse pollen
        for pollen in self.mouse_pollen[:]:

            pollen["y"] += pollen["speed"] / 60
            pollen["life"] -= 0.02

            pollen_rect = self.pollen.get_rect(
                center=(pollen["x"], pollen["y"])
            )

            self.screen.blit(
                self.pollen,
                pollen_rect
            )

            if pollen["life"] <= 0:
                self.mouse_pollen.remove(pollen)

        # Title
        title = self.font_title.render(
            "BEECAREFUL!",
            True,
            self.title_color
        )

        title_rect = title.get_rect(center=(300, 65))

        # Shadow title
        title_shadow = self.font_title.render(
            "BEECAREFUL!",
            True,
            self.shadow_color
        )

        self.screen.blit(
            title_shadow,
            (title_rect.x + 3, title_rect.y + 3)
        )

        self.screen.blit(title, title_rect)

        # Subtitles
        self.draw_text_with_shadow(
            "Ajude a abelhinha a coletar pólen",
            self.font_subtitle,
            (300, 105),
            self.text_color
        )

        self.draw_text_with_shadow(
            "e fugir das gotas de chuva!",
            self.font_subtitle,
            (300, 125),
            self.text_color
        )

        # Button state
        mouse_position = pygame.mouse.get_pos()

        self.button_hover = self.button_rect.collidepoint(
            mouse_position
        )

        # Button JOGAR
        if self.button_pressed:
            button_rect = self.button_rect.move(0, 3)

        elif self.button_hover:
            button_rect = self.button_rect.move(0, -2)

        else:
            button_rect = self.button_rect

        # Shadow
        shadow_rect = button_rect.move(4, 4)

        pygame.draw.rect(
            self.screen,
            self.shadow_color,
            shadow_rect
        )

        # Border
        pygame.draw.rect(
            self.screen,
            self.shadow_color,
            button_rect
        )

        # Yellow interior
        button_inner = button_rect.inflate(-4, -4)

        pygame.draw.rect(
            self.screen,
            self.title_color,
            button_inner
        )

        # Text
        button_text = self.font_button.render(
            "JOGAR",
            True,
            self.shadow_color
        )

        button_text_rect = button_text.get_rect(
            center=button_rect.center
        )

        self.screen.blit(
            button_text,
            button_text_rect
        )

        # Bee movement

        bee_y = self.bee_base_y + math.sin(time * 3) * 7

        self.bee_rect.centery = bee_y

        self.screen.blit(
            self.bee,
            self.bee_rect
        )

        # Commands
        self.draw_text_with_shadow(
            "── COMANDOS ──",
            self.font_commands,
            (300, 275),
            self.text_color
        )

        self.draw_text_with_shadow(
            "W, A, S, D / SETAS  -  Mover",
            self.font_commands,
            (300, 305),
            self.text_color
        )

        self.draw_text_with_shadow(
            "ESC  -  Pausar",
            self.font_commands,
            (300, 325),
            self.text_color
        )

    def startGame(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.button_pressed = True
                self.button_press_time = pygame.time.get_ticks()

        return False

    def update(self):
        if self.button_pressed:

            current_time = pygame.time.get_ticks()

            if current_time - self.button_press_time >= 400:
                self.button_pressed = False
                self.state = GameState.PLAYING
                return True

        return False