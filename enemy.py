import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, map, x, y, width, height, is_optional, texture, health):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.is_alive = True
        self.is_optional = is_optional
        self.texture = pygame.image.load(texture)
        self.texture_on_death = pygame.image.load("assets/register.png")
        self.texture_on_death = pygame.transform.scale2x(self.texture_on_death)
        self.death_tick = 0

        self.map = map
        self.enemy_clock = pygame.time.Clock()
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_interval = 500
        self.texture = pygame.transform.scale(self.texture, (width, height))
        self.enemy_rect = self.texture.get_rect()
        self.enemy_rect.topleft = (self.x, self.y)

    def update_enemy(self, player):
        if ((self.x + self.map.map_x <= player.x + 40 <= self.x + self.map.map_x + self.width or self.x + self.map.map_x <= player.x <= self.x + self.map.map_x + self.width) and
                (self.y >= player.y >= self.y - self.height and self.is_alive)):
            player.damage_player(100)

    def draw_health_bar(self, screen):
        bar_width = self.width
        bar_height = 5
        health_percentage = max(0, self.health / self.max_health)
        bar_color = (0, 255, 0)

        bar_x = self.x + self.map.map_x
        bar_y = self.y - 10

        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width * health_percentage, bar_height))

    def render_enemy(self, screen):
        if self.is_alive:
            self.draw_health_bar(screen)
            screen.blit(self.texture, (self.x + self.map.map_x, self.y))
        elif self.death_tick < 120:
            screen.blit(self.texture_on_death, (self.x + self.map.map_x, self.y + 50))
            self.death_tick += 1

    def damage_enemy(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
