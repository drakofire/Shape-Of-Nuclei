import pygame
import pymunk               # Import pymunk..
import pymunk.pygame_util

# draw a picture of something on a piece of paper, and take a picture of it and upload it to program and do things!!!!

"""
It would be funny if we had the marbles going toward the shape at randomized trajectories 

one marble at a time
detect 

oh we already have that one down, don't need to go over it again

make it part of the shape, dont avoid those position

-->diffusion limited aggregation

--> if neighbor to a marble use, refract back/ bouncing wall to keep it, less expensive! 
sitting in a grid-- sitting in a shape accross
marble doesn't stick-- refracted run it until it hits the shape
have some maximum steps, start a new thing

"""

#Init Pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

space = pymunk.Space()      # Create a Space which contain the simulation
space.gravity = 0,81      # Set its gravity


body = pymunk.Body()        # Create a Body
body.position = 300,300      # Set the position of the body

body2 = pymunk.Body()
body2.position = 200,200

circle = pymunk.Circle(body2,100)
circle.color = pygame.Color("pink")
circle.mass = 100
space.add(body2, circle)

poly = pymunk.Poly.create_box(body) # Create a box shape and attach to body
poly.mass = 100              # Set the mass on the shape
space.add(body, poly)       # Add both body and shape to the simulation

draw_options = pymunk.pygame_util.DrawOptions(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    space.step(1/60)

    screen.fill(pygame.Color("White"))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()