import pygame
# Initialize the pygame
pygame.init()

# Create a game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Battle Ship")
icon = pygame.image.load('space-shuttle.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('arcade-game.png')
PlayerX = 370
PlayerY = 500
PlayerX_change = 0

def player(x,y):
    screen.blit(PlayerImg,(x,y))

running = True
# Game loop
while running:
    screen.fill((37,124,148)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Keystroke
        if event.type == pygame.KEYDOWN:
            print("Key is pressed")
            if event.key == pygame.K_LEFT:
                PlayerX_change = -0.1
                print("Left key is pressed")
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 0.1
                print("Right key is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key is released")
    #FMY = 5 = 5 -> 5 '+=' -0.1 -> 5 = 5 - 0.1
        #  5 = 5 -> 5 '+=' 0.1 -> 5 = 5 + 0.1
    PlayerX += PlayerX_change
    player(PlayerX,PlayerY)


    pygame.display.update()