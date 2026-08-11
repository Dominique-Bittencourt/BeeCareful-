#!/usr/bin/python

# -*- coding: utf-8 -*-

from code.Pollen import Pollen


class PollenFactory:

    @staticmethod
    def create_from_flower(screen, flower):
        x, y = flower.get_pollen_position()

        return Pollen(
            screen,
            x,
            y,
            flower
        )
