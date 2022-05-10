import math

size = 300
depth = 0
cords = [[100, 400], [800, 400]]

def koch_curve(n, line):
    if n != 0:
        w = line[1][0] - line[0][0]
        h = line[1][1] - line[0][1]
        H = math.hypot(w, h)

        x1 = line[0][0] + w / 3
        y1 = line[0][1] + h / 3

        x2 = line[0][0] + w / 3 * 2
        y2 = line[0][1] + h / 3 * 2

        point1 = [x1, y1]
        point3 = [x2, y2]

        alpha = 2 * math.pi / 3 + math.atan(h / w) if w != 0 else 0

        if line[0][0] > line[1][0]:
            alpha += math.pi

        point2 = [x1 - H / 3 * math.cos(alpha), y1 - H / 3 * math.sin(alpha)]

        return [
            *koch_curve(n - 1, [line[0], point1]),
            *koch_curve(n - 1, [point1, point2]),
            *koch_curve(n - 1, [point2, point3]),
            *koch_curve(n - 1, [point3, line[1]]),
        ]

    return line

# def count_time(func, *args):
#     import time
#     start = time.time()
#     func(*args)
#     print("Максимальня глубина: " + str(args[0]))
#     print("Количество итераций: " + str(i))
#     print("Время выполнения: " + str(time.time() - start))

#count_time(koch_curve, depth, cords)


import pygame
WIDTH = 900
HEIGHT = 500
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

def drawPath(path):
  pygame.draw.lines(screen, (0, 0, 0), False, path, 1)

def update():
    screen.fill((255, 255, 255))
    pygame.key.set_text_input_rect(pygame.Rect((0, 600), (240, 240)))
    drawPath(koch_curve(depth, cords))
    pygame.display.flip()

update()

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            depth = int(event.unicode)
            update()