#!/bin/python3

import pygame


class ColorMap:
    def __init__(self):
        self.map_x = 0
        self.zoom_scale = 0
        self.image = pygame.image.load('assets/color_map.png')
        self.image_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.image_rect.width * 2.5),
                                                         int(self.image_rect.height * 2.5)))

    def update(self, x_to_move, player):
        if player.y >= 10:
            # collision between player and objects on its right (width -> 100, height -> 100)
            if x_to_move < 0 and (self.image.get_at((-self.map_x + player.x + 40 + player.speed, player.y + 99))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x + 40 + player.speed, player.y))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x + 40 + player.speed, player.y + 33))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x + 40 + player.speed, player.y + 66))[1] > 100):
                return
            # collision between player and objects on its left (width -> 100, height -> 100)
            if x_to_move > 0 and (self.image.get_at((-self.map_x + player.x - player.speed, player.y + 99))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x - player.speed, player.y))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x - player.speed, player.y + 33))[1] > 100 or \
                    self.image.get_at((-self.map_x + player.x - player.speed, player.y + 66))[1] > 100):
                return
        if x_to_move == 0:
            return
        self.map_x += x_to_move
