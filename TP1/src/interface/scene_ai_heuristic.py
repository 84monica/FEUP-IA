import pygame
from scene import Scene
import sys

import scene_ai_uniform
import scene_home
import scene_greedy
import scene_a_star
import scene_weighted_a_star

def draw_rectangle(x, y, screen, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 150, 150))

def draw_triangle(x, y, screen, color):
    pygame.draw.polygon(screen, color, [[100/2 + x, 100/2 + y], [x, 250/2 + y], [200/2 + x, 250/2 + y]])

class SceneAiHeuristic(Scene):
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

        self.uniform_title_text = self.font.render('Heuristic Search Methods', True, self.bg)

        self.bfs_text_one = self.small_font.render('Greedy', True, self.white)
        self.bfs_text_two = self.small_font.render('Search', True, self.white)

        self.dfs_text_one = self.small_font.render('A* Search', True, self.white)
        self.dfs_text_two = self.small_font.render(' ', True, self.white)

        self.id_text_one = self.small_font.render('Weighted', True, self.white)
        self.id_text_two = self.small_font.render('A* Search', True, self.white)


        # Get the dimensions of the text
        self.ai_text_rect = self.ai_text.get_rect()
        self.uniform_text_rect = self.uniform_text.get_rect()
        self.uniform_title_text_rect = self.uniform_title_text.get_rect()
        self.heuristic_text_rect = self.heuristic_text.get_rect()
        self.first_title_text_rect = self.first_title_text.get_rect()
        self.second_title_text_rect = self.second_title_text.get_rect()
        self.ai_text_rect = (50, 350)
        self.uniform_text_rect = (35, 428)
        self.uniform_title_text_rect = (550, 50)
        self.heuristic_text_rect = (35, 488)
        self.first_title_text_rect = (20, 20)
        self.second_title_text_rect = (70, 90)

        self.bfs_text_one_rect = self.bfs_text_one.get_rect()
        self.bfs_text_one_rect = (560, 240)
        self.bfs_text_two_rect = self.bfs_text_two.get_rect()
        self.bfs_text_two_rect = (560, 270)

        self.dfs_text_one_rect = self.dfs_text_one.get_rect()
        self.dfs_text_one_rect = (790, 350)
        self.dfs_text_two_rect = self.dfs_text_two.get_rect()
        self.dfs_text_two_rect = (780, 370)

        self.id_text_one_rect = self.id_text_one.get_rect()
        self.id_text_one_rect = (495, 520)
        self.id_text_two_rect = self.id_text_two.get_rect()
        self.id_text_two_rect = (490, 550)


        # Define back button
        self.backButton = pygame.image.load("TP1/src/Images/backward.png")

        # Get dimensions of button
        self.backButton_rect = self.backButton.get_rect()
        self.backButton_rect = (900, 590)

    def cancel_thread(self):
        pass

    def on_update(self):
        pass
 
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.Rect(20, 420, 300, 40).collidepoint(event.pos):
                return scene_ai_uniform.SceneAiUniform(self.dir)
            if pygame.Rect(520, 150, 150, 150).collidepoint(event.pos):
                return scene_greedy.SceneGreedy(self.dir)
            if pygame.Rect(770, 250, 150, 150).collidepoint(event.pos):
                return scene_a_star.SceneAStar(self.dir)
            if pygame.Rect(470, 430, 150, 150).collidepoint(event.pos):
                return scene_weighted_a_star.SceneWeightedAStar(self.dir)
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
        draw_rectangle(470, 430, screen, self.blue)
        draw_rectangle(770, 250, screen, self.blue)
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

        draw_triangle(545, 108, screen, self.red)
        pygame.draw.rect(screen, self.red, pygame.Rect(810, 260, 70, 70))
        pygame.draw.circle(screen, self.red, [545, 480], 40)
        screen.blit(self.backButton, self.backButton_rect)