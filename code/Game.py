#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MENU_MUSIC,
    GAME_MUSIC
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

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif self.menu.state == GameState.MENU:
                if self.menu.startGame(event):
                    self.change_music()

    def checkVictory(self, ):
        pass

    def checkGameOver(self, ):
        pass
