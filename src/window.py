import pygame as pg
import pygame.locals as pgc  # pygame constants

import grid
import colors as c

# stałe
WIDTH, HEIGHT = 600, 600

pg.init()
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

grid_obj = grid.Grid()

run = True
while run:
    for e in pg.event.get():
        if e.type == pgc.QUIT:
            run = False

    WINDOW.fill(c.BLACK)

    # pg.draw.rect(WINDOW, c.GREY, pg.Rect(100, 100, 400, 400))

    # pg.draw.rect(WINDOW, c.RED, pg.Rect(200, 200, 200, 200))

    pg.display.update()

pg.quit()
