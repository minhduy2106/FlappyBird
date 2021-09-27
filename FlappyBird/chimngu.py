from typing import SupportsRound
import pygame
from random import randint
import sys

from pygame.constants import K_SPACE

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappybird')
running = True
pausing = False
clock = pygame.time.Clock()
background = pygame.image.load("asset/sprites/background-day.png")
background = pygame.transform.scale(background, (400, 600))

x_bird = 50
y_bird = 350
tube1_x = 600
tube2_x = 800
tube3_x = 1000
tube_width = 50
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

bird_img = pygame.image.load("asset/sprites/yellowbird-midflap.png")
bird_img = pygame.transform.scale(bird_img, (30, 30))
base_img = pygame.image.load("asset/sprites/base.png")
base_img = pygame.transform.scale(base_img, (400, 50))

tube_img = pygame.image.load("asset/sprites/tube.png")
tube_op_img = pygame.image.load("asset/sprites/tube_op.png")
distan_tube = 120

bird_drop_velocity = 0
gravity = 0.5
tube_velocity = 2
score = 0
font = pygame.font.SysFont('san', 20)


tube1_pass = False
tube2_pass = False
tube3_pass = False
score = 0

message_img = pygame.image.load("asset/sprites/message.png")
message_img = pygame.transform.scale(message_img, (200, 300))
font1 = pygame.font.SysFont('san', 50)

die = pygame.mixer.Sound("asset/audio/die.wav")
hit = pygame.mixer.Sound("asset/audio/hit.wav")
point = pygame.mixer.Sound("asset/audio/point.wav")
wing = pygame.mixer.Sound("asset/audio/wing.wav")

while running:

    clock.tick(60)
    screen.blit(background, (0, 0))
    base = screen.blit(base_img, (0, 550))
    bird = screen.blit(bird_img, (x_bird, y_bird))

    # draw tube
    tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x, 0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
    # oposite tube
    tube1_op_img = pygame.transform.scale(
        tube_op_img, (tube_width, 600 - (tube1_height + distan_tube + 50)))
    tube1_op = screen.blit(tube1_op_img, (tube1_x, tube1_height + distan_tube))
    tube2_op_img = pygame.transform.scale(
        tube_op_img, (tube_width, 600 - (tube2_height + distan_tube + 50)))
    tube2_op = screen.blit(tube2_op_img, (tube2_x, tube2_height + distan_tube))
    tube3_op_img = pygame.transform.scale(
        tube_op_img, (tube_width, 600 - (tube3_height + distan_tube + 50)))
    tube3_op = screen.blit(tube3_op_img, (tube3_x, tube3_height + distan_tube))
    # tube_move
    tube1_x -= tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity
    # create new tube
    if tube1_x < -tube_width:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_pass = False
    if tube2_x < -tube_width:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False
    if tube3_x < -tube_width:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_pass = False

    # show_score
    score_txt = font.render("Score : " + str(score), True, (255, 0, 0))
    screen.blit(score_txt, (5, 5))
    # plus score
    if tube1_x + tube_width <= x_bird and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + tube_width <= x_bird and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + tube_width <= x_bird and tube3_pass == False:
        score += 1
        tube3_pass = True

    # check va cham
    tubes = [tube1, tube2, tube3, tube1_op, tube2_op, tube3_op]
    for tube in tubes:
        if bird.colliderect(tube):
            tube_velocity = 0
            bird_drop_velocity = 0
            f_score = font1.render("SCORE : " + str(score), True, (255, 0, 0))
            screen.blit(f_score, (100, 100))
            screen.blit(message_img, (85, 160))
            pausing = True
    if bird.colliderect(base):
        pygame.mixer.Sound.play(die).tick(1)
        tube_velocity = 0
        bird_drop_velocity = 0
        f_score = font1.render("SCORE : " + str(score), True, (255, 0, 0))
        screen.blit(f_score, (100, 100))
        screen.blit(message_img, (85, 160))
        pausing = True

    # drop bird
    y_bird += bird_drop_velocity
    bird_drop_velocity += gravity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                if pausing:
                    x_bird = 50
                    y_bird = 350
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    tube_velocity = 2
                    score = 0
                    pausing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                if pausing:
                    x_bird = 50
                    y_bird = 350
                    tube1_x = 600
                    tube2_x = 800
                    tube3_x = 1000
                    tube_velocity = 2
                    score = 0
                    pausing = False

    pygame.display.flip()

pygame.quit()
