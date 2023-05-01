import math
import pygame

pygame.init()

windowSize = 600
window = pygame.display.set_mode((windowSize, windowSize))

pygame.display.set_caption("Ball Kinematics")

window.fill((255, 255, 255))

def invertCoord(coords):
    
    return (coords[0], windowSize - coords[1])

class Ball:

    def __init__(self, x, y, velocity, angle, color):

        self.x = x
        self.y = y
        
        self.vX = velocity * math.cos(math.radians(angle))
        self.vY = velocity * math.sin(math.radians(angle))

        self.color = color

    def periodic(self):

        self.x += self.vX/50
        self.y += self.vY/50

        self.vY -= 9.81

    def draw(self, surface):

        pygame.draw.circle(surface, self.color, invertCoord((self.x, self.y)), 5)

b = Ball(0, 0, 100, 45, (255, 0, 0))

running = True

while running:

    if pygame.time.get_ticks() % (1000 / 50) == 0:

        print(f"frame\n{pygame.time.get_ticks()}\n")

        window.fill((255, 255, 255))
        
        b.periodic()
        b.draw(window)

        pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False