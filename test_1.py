import pygame
import pymunk
import pymunk.pygame_util


width = 600
height = 600

screen=pygame.display.set_mode((width, height))
clock=pygame.time.Clock()

space = pymunk.Space()
space.gravity = 0,90

x=width/2
y=height/2

body = pymunk.Body(body_type=pymunk.Body.STATIC)
body.position = (x,y)
obb = pymunk.Circle(body, 20)
space.add(body, obb)

body2=pymunk.Body()
body2.position = x, 9
circle=pymunk.Circle(body2, 9)
circle.color=pygame.Color("pink")
circle.mass = 10
space.add(body2, circle)



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


