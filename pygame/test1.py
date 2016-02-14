
background_image_filename = 'img/sushiplate.jpg'
mouse_image_filename = 'img/fugu.png'

import pygame
from pygame.locals import * 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480),0,32)
#screen = pygame.display.set_mode((640, 480), 0, 32)

#pygame.display.set_caption("hello,world")
pygame.display.set_caption("hello world")
#pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename)
mouse_curse = pygame.image.load(mouse_image_filename)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    x, y = pygame.mouse.get_pos();
    
    x -= mouse_curse.get_width() / 2
    y -= mouse_curse.get_height() / 2
    
    screen.blit(mouse_curse, (x, y))
    
    pygame.display.update()


