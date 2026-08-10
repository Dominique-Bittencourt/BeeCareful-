#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.state = None

        # Fundo
        self.surf = pygame.image.load('./asset/sky.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        # Fonte
        self.font_title = pygame.font.Font(None, 48)
        self.font_subtitle = pygame.font.Font(None, 22)
        self.font_button = pygame.font.Font(None, 32)
        self.font_commands = pygame.font.Font(None, 20)

        # Cores
        self.white = (255, 255, 255)
        self.dark = (40, 60, 70)

        # Botão
        self.button_rect = pygame.Rect(250, 180, 100, 45)

    def draw(self, ):
        # Fundo
        self.screen.blit(self.surf, self.rect)

        # Título
        title = self.font_title.render(
            "BEECAREFUL!",
            True,
            self.dark
        )

        title_rect = title.get_rect(center=(300, 65))
        self.screen.blit(title, title_rect)

        # Subtítulos
        subtitle1 = self.font_subtitle.render(
            "Ajude a abelhinha a coletar pólen",
            True,
            self.dark
        )

        subtitle2 = self.font_subtitle.render(
            "e salvar a colmeia!",
            True,
            self.dark
        )

        subtitle1_rect = subtitle1.get_rect(center=(300, 105))
        subtitle2_rect = subtitle2.get_rect(center=(300, 125))

        self.screen.blit(subtitle1, subtitle1_rect)
        self.screen.blit(subtitle2, subtitle2_rect)

        # Botão JOGAR
        pygame.draw.rect(
            self.screen,
            self.white,
            self.button_rect,
            border_radius=8
        )

        button_text = self.font_button.render(
            "JOGAR",
            True,
            self.dark
        )

        button_text_rect = button_text.get_rect(
            center=self.button_rect.center
        )

        self.screen.blit(button_text, button_text_rect)

        # Comandos
        commands_title = self.font_commands.render(
            "── COMANDOS ──",
            True,
            self.dark
        )

        commands_title_rect = commands_title.get_rect(
            center=(300, 275)
        )

        self.screen.blit(commands_title, commands_title_rect)

        commands_move = self.font_commands.render(
            "W A S D / SETAS  -  Mover",
            True,
            self.dark
        )

        commands_pause = self.font_commands.render(
            "ESC  -  Pausar",
            True,
            self.dark
        )

        move_rect = commands_move.get_rect(
            center=(300, 305)
        )

        pause_rect = commands_pause.get_rect(
            center=(300, 325)
        )

        self.screen.blit(commands_move, move_rect)
        self.screen.blit(commands_pause, pause_rect)

    def startGame(self, ):
        pass

    def exitGame(self, ):
        pass

    def changeState(self, ):
        pass
