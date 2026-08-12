#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MENU_MUSIC,
    GAME_MUSIC,
    MAX_LIVES,
)

from code.Menu import Menu
from code.GameState import GameState
from code.Background import Background
from code.Flower import Flower
from code.Bee import Bee
from code.Pollen import Pollen
from code.PollenFactory import PollenFactory
from code.Cloud import Cloud
from code.RaindropFactory import RaindropFactory

class Game:
    def __init__(self):
        pygame.init()

        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("BeeCareful!")

        self.clock = pygame.time.Clock()

        self.running = True
        self.score = None
        self.timer = None

        self.menu = Menu(self.screen)
        self.background = Background(self.screen)

        # Life HUD
        self.heart = pygame.image.load(
            './asset/heart.png'
        ).convert_alpha()

        self.clouds = [
            Cloud(
                self.screen,
                './asset/cloud1.png',
                50,
                75,
                18
            ),
            Cloud(
                self.screen,
                './asset/cloud2.png',
                210,
                105,
                19
            ),
            Cloud(
                self.screen,
                './asset/cloud1.png',
                380,
                70,
                18
            ),
            Cloud(
                self.screen,
                './asset/cloud2.png',
                550,
                115,
                19
            )
        ]

        self.raindrops = []

        self.rain_cooldowns = [
            1.6,
            2.5,
            2.0,
            3.0
        ]

        self.flowers = [
            Flower(
                self.screen,
                './asset/pansy.png',
                55,
                310
            ),
            Flower(
                self.screen,
                './asset/tulip.png',
                180,
                310
            ),
            Flower(
                self.screen,
                './asset/sunflower.png',
                300,
                310
            ),
            Flower(
                self.screen,
                './asset/lily.png',
                425,
                310
            ),
            Flower(
                self.screen,
                './asset/rose.png',
                550,
                310
            )
        ]

        self.bee = Bee(self.screen)

        self.pollens = []
        self.pollen_cooldowns = {}

        for flower in self.flowers:
            self.pollens.append(
                PollenFactory.create_from_flower(
                    self.screen,
                    flower
                )
            )

            self.pollen_cooldowns[flower] = 0

        # Game over font
        self.game_over_font = pygame.font.Font(
            './asset/fonts/PixelifySans-VariableFont_wght.ttf',
            42
        )

        self.game_over_text_font = pygame.font.Font(
            './asset/fonts/VT323-Regular.ttf',
            24
        )

        self.game_over_color = (255, 220, 90)
        self.game_over_shadow = (92, 58, 35)
        self.game_over_text_color = (255, 248, 220)

    def start(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            self.events()
            self.update(dt)
            self.draw()

        pygame.quit()

    def change_music(self):
        pygame.mixer.music.load(GAME_MUSIC)
        pygame.mixer.music.play(-1)

    def update(self, dt):
        if self.menu.state == GameState.PLAYING:

            self.bee.move()
            self.bee.update(dt)
            self.background.update(dt)

            # Update flowers with the ground
            for flower in self.flowers:
                flower.update_position(
                    self.background.ground_x
                )

            # Loop flowers
            for flower in self.flowers:

                if flower.rect.right < 0:
                    last_flower = max(
                        self.flowers,
                        key=lambda item: item.world_x
                    )

                    flower.world_x = (
                            last_flower.world_x + 125
                    )

                    flower.update_position(
                        self.background.ground_x
                    )

            # Update clouds
            for cloud in self.clouds:
                cloud.update(dt)

            # Generate rain
            for i, cloud in enumerate(self.clouds):

                self.rain_cooldowns[i] -= dt

                if self.rain_cooldowns[i] <= 0:
                    self.raindrops.append(
                        RaindropFactory.create_from_cloud(
                            self.screen,
                            cloud
                        )
                    )

                    self.rain_cooldowns[i] = 2.5

            # Update raindrops
            for raindrop in self.raindrops:
                if raindrop.active:
                    raindrop.update(dt)

                    if self.bee.collide(raindrop):
                        raindrop.active= False
                        self.bee.take_damage()



            # Remove inactive raindrops
            self.raindrops = [
                raindrop
                for raindrop in self.raindrops
                if raindrop.active
            ]

            # Update pollen
            for pollen in self.pollens:
                if not pollen.is_collected():
                    pollen.update(dt)

                    if self.bee.collide(pollen):
                        pollen.collect()
                        self.pollen_cooldowns[pollen.flower] = 2.0

                    elif pollen.rect.bottom < 0:
                        pollen.collect()
                        self.pollen_cooldowns[pollen.flower] = 2.0

            # Remove collected or expired pollen
            self.pollens = [
                pollen
                for pollen in self.pollens
                if not pollen.is_collected()
            ]

            # Regenerate pollen
            for flower in self.flowers:

                if not any(
                        pollen.flower == flower
                        for pollen in self.pollens
                ):
                    self.pollen_cooldowns[flower] -= dt

                    if self.pollen_cooldowns[flower] <= 0:
                        self.pollens.append(
                            PollenFactory.create_from_flower(
                                self.screen,
                                flower
                            )
                        )

            self.checkGameOver()

    def draw_lives(self):
        for i in range(self.bee.lives):
            heart_rect = self.heart.get_rect(
                topleft=(20 + i * 30, 15)
            )

            self.screen.blit(
                self.heart,
                heart_rect
            )

    def draw_game_over(self):
        # Background
        self.background.draw()

        # Dark overlay
        overlay = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 100))

        self.screen.blit(
            overlay,
            (0, 0)
        )

        # Title shadow
        title_shadow = self.game_over_font.render(
            "GAME OVER",
            True,
            self.game_over_shadow
        )

        title = self.game_over_font.render(
            "GAME OVER",
            True,
            self.game_over_color
        )

        title_rect = title.get_rect(
            center=(300, 155)
        )

        self.screen.blit(
            title_shadow,
            (
                title_rect.x + 3,
                title_rect.y + 3
            )
        )

        self.screen.blit(
            title,
            title_rect
        )

        # Message
        message = self.game_over_text_font.render(
            "Que pena! A chuva foi demais...",
            True,
            self.game_over_text_color
        )

        message_rect = message.get_rect(
            center=(300, 215)
        )

        self.screen.blit(
            message,
            message_rect
        )

        message2 = self.game_over_text_font.render(
            "Tome cuidado da próxima vez!",
            True,
            self.game_over_text_color
        )

        message2_rect = message2.get_rect(
            center=(300, 240)
        )

        self.screen.blit(
            message2,
            message2_rect
        )

        # Restart instruction
        restart = self.game_over_text_font.render(
            "ENTER - Jogar novamente",
            True,
            self.game_over_text_color
        )

        restart_rect = restart.get_rect(
            center=(300, 285)
        )

        self.screen.blit(
            restart,
            restart_rect
        )

        # Menu instruction
        menu = self.game_over_text_font.render(
            "ESC - Voltar ao menu",
            True,
            self.game_over_text_color
        )

        menu_rect = menu.get_rect(
            center=(300, 320)
        )

        self.screen.blit(
            menu,
            menu_rect
        )

    def draw(self):
        if self.menu.state == GameState.MENU:
            self.menu.draw()

        elif self.menu.state == GameState.PLAYING:
            self.background.draw()

            for cloud in self.clouds:
                cloud.draw()

            for raindrop in self.raindrops:
                raindrop.draw()

            for flower in self.flowers:
                flower.draw()

            for pollen in self.pollens:
                pollen.draw()

            self.bee.draw()
            self.draw_lives()

        elif self.menu.state == GameState.GAME_OVER:
            self.draw_game_over()

        pygame.display.flip()


    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif self.menu.state == GameState.MENU:
                if self.menu.startGame(event):
                    self.change_music()

            elif self.menu.state == GameState.GAME_OVER:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.restart_game()

                    elif event.key == pygame.K_ESCAPE:
                        self.menu.state = GameState.MENU

    def checkVictory(self, ):
        pass

    def checkGameOver(self):
        if self.bee.lives <= 0:
            self.menu.state = GameState.GAME_OVER

    def restart_game(self):
        self.bee.lives = MAX_LIVES
        self.bee.x = 300
        self.bee.y = 280
        self.bee.rect.center = (
            self.bee.x,
            self.bee.y
        )

        self.bee.invulnerability_time = 0

        self.raindrops.clear()

        self.pollens.clear()
        for flower in self.flowers:
            self.pollens.append(
                PollenFactory.create_from_flower(
                    self.screen,
                    flower
                )
            )

            self.pollen_cooldowns[flower] = 0

        self.background.ground_x = 0
        self.background.mountain_x = 0

        self.menu.state = GameState.PLAYING

        pygame.mixer.music.load(GAME_MUSIC)
        pygame.mixer.music.play(-1)

