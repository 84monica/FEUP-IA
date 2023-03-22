import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((1000, 700))

# Set up the font
font = pygame.font.SysFont('Arial', 34)
title_font = pygame.font.SysFont('Arial', 70)

# Define the vertices of the figure
bg_vertices = [(0, 0), (0, 700), (1000, 700), (1000, 0)]

# Define the color of the figure
bg = (130, 50, 180) # purple
gold = (235, 183, 12) # buttons
white = (255, 255, 255) # white
red = (255, 0, 0) # red

# Define the texts
ai_text = font.render('AI', True, white)
human_text = font.render('Human', True, white)
first_title_text = title_font.render('SYMMETRIC', True, white)
second_title_text = title_font.render('PUZZLES', True, white)

# Get the dimensions of the text
ai_text_rect = ai_text.get_rect()
human_text_rect = human_text.get_rect()
first_title_text_rect = first_title_text.get_rect()
second_title_text_rect = second_title_text.get_rect()

ai_text_rect = (362, 418)
human_text_rect = (577, 418)
first_title_text_rect = (300, 140)
second_title_text_rect = (350, 210)

# Draw background
pygame.draw.polygon(screen, bg, bg_vertices)

pygame.draw.rect(screen, gold, pygame.Rect(310, 400, 140, 70), 200, 20)
pygame.draw.rect(screen, gold, pygame.Rect(560, 400, 140, 70), 200, 20)

screen.blit(ai_text, ai_text_rect)
screen.blit(human_text, human_text_rect)
screen.blit(first_title_text, first_title_text_rect)
screen.blit(second_title_text, second_title_text_rect)



# Keep the window open until the user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.Rect(310, 400, 140, 70).collidepoint(event.pos):
                print('Button clicked!')
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()