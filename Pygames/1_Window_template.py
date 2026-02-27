"""
Video Reference: '@KennyYipCoding'....🌈
"""

import pygame
import random

# Game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) # You need to pass a touple inside function.
pygame.display.set_caption("Legendery Coder Sourabh's Game") # Title of the window
clock = pygame.time.Clock() # Used for the frame rate.


while True: # Game loop. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicks the 'X' button on top-right corner of window
            pygame.quit()
            exit()

    pygame.display.update() # Update display by redrawing the screen
    clock.tick(60) # 60 Frames Per Second (FPS)




