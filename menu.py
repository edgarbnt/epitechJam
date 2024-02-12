import json

import pygame

players = json.load(open("assets/players.json"))


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.players = players
        self.current_player = 0
        self.start_button = pygame.image.load("assets/start_button.png")
        self.left_arrow = pygame.image.load("assets/arrow_button.png")
        self.right_arrow = pygame.image.load("assets/arrow_button.png")
        self.selection_rect = pygame.Rect(175, 100, 50, 50)
        self.game_over = pygame.image.load("assets/game_over.png")
        self.victory = pygame.image.load("assets/victory.png")
        self.replay = pygame.image.load("assets/replay.png")

        for player in self.players:
            player["sprite"] = pygame.image.load(player["texture"])
            player["sprite"] = pygame.transform.scale(player["sprite"], (920 / 2, 623 / 2))


        self.start_button = pygame.transform.scale(self.start_button, (466 / 2, 151 / 2))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.topleft = (400 - 466 / 4, 400)

        self.left_arrow = pygame.transform.scale(self.left_arrow, (542 / 6, 461 / 6))
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.left_arrow = pygame.transform.rotate(self.left_arrow, 180)
        self.left_arrow_rect.topleft = (640 - 542 / 4, 250)

        self.right_arrow = pygame.transform.scale(self.right_arrow, (542 / 6, 461 / 6))
        self.right_arrow_rect = self.right_arrow.get_rect()
        self.right_arrow_rect.topleft = (200, 250)

        self.game_over = pygame.transform.scale(self.game_over, (348, 236))

        self.victory = pygame.transform.scale(self.victory, (1500 / 6, 577 / 6))

        self.replay = pygame.transform.scale(self.replay, (1264 / 3, 254 / 3))
        self.replay_rect = self.replay.get_rect()
        self.replay_rect.topleft = (400 - ((1264 / 3) / 2), 450 - ((254 / 3) / 2))

    def update_menu(self):
        pass

    def render_menu(self, screen, start_button_clicked):
        screen.blit(self.start_button, (400 - 466 / 4, 400))
        screen.blit(self.left_arrow, (200, 250))
        screen.blit(self.right_arrow, (640 - 542 / 4, 250))

        player_image = self.players[self.current_player]["sprite"]

        if start_button_clicked == 1:
            player_rect = pygame.Rect(180, 0, 280, 300)
            cropped_player_image = player_image.subsurface(player_rect)
            screen.blit(cropped_player_image, (230, 100))
        else:
            player_rect = pygame.Rect(0, 0, 280, 300)
            cropped_player_image = player_image.subsurface(player_rect)
            screen.blit(cropped_player_image, (285, 100))


