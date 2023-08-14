import pygame
import time
import random

pygame.init()

#color
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#window size
window_width = 800
window_height = 600

# Snake
snake_block = 10

# Size of the score
font_style = pygame.font.SysFont(None, 50)

# Display the score on the screen
def your_score(score):
    value = font_style.render("Pontuação: " + str(score), True, BLACK)
    game_window.blit(value, [0, 0])

# Snake drawing on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], snake_block, snake_block])

# Game Over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])

# Main function
def gameLoop():
    game_over = False
    game_close = False

    # Initial position
    snake_x = window_width / 2
    snake_y = window_height / 2

    # Speed
    snake_x_change = 0
    snake_y_change = 0

    # Store the snake's segments
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_window.fill(WHITE)
            message("Game Over! \n Pressione P-Play Again ou Q-Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block
                    snake_x_change = 0

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        game_window.fill(WHITE)
        pygame.draw.rect(game_window, RED, [food_x, food_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(snake_x)
        snake_Head.append(snake_y)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(30)

    pygame.quit()
    quit()

# Start
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Jogo da Cobra')
clock = pygame.time.Clock()
gameLoop()
