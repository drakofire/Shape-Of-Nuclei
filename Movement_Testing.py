import sys
import pygame
import pymunk
import pymunk.pygame_util

# 1. Initialize Pygame and screen window
pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

# 2. Setup Pymunk Space
space = pymunk.Space()
space.gravity = (0, 0)

static_body = space.static_body
walls = [
    pymunk.Segment(static_body, (0, 750), (750, 750), 5),  # Bottom floor
    pymunk.Segment(static_body, (0, 0), (0, 750), 5),      # Left wall
    pymunk.Segment(static_body, (750, 0), (750, 750), 5),  # Right wall
    pymunk.Segment(static_body, (0, 0), (750, 0), 5)       # Top ceiling
]

for wall in walls:
    wall.elasticity = 1 
    wall.friction = 0.3   

space.add(*walls)
# -----------------------------------------------------
vertices = [
    (0,250), (50,50), (200,50), (100,-50), (150,-250), (0,-100), (-150,-250), (-100,-50), (-200,50), (-50,50)
]
obstacle_body = pymunk.Body(body_type=pymunk.Body.STATIC)
obstacle_body.position = (300, 300)  # Set position

# 2. Attach a shape (box, circle, or polygon)
obstacle_shape = pymunk.Poly(obstacle_body, vertices)
obstacle_shape.friction = 0.8
obstacle_shape.elasticity = 0.2


# 3. Add BOTH the custom static body and its shape to space
space.add(obstacle_body, obstacle_shape)
def create_box(space, position, radius=5, mass=5):
    # 1. Calculate moment for the shape
    moment = pymunk.moment_for_circle(mass, 0, radius)
    
    # 2. Create UNIQUE body and shape instances
    body = pymunk.Body(mass, moment)
    body.position = position
    
    shape = pymunk.Circle(body, radius, offset=(0, 0))
    shape.elasticity = 0.7
    shape.friction = 0.5
    shape.elasticity = 1  # Set bounciness on the box shape to match walls
    shape.friction = 0.01
    body.velocity = (1000, 1000)
    
    # 3. Add the new instance pair to the space
    space.add(body, shape)
    return body, shape

for i in range(500):
    create_box(space, (100, 100))


# 4. Simulation & Rendering Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    space.step(1 / 60.0)
    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()