import pygame
from console2048 import *
from colors import *


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.index = 0

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(204, 192, 179), (
                    x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3,
                    self.cell_size - 3,
                    self.cell_size - 3))
                pygame.draw.rect(screen, pygame.Color(187, 173, 160), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 3)
        pygame.draw.rect(screen, pygame.Color(187, 173, 160),
                         (self.left - 3, self.top - 3, 4 * self.cell_size, 4 * self.cell_size), 3)
        pygame.draw.rect(screen, pygame.Color(187, 173, 160), (10, 10, 150, 90))
        pygame.draw.rect(screen, pygame.Color(187, 173, 160), (340, 10, 150, 90))
        font = pygame.font.Font('ClearSans-Bold.ttf', 40)
        text1 = font.render("Счёт:", True, (0, 0, 0))
        screen.blit(text1, (10, 0))
        text2 = font.render("Рекорд:", True, (0, 0, 0))
        screen.blit(text2, (340, 0))
        score = open("score.txt", "r").readline()
        text3 = font.render(str(score), True, (0, 0, 0))
        screen.blit(text3, (10, 50))
        best_score = open("best_score.txt", "r").readline()
        text4 = font.render(str(best_score), True, (0, 0, 0))
        screen.blit(text4, (340, 50))

        default_image = pygame.image.load('default.png')
        screen.blit(default_image, (50, 625))
        winter_image = pygame.image.load('winter.png')
        screen.blit(winter_image, (200, 625))
        night_image = pygame.image.load('night.png')
        screen.blit(night_image, (350, 625))
        fire_image = pygame.image.load('fire.png')
        screen.blit(fire_image, (125, 750))
        radioactive_image = pygame.image.load('radioactive.png')
        screen.blit(radioactive_image, (275, 750))

        for i in range(3):
            pygame.draw.rect(screen, pygame.Color(187, 173, 160), (50 + i * 150, 625, 100, 100), 5)
        for i in range(2):
            pygame.draw.rect(screen, pygame.Color(187, 173, 160), (125 + i * 150, 750, 100, 100), 5)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def draw(self, screen):
        for j in range(self.height):
            for i in range(self.width):
                num = mp[i][j]
                if num != 0:
                    if num > 2048:
                        num = 0
                    font_ij = pygame.font.Font("ClearSans-Bold.ttf", 50)
                    text = font_ij.render(str(num), True, (0, 0, 0))
                    text_x = self.cell_size * i + self.left
                    text_y = self.cell_size * j + self.top
                    text_w = text.get_width()
                    pygame.draw.rect(screen, pygame.Color(themes[self.index][num]),
                                     (text_x + 3, text_y + 3, self.cell_size - 6,
                                      self.cell_size - 6))
                    screen.blit(text, (text_x + 50 + len(str(num)) * 15 - text_w, text_y + 15))
