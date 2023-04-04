import pygame
from scene import Scene
import sys

import scene_ai_uniform
import scene_home
import scene_greedy
import scene_a_star
import scene_weighted_a_star
import scene_ai_heuristic
import search_methods

def draw_rectangle(x, y, screen, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 150, 150))

def draw_triangle(x, y, screen, color):
    pygame.draw.polygon(screen, color, [[100/2 + x, 100/2 + y], [x, 250/2 + y], [200/2 + x, 250/2 + y]])

class SceneAiChooseHeuristic(Scene):
    """ Welcome screen of the game, the first one to be loaded."""
 
    def __init__(self, director):
        self.dir = director

        # Set up the font
        self.font = pygame.font.SysFont('Arial', 34)
        self.title_font = pygame.font.SysFont('Arial', 70)
        self.small_font = pygame.font.SysFont('Arial', 24)

        # Define the vertices of the figure
        self.bg_vertices = [(0, 0), (0, 700), (1000, 700), (1000, 0)]
        self.second_part = [(480, 0), (310, 700), (1000, 700), (1000, 0)]
        self.division_vertices = [(470, 0), (300, 700), (320, 700), (490, 0)]

        # Define the color of the figure
        self.bg = (130, 50, 180) # purple
        self.gold = (235, 183, 12) # buttons
        self.white = (255, 255, 255) # white
        self.red = (255, 0, 0) # red
        self.blue = (60, 204, 247) # division

        # Define the texts
        self.ai_text = self.font.render('AI', True, self.white)
        self.first_title_text = self.title_font.render('SYMMETRIC', True, self.white)
        self.second_title_text = self.title_font.render('PUZZLES', True, self.white)

        self.uniform_text = self.small_font.render('Uniform Search Methods', True, self.white)
        self.heuristic_text = self.small_font.render('Heuristic Search Methods', True, self.white)

        self.uniform_title_text = self.font.render('Choose heuristic', True, self.bg)

        self.bfs_text_one = self.small_font.render('H1', True, self.white)
        self.bfs_text_two = self.small_font.render(' ', True, self.white)

        self.dfs_text_one = self.small_font.render('H2', True, self.white)
        self.dfs_text_two = self.small_font.render(' ', True, self.white)

        self.id_text_one = self.small_font.render('H3', True, self.white)
        self.id_text_two = self.small_font.render(' ', True, self.white)

        self.h1_text_1 = self.small_font.render('Number of rows and', True, self.white)
        self.h1_text_2 = self.small_font.render('columns that are\'t', True, self.white)
        self.h1_text_3 = self.small_font.render('palindormes / 2', True, self.white)

        self.h2_text_1 = self.small_font.render('Assigns a score to each row', True, self.white)
        self.h2_text_2 = self.small_font.render('and column based on how ', True, self.white)
        self.h2_text_3 = self.small_font.render('close it is to being a palindrome', True, self.white)

        self.h3_text_1 = self.small_font.render('Makes an estimation of the ', True, self.white)
        self.h3_text_2 = self.small_font.render('number of pieces that need to', True, self.white)
        self.h3_text_3 = self.small_font.render('be placed to end the game', True, self.white)



        # Get the dimensions of the text
        self.ai_text_rect = self.ai_text.get_rect()
        self.uniform_text_rect = self.uniform_text.get_rect()
        self.uniform_title_text_rect = self.uniform_title_text.get_rect()
        self.heuristic_text_rect = self.heuristic_text.get_rect()
        self.first_title_text_rect = self.first_title_text.get_rect()
        self.second_title_text_rect = self.second_title_text.get_rect()
        self.ai_text_rect = (50, 350)
        self.uniform_text_rect = (35, 428)
        self.uniform_title_text_rect = (600, 50)
        self.heuristic_text_rect = (35, 488)
        self.first_title_text_rect = (20, 20)
        self.second_title_text_rect = (70, 90)

        self.bfs_text_one_rect = self.bfs_text_one.get_rect()
        self.bfs_text_one_rect = (580, 255)
        self.bfs_text_two_rect = self.bfs_text_two.get_rect()
        self.bfs_text_two_rect = (560, 270)

        self.dfs_text_one_rect = self.dfs_text_one.get_rect()
        self.dfs_text_one_rect = (515, 420)
        self.dfs_text_two_rect = self.dfs_text_two.get_rect()
        self.dfs_text_two_rect = (780, 370)

        self.id_text_one_rect = self.id_text_one.get_rect()
        self.id_text_one_rect = (450, 590)
        self.id_text_two_rect = self.id_text_two.get_rect()
        self.id_text_two_rect = (490, 550)

        self.h1_text_1_rect = self.h1_text_1.get_rect()
        self.h1_text_2_rect = self.h1_text_2.get_rect()
        self.h1_text_3_rect = self.h1_text_3.get_rect()

        self.h2_text_1_rect = self.h2_text_1.get_rect()
        self.h2_text_2_rect = self.h2_text_2.get_rect()
        self.h2_text_3_rect = self.h2_text_3.get_rect()

        self.h3_text_1_rect = self.h3_text_1.get_rect()
        self.h3_text_2_rect = self.h3_text_2.get_rect()
        self.h3_text_3_rect = self.h3_text_3.get_rect()

        self.h1_text_1_rect = (700, 175)
        self.h1_text_2_rect = (700, 205)
        self.h1_text_3_rect = (700, 235)

        self.h2_text_1_rect = (640, 350)
        self.h2_text_2_rect = (640, 385)
        self.h2_text_3_rect = (640, 420)

        self.h3_text_1_rect = (580, 520)
        self.h3_text_2_rect = (580, 555)
        self.h3_text_3_rect = (580, 590)

        # Define back button
        self.backButton = pygame.image.load("TP1/src/Images/backward.png")

        # Get dimensions of button
        self.backButton_rect = self.backButton.get_rect()
        self.backButton_rect = (900, 590)

    def cancel_thread(self):
        pass

    def on_update(self):
        pass
 
    heuristic_ = None

    def def_heuristic(self, num):
        global heuristic_
        if num == 1:
            heuristic_ = search_methods.h1
        elif num == 2:
            heuristic_ = search_methods.h2
        elif num == 3:
            heuristic_ = search_methods.h3
        else:
            heuristic_ = search_methods.h1

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.Rect(20, 420, 300, 40).collidepoint(event.pos):
                return scene_ai_uniform.SceneAiUniform(self.dir)
            if pygame.Rect(520, 150, 150, 150).collidepoint(event.pos):
                self.def_heuristic(1)
                return scene_ai_heuristic.SceneAiHeuristic(self.dir)
            if pygame.Rect(455, 320, 150, 150).collidepoint(event.pos):
                self.def_heuristic(2)
                return scene_ai_heuristic.SceneAiHeuristic(self.dir)
            if pygame.Rect(390, 490, 150, 150).collidepoint(event.pos):
                self.def_heuristic(2)
                return scene_ai_heuristic.SceneAiHeuristic(self.dir)
            if pygame.Rect(900, 590, 64, 64).collidepoint(event.pos):
                return scene_home.SceneHome(self.dir)
        return self
 
    def on_draw(self, screen):
        # Draw background
        pygame.draw.polygon(screen, self.bg, self.bg_vertices)
        pygame.draw.polygon(screen, self.gold, self.second_part)
        pygame.draw.polygon(screen, self.blue, self.division_vertices)

        pygame.draw.rect(screen, self.gold, pygame.Rect(20, 420, 300, 40), 20, 20)
        pygame.draw.rect(screen, self.gold, pygame.Rect(20, 480, 300, 40), 20, 20)

        draw_rectangle(520, 150, screen, self.blue)
        draw_rectangle(455, 320, screen, self.blue)
        draw_rectangle(390, 490, screen, self.blue)
        screen.blit(self.bfs_text_one, self.bfs_text_one_rect)
        screen.blit(self.bfs_text_two, self.bfs_text_two_rect)
        screen.blit(self.dfs_text_one, self.dfs_text_one_rect)
        screen.blit(self.dfs_text_two, self.dfs_text_two_rect)
        screen.blit(self.id_text_one, self.id_text_one_rect)
        screen.blit(self.id_text_two, self.id_text_two_rect)

        screen.blit(self.ai_text, self.ai_text_rect)
        screen.blit(self.uniform_text, self.uniform_text_rect)
        screen.blit(self.heuristic_text, self.heuristic_text_rect)
        screen.blit(self.uniform_title_text, self.uniform_title_text_rect)
        screen.blit(self.first_title_text, self.first_title_text_rect)
        screen.blit(self.second_title_text, self.second_title_text_rect)

        screen.blit(self.h1_text_1, self.h1_text_1_rect)
        screen.blit(self.h1_text_2, self.h1_text_2_rect)
        screen.blit(self.h1_text_3, self.h1_text_3_rect)

        screen.blit(self.h2_text_1, self.h2_text_1_rect)
        screen.blit(self.h2_text_2, self.h2_text_2_rect)
        screen.blit(self.h2_text_3, self.h2_text_3_rect)

        screen.blit(self.h3_text_1, self.h3_text_1_rect)
        screen.blit(self.h3_text_2, self.h3_text_2_rect)
        screen.blit(self.h3_text_3, self.h3_text_3_rect)

        draw_triangle(545, 108, screen, self.red)
        pygame.draw.rect(screen, self.red, pygame.Rect(495, 330, 70, 70))
        pygame.draw.circle(screen, self.red, [465, 540], 40)
        screen.blit(self.backButton, self.backButton_rect)