# -*- encoding: utf-8 -*-
 
# Modules
import pygame
 
class Director:
    """Represents the main object of the game.
 
    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.
 
    This object must be used with Scene objects that are defined later."""
 
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Game Name")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
 
    def loop(self):
        "Main game loop."
 
        while not self.quit_flag:
            #time = self.clock.tick(60)
 
            # Exit events
            for event in pygame.event.get():
                self.scene = self.scene.on_event(event)
                if event.type == pygame.QUIT:
                    if self.scene.cancel_thread():
                        print("canceled")
                        self.quit()
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
 
            # Update scene
            self.scene.on_update()
 
            # Draw the screen
            self.scene.on_draw(self.screen)
            pygame.display.flip()
 
    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True