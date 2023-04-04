import pygame, sys
import threading as th
import time
from scene import Scene

import sys
sys.path.append('../')
from game_state import GameState
sys.path.append('../FEUP-IA/interface')

import scene_home
import timer_class
import search_methods

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

        self.dir = director

        #teste
        # to-do move this as parameter of funtion, generalize the class
        # search_methods.test_bfs_easy(0)
      
        self.board = search_methods.solution.move_history[0]
        self.time_ = search_methods.time_

        self.play = False
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
        self.ia_text = self.font.render('IA', True, self.white)
        self.finish_text = self.font.render('Finish!', True, self.white)
        self.time_text = self.font.render('Time: ' + str(round(self.time_, 2)), True, self.white)


        # Get the dimensions of the text
        self.ia_text_rect = self.ia_text.get_rect()
        self.ia_text_rect = (90, 40)

        self.finish_text_rect = self.finish_text.get_rect()
        self.finish_text_rect = (30, 140)

        self.time_text_rect = self.time_text.get_rect()
        self.time_text_rect = (30, 240)


        # Define back button
        self.backButton = pygame.image.load("Images/backward.png")
        self.playButton = pygame.image.load("Images/play_button.png")

        # Get dimensions of button
        self.backButton_rect = self.backButton.get_rect()
        self.backButton_rect = (900, 590)

        self.playButton_rect = self.playButton.get_rect()
        self.playButton_rect = (400, 200)
 

    def on_update(self):
        pass


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

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(900, 590, 64, 64).collidepoint(event.pos):
                return scene_home.SceneHome(self.dir)
            if pygame.Rect(400, 200, 256, 256).collidepoint(event.pos) and self.play == False:
                self.play = True
                # return scene_home.SceneHome(self.dir)
        return self
    
    mov = 0

    def on_draw(self, screen):
        global mov

        # update board with values save in move_history
        if self.play == True and self.mov < len(search_methods.solution.move_history):
            self.board = search_methods.solution.move_history[self.mov]
            time.sleep(1)
            self.mov +=1
        elif self.mov >= len(search_methods.solution.move_history):
            time.sleep(1)
            self.done = True

        self.screen = screen
        # Draw background
        pygame.draw.polygon(screen, self.gold, self.bg_vertices)

        pygame.draw.rect(screen, self.bg, pygame.Rect(10, 20, 200, 600))

        pygame.draw.rect(screen, self.gold, pygame.Rect(32, 32, 150, 50), 25, 20)
        pygame.draw.rect(screen, self.gold, pygame.Rect(560, 400, 140, 70), 200, 20)

        screen.blit(self.ia_text, self.ia_text_rect)
        screen.blit(self.backButton, self.backButton_rect)

        self.draw_board(screen)
        
        if self.done == True:
            screen.blit(self.finish_text, self.finish_text_rect)
            screen.blit(self.time_text, self.time_text_rect)

        if self.play == False:
            screen.blit(self.playButton, self.playButton_rect)

        
        

    