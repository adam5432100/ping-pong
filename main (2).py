import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y, ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballspeed_x *= -1

def player_animation():
    global player_speed, player
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PING PONG by Adam')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('blue')
blue = (200, 200, 200)

ball_speed_x = 9
ball_speed_y = 8
player_speed = 0
opponent_speed = 20

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10

    ball_animation()
    player_animation()
  
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, blue, opponent)
    pygame.draw.ellipse(screen, blue, ball)
    pygame.draw.aaline(screen, blue, (screen_width/2, 0), (screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)
