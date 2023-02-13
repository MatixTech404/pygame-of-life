import pygame as pg
import pygame.locals as pgc  # pygame constants

from wgrid import WGrid
import colors as c

# our constants
WIDTH, HEIGHT = 600, 600

pg.init()
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

grid = WGrid(WINDOW, None, (0, 0), (600, 600), margin=1)

run = True
while run:
    for e in pg.event.get():
        if e.type == pgc.QUIT:
            run = False
        if e.type == pgc.MOUSEBUTTONDOWN and e.button == pgc.BUTTON_LEFT:
            pos = e.pos
            grid.toggle_cell(pos[0], pos[1])
        if e.type == pgc.MOUSEBUTTONDOWN and e.button == pgc.BUTTON_RIGHT:
            grid.evolve()
        if e.type == pgc.KEYDOWN and e.key == pgc.K_SPACE:
            grid.evolve()
        if e.type == pgc.KEYDOWN and e.key == pgc.K_c:
            grid.grid.set_grid()
        if e.type == pgc.KEYDOWN and e.key == pgc.K_r:
            grid.grid.set_random_grid()

    WINDOW.fill(c.BLACK)

    grid.draw()

    pg.display.update()

pg.quit()
