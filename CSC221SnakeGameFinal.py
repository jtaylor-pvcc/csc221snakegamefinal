import pygame
import random
#initializes pygame + display
pygame.init() 
pygame.display.init()
#sets display parameters
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

grid_size = 20
grid_width = width // grid_size
grid_height = height // grid_size
#sets colors
black = (0, 0, 0)
white = (255, 255, 255)
red =(255, 0, 0)
green = (0, 255, 0) 
#defines snake basics
snake_color = green
snake_speed = 10
snake_block = 20

font_style = pygame.font.SysFont(None, 50)
#defines message
def message(msg, color, y_displacement=0):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(width / 2, height / 2 + y_displacement))
    screen.blit(mesg, mesg_rect)
#defines the game loop  
def game_loop():
    running = True
    game_over = False
    game_quit = False

                
    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    snake_length = 1
    snake_list = []
    #randomizes food spawn position on x and y axes
    food_x = round(random.randrange(0, width - snake_block) / 20) * 20
    food_y = round(random.randrange(0, height - snake_block) / 20) * 20
     
    clock = pygame.time.Clock()
   
  
    #starts game loop                   
    while not game_over and not game_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_over = True
               game_quit = True
            if event.type == pygame.KEYDOWN: #sets movement via arrow keys
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                       x1_change = snake_block
                       y1_change = 0
                elif event.key == pygame.K_UP:
                        x1_change = 0
                        y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                        x1_change = 0
                        y1_change = snake_block
        #ends game if snake collides with border
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])#draws food
        #sets snake head
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        #allows snake length not to get too long
        if len(snake_list) > snake_length:
            del snake_list[0]
        #if snake head collides with its body, game ends
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        for pos in snake_list:
            pygame.draw.rect(screen, snake_color, [pos[0], pos[1], snake_block, snake_block])

        pygame.display.update()
        #if snake eats food, length increases
        if x1 == food_x and y1 == food_y:
            snake_length += 1
            food_x = round(random.randrange(0, width - snake_block) / 20) * 20
            food_y = round(random.randrange(0, height - snake_block) / 20) * 20
           
        clock.tick(snake_speed)
    #if snake collides with itself or border, game ends and messages pops up
    message("GAME OVER!", red)
    message("Press Q to Quit or P to Play Again", white, 50)
    pygame.display.update()
    #system waits for user input to decide next course of action
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    waiting = False
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    game_loop()

   

game_loop()
