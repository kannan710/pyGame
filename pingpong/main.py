import pygame
from sys import exit
from random import choice

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_y:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_x:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_y:
        opponent.bottom = screen_y

def restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_x // 2, screen_y // 2)

    if current_time - score_time < 700:
        number_three = game_font.render('3', False, 'white')
        screen.blit(number_three, (screen_x // 2 - 8, screen_y // 2 + 13))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render('2', False, 'white')
        screen.blit(number_two, (screen_x // 2 - 8, screen_y // 2 + 13))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render('1', False, 'white')
        screen.blit(number_one, (screen_x // 2 - 8, screen_y // 2 + 13))
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = 7 * choice((1, -1))
        ball_speed_y = 7 * choice((1, -1))
        score_time = None


screen_x = 1000
screen_y = 600

pygame.init()

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('Ping Pong game')
clock = pygame.time.Clock()

#Game rectangles
ball = pygame.Rect(screen_x // 2 - 10, screen_y // 2 - 10, 20, 20)
player = pygame.Rect(screen_x - 20, screen_y // 2 - 45, 10, 90)
opponent = pygame.Rect(10, screen_y // 2 - 45, 10, 90)

#ball speed
ball_speed_x = 4 * choice((1, -1))
ball_speed_y = 4 * choice((1, -1))
#player speed
player_speed = 0
#opponent speed
opponent_speed = 6

player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 28)

score_time = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_UP:
                player_speed = 0
    
    ball_animation()
    opponent_ai()
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_y:
        player.bottom = screen_y
    
    screen.fill('black')
    pygame.draw.rect(screen, 'white', player)
    pygame.draw.rect(screen, 'white', opponent)
    pygame.draw.ellipse(screen, 'white', ball)
    pygame.draw.aaline(screen, 'white', (screen_x / 2, 0), (screen_x / 2, screen_y))
    
    if score_time:
        restart()

    player_text = game_font.render(f'{player_score}', False, 'white')
    player_text_rect = player_text.get_rect(center = (screen_x // 2 + 20, screen_y // 2))
    screen.blit(player_text, player_text_rect)

    opponent_text = game_font.render(f'{opponent_score}', False, 'white')
    opponent_text_rect = opponent_text.get_rect(center = (screen_x // 2 - 20, screen_y // 2))
    screen.blit(opponent_text, opponent_text_rect)

    pygame.display.update()
    clock.tick(60)

