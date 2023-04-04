import pygame, sys
from scene import Scene
import scene_ai_uniform
import scene_human

class SceneHome(Scene):
    """ Welcome screen of the game, the first one to be loaded."""
 
    def __init__(self, director):
        self.dir = director

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
        self.ai_text = self.font.render('AI', True, self.white)
        self.human_text = self.font.render('Human', True, self.white)
        self.first_title_text = self.title_font.render('SYMMETRIC', True, self.white)
        self.second_title_text = self.title_font.render('PUZZLES', True, self.white)

        # Get the dimensions of the text
        self.ai_text_rect = self.ai_text.get_rect()
        self.human_text_rect = self.human_text.get_rect()
        self.first_title_text_rect = self.first_title_text.get_rect()
        self.second_title_text_rect = self.second_title_text.get_rect()

        self.ai_text_rect = (362, 418)
        self.human_text_rect = (577, 418)
        self.first_title_text_rect = (300, 140)
        self.second_title_text_rect = (350, 210)
 
    def cancel_thread(self):
        pass

    def on_update(self):
        pass
 
    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.Rect(310, 400, 140, 70).collidepoint(event.pos):
                return scene_ai_uniform.SceneAiUniform(self.dir)
            if pygame.Rect(560, 400, 140, 70).collidepoint(event.pos):
                return scene_human.SceneHuman(self.dir)

        return self
 
    def on_draw(self, screen):
        # Draw background
        pygame.draw.polygon(screen, self.bg, self.bg_vertices)

        pygame.draw.rect(screen, self.gold, pygame.Rect(310, 400, 140, 70), 200, 20)
        pygame.draw.rect(screen, self.gold, pygame.Rect(560, 400, 140, 70), 200, 20)

        screen.blit(self.ai_text, self.ai_text_rect)
        screen.blit(self.human_text, self.human_text_rect)
        screen.blit(self.first_title_text, self.first_title_text_rect)
        screen.blit(self.second_title_text, self.second_title_text_rect)