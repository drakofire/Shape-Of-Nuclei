import pygame
import pymunk
import colorsys
import numpy as np
import pymunk.pygame_util

# Global Variables
width = 600
height = 600
marbles = []

def main():
    screen=pygame.display.set_mode((width, height))
    clock=pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = 00,100

    x=width/2
    y=height/2

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x,y)
    middle_shape = pymunk.Circle(body, 100)
    space.add(body, middle_shape)
    

    running = True
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    ticks_until_next_marble = 25
    counter = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
        if counter <= 1000:
            ticks_until_next_marble -= 1
            if ticks_until_next_marble <= 0:
                how_many_marbles(space, counter, ticks_until_next_marble)
                ticks_until_next_marble = 1
                counter+=1

        #space.debug_draw(draw_options)


        '''
        switch it to pygame draw 
        '''

        space.step(1 / 60)
        draw_marbles(screen, marbles)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def randomx(width):
    '''
    Randimizes a distance inbetween 0 and width. 
    '''
    rng = np.random.default_rng()
    x = rng.integers(0, width)
    return x

def how_many_marbles(space, counter, ticks):
    '''
    adds marble into arr to be spawned in space() later
    '''
    body2=pymunk.Body()
    body2.position = getrandompoint(width, height)
    circle=pymunk.Circle(body2, 9)
    circle.color = get_color(counter, ticks)
    circle.mass = 100
    space.add(body2, circle)
    marbles.append(circle)
    

def draw_marbles(screen, marbles):
    '''
    Draws marbles...l ol..
    '''
    for marble in marbles:
        pos = (int(marble.body.position.x), int(marble.body.position.y))
        pygame.draw.circle(screen, marble.color, pos, 9)


def get_color(counter, ticks):
    '''
    Uses an oscilating alg to pick the hue of the ball. Every 100 balls it shifts hue.
    '''
    group = counter // 100
    basic_hue = (group * 0.15) % 1.0 
    oscillation = 0.05 * (ticks / 50.0)
    hue = (basic_hue + oscillation) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)    #colorsys module.. converts Hue, Saturaltion, Variation to Red, Green, Blue
    return int(r * 255), int(g * 255), int(b * 255)


#def vector_calculation():
    

def getrandompoint(width, height):
    '''
    Treat perimeter as one continuous line, L=2*(width+height)
    Function cuts each section into strips. Depending on where the random distance lands,
    there will be a correlating section for which the ball spawns. 
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

main()



