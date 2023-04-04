import pygame, sys
import threading as th
import time
from scene import Scene

import sys
from game_state import GameState

import scene_home
import timer_class

BOARD_SIZE = 5
CELL_SIZE = 100
PIECE_SIZE = 45
WIDTH = BOARD_SIZE * CELL_SIZE
HEIGHT = BOARD_SIZE * CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SceneHuman(Scene):
    """ Welcome screen of the game, the first one to be loaded."""
 
    def __init__(self, director):
        self.clock = pygame.time.Clock()
        self.counter, self.text = 0, '0'.rjust(3)
        self.time = 'Time: '

        self.tmr = timer_class.TimerClass()
        self.tmr.start()

        self.dir = director

        self.board = [[0, 0, 0, 1, 2], 
                      [0, 0, 0, 2, 0], 
                      [3, 3, 3, 0, 3],
                      [0, 1, 1, 0, 3],
                      [0, 0, 2, 0, 0]]

        self.done = False

        self.piece = 0

        # Set up the font
        self.font = pygame.font.SysFont('Arial', 34)
        self.title_font = pygame.font.SysFont('Arial', 70)

        # Define the vertices of the figure
        self.bg_vertices = [(0, 0), (0, 700), (1000, 700), (1000, 0)]

        # Define the color of the figure
        self.bg = (130, 50, 180) # purple
        self.gold = (235, 183, 12) # buttons
        self.white = (255, 255, 255) # white
        self.red = (255, 0, 0) # red

        # Define the texts
        self.human_text = self.font.render('Human', True, self.white)
        self.won_text = self.font.render('You won!', True, self.white)

        # Get the dimensions of the text
        self.human_text_rect = self.human_text.get_rect()
        self.won_text_rect = self.won_text.get_rect()

        self.human_text_rect = (53, 40)
        self.won_text_rect = (30, 140)

        # Define back button
        self.backButton = pygame.image.load("Images/backward.png")

        # Get dimensions of button
        self.backButton_rect = self.backButton.get_rect()
        self.backButton_rect = (900, 590)
 
    def select_piece(self, key):
        if key == 1:
            self.piece = 1
        elif key == 2:
            self.piece = 2
        elif key == 3:
            self.piece = 3
        elif key == 0:
            self.piece = 0
        else:
            return False
        print(str(key))
        return True

    def on_update(self):
        pass


    def cancel_thread(self):
        self.tmr.stop()
        return True

    def draw_board(self, screen):
        pygame.draw.rect(screen, WHITE, pygame.Rect(270, 100, CELL_SIZE*5, CELL_SIZE*5))
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                x = j * CELL_SIZE + 270
                y = i * CELL_SIZE + 100
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, GRAY, rect, 2)
                elif self.board[i][j] == 1:
                    pygame.draw.polygon(screen, BLUE, ((270+10+CELL_SIZE*j,100+20+CELL_SIZE*i),(270+90+CELL_SIZE*j,100+20+CELL_SIZE*i),(270+50+CELL_SIZE*j,100+80+CELL_SIZE*i)))
                    pygame.draw.rect(screen, GRAY, rect, 2)
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, GREEN, rect, PIECE_SIZE + 5)
                    pygame.draw.rect(screen, GRAY, rect, 2)
                    
                else:
                    pygame.draw.circle(screen, RED, (j * CELL_SIZE + CELL_SIZE + 440// 2, i * CELL_SIZE + CELL_SIZE + 100// 2), PIECE_SIZE)
                    pygame.draw.rect(screen, GRAY, rect, 2)


    def place_piece(self, row, col):
        self.board[row][col] = self.piece
        return True

    def dj_piece(self):
        # Draw the menu
        menu_font = pygame.font.SysFont(None, 30)
        colors = [BLACK, BLACK, BLACK, BLACK]
        for i in range(4):
            colors[i] = BLACK
            if i == self.piece:
                colors[i] = RED
        text1 = menu_font.render("Choose a piece:", True, BLACK)
        text2 = menu_font.render("1 - Triangle", True, colors[1])
        text3 = menu_font.render("2 - Rectangle", True, colors[2])
        text4 = menu_font.render("3 - Circle", True, colors[3])
        text5 = menu_font.render("0 - Erase", True, colors[0])
        menu_width = max(text1.get_width(), text2.get_width(), text3.get_width(), text4.get_width()) +10
        menu_height = text1.get_height() * 5 + 15
        menu_surf = pygame.Surface((menu_width, menu_height))
        menu_surf.fill(WHITE)
        menu_rect = menu_surf.get_rect()
        menu_rect.center = (WIDTH + 385, HEIGHT-300)
        menu_surf.blit(text1, (menu_width // 2 - text1.get_width() // 2, 10))
        menu_surf.blit(text2, (menu_width // 2 - text2.get_width() // 2, text1.get_height() + 10))
        menu_surf.blit(text3, (menu_width // 2 - text3.get_width() // 2, text1.get_height() * 2 + 10))
        menu_surf.blit(text4, (menu_width // 2 - text4.get_width() // 2, text1.get_height() * 3 + 10))
        menu_surf.blit(text5, (menu_width // 2 - text5.get_width() // 2, text1.get_height() * 4 + 10))
        self.screen.blit(menu_surf, menu_rect)


    def on_event(self, event):
        if event.type == pygame.KEYDOWN and not self.done:
            if event.key == pygame.K_1:
                self.select_piece(1)
            if event.key == pygame.K_2:
                self.select_piece(2)
            if event.key == pygame.K_3:
                self.select_piece(3)
            if event.key == pygame.K_0:
                self.select_piece(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x >= 270 and x < 770 and y >= 100 and y < 600:
                x = x - 270
                y = y - 100
                i = (y // CELL_SIZE)
                j = (x // CELL_SIZE)
                if i < BOARD_SIZE and j < BOARD_SIZE and (self.board[i][j] == 0 or self.piece == 0):
                    self.board[i][j] = self.piece
            if pygame.Rect(900, 590, 64, 64).collidepoint(event.pos):
                self.cancel_thread()
                return scene_home.SceneHome(self.dir)
        self.game = GameState(self.board)
        if self.game.is_palindrome() and self.done == False:
            self.cancel_thread()
            self.done = True
        return self
 
    def on_draw(self, screen):
        self.screen = screen
        # Draw background
        pygame.draw.polygon(screen, self.gold, self.bg_vertices)

        pygame.draw.rect(screen, self.bg, pygame.Rect(10, 20, 200, 600))

        pygame.draw.rect(screen, self.gold, pygame.Rect(32, 32, 150, 50), 25, 20)
        pygame.draw.rect(screen, self.gold, pygame.Rect(560, 400, 140, 70), 200, 20)

        screen.blit(self.human_text, self.human_text_rect)
        screen.blit(self.backButton, self.backButton_rect)
        if self.done:
            screen.blit(self.won_text, self.won_text_rect)
        screen.blit(self.font.render(str(self.tmr.get_count()), True, (0, 0, 0)), (120, 100))
        screen.blit(self.font.render(self.time, True, (0, 0, 0)), (30, 100))

        self.draw_board(screen)
        self.dj_piece()