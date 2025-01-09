import pygame
import random
pygame.init()

win = pygame.display.set_mode((400,600))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 56)#(default_font_style,font_size)
def text_screen(text, color, x, y):
    screen_text = font.render(text,True, color)#text, antihalazing:converting high resolution to low resolution,color
    win.blit(screen_text, [x,y]) #blit function update the screen


def plot_snake(win, color, snk_list, width, height):
    #print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(win, color, [x, y, width, height])

def gem_loop():
    exit_game = False
    game_over = False
    
    x = 50
    y = 50
    width = 10
    height = 10
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    fps = 30
    velocity_x = 0
    velocity_y = 0
    vel = 4
    food_x = random.randint(0,400/2)
    food_y = random.randint(0,400/2)
    score = 0

    snk_list = []
    snk_length = 1

    while not exit_game:
        #pygame.time.delay(100)-> this is shortcut
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:#type of event
                if event.key == pygame.K_RIGHT:#Which key for run event
                    velocity_x = vel
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -vel
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -vel
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = vel
                    velocity_x = 0
        
        x = x + velocity_x
        y = y + velocity_y

        if abs(x - food_x)<6 and abs(y - food_y)<6:#dist bet food and snake is less tahn 6
            score += 1
            print("Score: ",score * 10)# display score on console                            
            food_x = random.randint(0,400/2)
            food_y = random.randint(0,400/2)
            snk_length += 5
        
        win.fill(white)
        text_screen("Score: " + str(score * 10), red, 5, 5)#String concanicate
        '''pygame is contains layer like in ibispaint x for example we created white window below that we showing score
        the score won't display if we write function before white window'''
        pygame.draw.rect(win, red, [food_x, food_y, width, height])
        #pygame.draw.rect(win, black, [x, y, width, height])#snake body
        #pygame.draw.rect(where, color, [coordinates x, y, width,height-> size of snake])

        head = []
        head.append(x)
        head.append(y)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]

            plot_snake(win, black, snk_list, width, height)#x & y replaced with snk_list, cause we defined x,y in list
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()
gem_loop()


