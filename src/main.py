import pygame as pg
import pygame.locals as pgc  # pygame constants

from wgrid import WGrid
import colors as c

# our constants
WIDTH, HEIGHT = 700, 600
FPS = 60

pg.init()
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

grid = WGrid(WINDOW, None, (0, 0), (600, 600), margin=1)

buttons = [pg.Rect(610, 100*i+10, 80, 80) for i in range(4)]
actions = ['grid.evolve()', 'evolve = not evolve', 'grid.set_grid()', 'grid.set_random_grid()']

clock = pg.time.Clock()
evolve = False
count = 0
max_count = 6
run = True
while run:
    for e in pg.event.get():
        if e.type == pgc.QUIT:
            run = False
        if e.type == pgc.MOUSEBUTTONDOWN:
            if e.button == pgc.BUTTON_LEFT:
                pos = e.pos
                if grid.rect.collidepoint(pos):
                    grid.toggle_cell(pos[0], pos[1])
                elif (b := pg.Rect(pos, (1, 1)).collidelist(buttons))+1:
                    exec(actions[b])  # I know it's not the most elegant solution, but it works ;-)
            if e.button == pgc.BUTTON_RIGHT:
                grid.evolve()
        if e.type == pgc.KEYDOWN:
            if e.key == pgc.K_SPACE:
                evolve = not evolve
            if e.key == pgc.K_c:
                grid.set_grid()
            if e.key == pgc.K_r:
                grid.set_random_grid()

    if evolve and count == max_count:
        grid.evolve()
        count = 0
    elif evolve:
        count += 1
    else:
        count = 0

    WINDOW.fill(c.BLACK)

    grid.draw()
    for i in buttons:
        pg.draw.rect(WINDOW, c.GREY, i)

    pg.display.update()
    clock.tick(FPS)

pg.quit()
