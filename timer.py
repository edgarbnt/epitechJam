#!/bin/python3

import pygame


class Timer:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render("00:00", True, (255, 255, 255))
        self.score_text = self.font.render("Score", True, (255, 255, 255))
        self.highscore_text = self.font.render("Best", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.rectangle_rect = self.text_rect.inflate(20, 20)
        self.rectangle_rect.topleft = (10, 35)
        self.text_rect.center = self.rectangle_rect.center

        value_minutes = 0
        value_sec = 0
        try:
            with open("./assets/best.txt", "a+") as file:
                file.seek(0)
                value = file.read()
                value_current_tick = int(value)
                value_minutes = value_current_tick // 60000
                value_sec = value_current_tick % 60000
                value_sec //= 1000
        except:
            pass
        self.text_surface_highscore = self.font.render(("%02d:%02d" % (value_minutes, value_sec)), True, (255, 255, 255))
        self.text_rect_highscore = self.text_surface_highscore.get_rect()
        self.rectangle_rect_highscore = self.text_rect_highscore.inflate(20, 20)
        self.rectangle_rect_highscore.topleft = (10, 110)
        self.text_rect_highscore.center = self.rectangle_rect_highscore.center

    def update(self, current_tick, starting_tick):
        minutes = (current_tick - starting_tick) // 60000
        sec = (current_tick - starting_tick) % 60000
        sec //= 1000

        self.text_surface = self.font.render(("%02d:%02d" % (minutes, sec)), True, (255, 255, 255))

    def render(self, game_display):
        pygame.draw.rect(game_display, (0, 0, 0), self.rectangle_rect)
        game_display.blit(self.text_surface, self.text_rect)
        self.text_rect.y -= 37
        game_display.blit(self.score_text, self.text_rect)
        self.text_rect.y += 37
        self.text_rect.y += 37
        self.text_rect.x += 5
        game_display.blit(self.highscore_text, self.text_rect)
        self.text_rect.x -= 5
        self.text_rect.y -= 37

        pygame.draw.rect(game_display, (0, 0, 0), self.rectangle_rect_highscore)
        game_display.blit(self.text_surface_highscore, self.text_rect_highscore)

