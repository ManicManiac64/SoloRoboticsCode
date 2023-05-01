import math
import random
import pygame

pygame.init()

windowSize = 600
window = pygame.display.set_mode((windowSize, windowSize))

framesPerSecond = 25

pygame.display.set_caption("Robot Arm Inverse Kinematics")

window.fill((255, 255, 255))

font = pygame.font.SysFont("Consolas", 20)

def invertCoord(coords):
    
    return (coords[0], windowSize - coords[1])


def debugPrint(title, value):
    
    print(f"{title}: {value}")

def label(screen: pygame.Surface, xy: tuple, text: str, color: tuple):

        screen.blit(font.render(text, False, color), xy)




class ArmSolver2:

    def __init__(self, baseX, baseY, length1, length2):

        self.length1 = length1
        self.length2 = length2

        self.maxReach = self.length1 + self.length2
        self.minReach = abs(self.length1 - self.length2)

        self.baseX = baseX
        self.baseY = baseY

        self.theta1 = math.radians(45)
        self.theta2 = math.radians(45)

        self.joints = [
            
                    [self.baseX, 
                    self.baseY],
                       
                    [self.baseX + self.length1 * math.cos(self.theta1), 
                    self.baseY + self.length1 * math.sin(self.theta1)],
                       
                    [self.baseX + self.length1 * math.cos(self.theta1) + self.length2 * math.cos(self.theta2), 
                    self.baseY + self.length1 * math.sin(self.theta1) + self.length2 * math.sin(self.theta2)]
                    ]

        self.lastJointCoord = [self.joints[2][0], self.joints[2][1]]

        self.elbowUp = True

    
    def targetToAngles(self, target: tuple):

        self.lastJointCoord = [self.joints[2][0], self.joints[2][1]]
        
        target = ((target[0] - self.baseX), (target[1] - self.baseY))

        r = math.sqrt(((target[0] ** 2) + (target[1] ** 2)))

        if self.minReach <= r <= self.maxReach:

            alpha = math.acos(((self.length1 ** 2) + (self.length2 ** 2) - (r ** 2)) / (2 * self.length1 * self.length2))

            self.theta2 = (math.radians(180) - alpha) if self.elbowUp else math.radians(180) - alpha

            psi = math.atan2((self.length2) * math.sin(self.theta2), (self.length1 + ((self.length2) * math.cos(self.theta2))))
            beta = math.atan2(target[1], target[0])

            if self.elbowUp:

                self.theta1 = beta + psi

            else:

                self.theta1 = beta - psi

            self.joints = [[self.baseX, self.baseY],
                           [self.baseX + self.length1 * math.cos(self.theta1), self.baseY + self.length1 * math.sin(self.theta1)],
                           [self.baseX + r * math.cos(beta), self.baseY + r * math.sin(beta)]]

    
    def lastJointVelocity(self):

        return [(self.joints[2][0] - self.lastJointCoord[0]) * framesPerSecond, (self.joints[2][1] - self.lastJointCoord[1]) * framesPerSecond]




balls = []

class Ball:

    def __init__(self, x, y, velocity, angle, color):

        self.x = x
        self.y = y
        
        self.vX = velocity * math.cos(math.radians(angle))
        self.vY = velocity * math.sin(math.radians(angle))

        self.color = color

        self.caught = False

        balls.append(self)

        self.start = pygame.time.get_ticks()

    
    def periodic(self):

        self.x += self.vX / framesPerSecond
        self.y += self.vY / framesPerSecond

        self.vY -= 5

        if self.y < 0:

            self.vY *= -0.5
            self.y = 0
    
    def draw(self, surface):

        pygame.draw.circle(surface, self.color, invertCoord((self.x, self.y)), 5)




def drawArm(surface: pygame.Surface, arm: ArmSolver2, target: tuple):

    arm.targetToAngles(invertCoord(target))

    pygame.draw.circle(window, (255, 100, 100), invertCoord((arm.baseX, arm.baseY)), arm.maxReach)

    pygame.draw.circle(window, (255, 255, 255), invertCoord((arm.baseX, arm.baseY)), arm.minReach - 2)

    topleft = invertCoord((arm.baseX - 150, arm.baseY))
    robot = pygame.Rect(topleft[0], topleft[1], 200, arm.baseY)
    pygame.draw.rect(surface, (0, 0, 0), robot)

    for jointIdx in range(2):
        
        pygame.draw.line(surface, (0, 255, 0), 
                         invertCoord((arm.joints[jointIdx][0], arm.joints[jointIdx][1])),
                         invertCoord((arm.joints[jointIdx + 1][0], arm.joints[jointIdx + 1][1])), 5)
        
        pygame.draw.circle(surface, (0, 0, 255), invertCoord((arm.joints[jointIdx][0], arm.joints[jointIdx][1])), 5)

    pygame.draw.circle(surface, (0, 0, 255), invertCoord((arm.joints[2][0], arm.joints[2][1])), 5)

    pygame.draw.circle(surface, (100, 100, 255), (targetX, targetY), 5)

    invertX, invertY = invertCoord((targetX, targetY))

    label(surface, (5, 5), f"({invertX}, {invertY})", (0, 0, 0))
    label(surface, (5, 30), f"Angle 1: {math.degrees(arm.theta1)}", (255, 0, 0))
    label(surface, (5, 55), f"Angle 2: {math.degrees(arm.theta2)}", (0, 0, 255))
    label(surface, (5, 80), f"Target: {targetX, targetY}", (0, 0, 255))


armSolver = ArmSolver2(300, 30, 250, 150)

Ball(600, 0, 300, 135, (0, 0, 255))

targetX, targetY = invertCoord((armSolver.joints[2][0], armSolver.joints[2][1]))

drawArm(window, armSolver, (0, 0))

running = True

while running:

    keys = pygame.key.get_pressed()

    window.fill((255, 255, 255))

    drawArm(window, armSolver, (targetX, targetY))

    for ball in balls:
            
        if pygame.time.get_ticks() % int(1000 / framesPerSecond) == 0:
            
            ball.periodic()

            if math.sqrt((armSolver.joints[2][0] - ball.x) ** 2 + (armSolver.joints[2][1] - ball.y) ** 2) <= 15 and keys[pygame.K_c]:
                
                ball.caught = True
                ball.vX = 0
                ball.vY = 0

            else:
                
                if ball.caught:

                    jointVelocity = armSolver.lastJointVelocity()
                    
                    ball.vX = jointVelocity[0] * framesPerSecond
                    ball.vY = jointVelocity[1] * framesPerSecond

                ball.caught = False

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                
                armSolver.elbowUp = not armSolver.elbowUp
                drawArm(window, armSolver, (targetX, targetY))

    if not balls[-1].caught:

        time = (pygame.time.get_ticks() - balls[-1].start) / 1000

        newTargetX = balls[-1].x + (balls[-1].vX * (1.5 - time))
        newTargetY = balls[-1].y + (balls[-1].vY * (1.5 - time)) - 2.5 * (1.5 - time) ** 2
            
        targetX += (newTargetX - targetX) * 0.05
        targetY += ((600 - newTargetY) - targetY) * 0.05

    elif balls[-1].caught or balls[-1].x < 0 or (abs(balls[-1].vY <= 3 and balls[-1].vX <= 3 and balls[-1].y <= 3)):

        del balls[-1]
        Ball(600, 0, random.randrange(100, 250), random.randrange(100, 135), (0, 0, 255))

    if keys[pygame.K_i]:

        armSolver.baseX -= 0.4
        targetX -= 0.4

    if keys[pygame.K_p]:

        armSolver.baseX += 0.4
        targetX += 0.4