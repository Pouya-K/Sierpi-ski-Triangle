import math
import pygame
import random

sideLength = int(input("Enter triangle side length: "))

def areaOfTriangle(a, b, c):
    d1 = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))  # AB
    d2 = math.sqrt(pow(a[0] - c[0], 2) + pow(a[1] - c[1], 2))  # AC
    d3 = math.sqrt(pow(b[0] - c[0], 2) + pow(b[1] - c[1], 2))  # BC
    semi = (d1 + d2 + d3) / 2
    return math.sqrt(semi * (semi - d1) * (semi - d2) * (semi - d3))


def isInTriangle(corner1, corner2, corner3, point):
    # 1 = A, 2 = B, 3 = C, point = P
    totalArea = areaOfTriangle(corner1, corner2, corner3)
    areaABP = areaOfTriangle(corner1, corner2, point)
    areaACP = areaOfTriangle(corner1, corner3, point)
    areaPCB = areaOfTriangle(corner3, corner2, point)
    return round(totalArea) == round(areaPCB + areaACP + areaABP)


def makeSierpinsky(surface, corner1, corner2, corner3, triangleHeight, point):
    if point[0] == 0 and point[1] == 0:
        inTriangle = False;
        while inTriangle == False:
            point = (random.randrange(50, 250), random.randrange(50, int(50 + triangleHeight)))
            inTriangle = isInTriangle(corner1, corner2, corner3, point)
    connecting = random.choice([corner1, corner2, corner3])
    point = ((point[0] + connecting[0]) / 2, (point[1] + connecting[1]) / 2)
    pygame.draw.circle(surface, (255, 255, 255), point, 1)
    return point


WIDTH = sideLength + 100
HEIGHT = sideLength + 100
win = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
win.fill((0, 0, 0))
triangleHeight = math.sqrt((pow(sideLength, 2)) - (pow(sideLength / 2, 2)))
corner1 = (50, 50 + triangleHeight)
corner2 = (50 + sideLength, 50 + triangleHeight)
corner3 = (50 + sideLength / 2, 50)
point = (0,0)
makeTriangle = False
clock = pygame.time.Clock()

pygame.display.set_caption('Sierpinski Triangle Demonstration')

while run:
    clock.tick(sideLength / 3.333333)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                makeTriangle = True

    pygame.draw.polygon(win, (255, 255, 255), [corner1, corner2, corner3], 2)
    if makeTriangle:
        point = makeSierpinsky(win, corner1, corner2, corner3, triangleHeight, point)
    pygame.display.flip()

pygame.quit()
