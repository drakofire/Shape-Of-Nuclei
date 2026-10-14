import pygame
import pymunk
import numpy as np
import pymunk.pygame_util


width = 600
height = 600

screen=pygame.display.set_mode((width, height))
clock=pygame.time.Clock()

space = pymunk.Space()
space.gravity = 9,90

x=width/2
y=height/2

body = pymunk.Body(body_type=pymunk.Body.STATIC)
body.position = (x,y)
obb = pymunk.Circle(body, 100)
obb.friction = 100.0
space.add(body, obb)


def randomx(width):
    rng = np.random.default_rng()
    x = rng.integers(0, width)
    return x

def how_many_marbles(n):
    for i in range(n):
        body2=pymunk.Body()
        body2.position = getrandompoint(width, height)
        circle=pymunk.Circle(body2, 9)
        circle.color=pygame.Color("pink")
        #ok now try to make it so they all go to the center
        #I think I am going to have to make a vector for the ball and calculate it going in that direction :_L I'll continue tomorrow.

        circle.mass = 10
        #I still don;t know what .friction does lol
        #circle.friction = 900.0
        space.add(body2, circle)

def getrandompoint(width, height):
    '''
    Idea: treat perimeter as one continuous line, L=2*(width+height)
    cut each section into strips yo
    '''
    L=2*(width+height)
    rng = np.random.default_rng()
    random_dist = rng.integers(0, L)
    if random_dist < width:
        #Top
        return random_dist, 0
    elif random_dist < width + height:
        #Right
        return width, random_dist-width
    elif random_dist < 2*width + height:
        #Bottom
        return width - (random_dist - (width+height)), height
    elif random_dist < L:
        #Left
        return 0, height - (random_dist - (2*width + height))

'''
body2=pymunk.Body()
body2.position = x, 0
circle=pymunk.Circle(body2, 9)
circle.color=pygame.Color("pink")
circle.mass = 10
circle.friction = 900.0
space.add(body2, circle)
'''
how_many_marbles(10)



running = True
draw_options = pymunk.pygame_util.DrawOptions(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    
    space.debug_draw(draw_options)

     # Update physics
    space.step(1 / 60)

    # Display everything
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


