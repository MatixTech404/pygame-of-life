import pygame as pg
import pygame.locals as pgc  # pygame constants

from wgrid import WGrid
from button_group import ButtonGroup
import colors as c

# our constants
WIDTH, HEIGHT = 700, 600
FPS = 60

pg.init()
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

grid = WGrid(WINDOW, None, (0, 0), (600, 600), margin=1)

actions = [grid.evolve, grid.enable_auto_evolve, grid.set_grid, grid.set_random_grid]
symbols = [pg.image.load(r'icons\1.png'), pg.image.load(r'icons\2.png'),
           pg.image.load(r'icons\3.png'), pg.image.load(r'icons\4.png')]
buttons = ButtonGroup(WINDOW, (610, 10), (0, 100), (80, 80), actions, symbols)

clock = pg.time.Clock()
run = True
while run:
    for e in pg.event.get():
        if e.type == pgc.QUIT:
            run = False
        if e.type == pgc.MOUSEBUTTONDOWN:
            if e.button == pgc.BUTTON_LEFT:
                pos = e.pos
                if grid.click(pos):
                    grid.toggle_cell(pos[0], pos[1])
                elif (b := buttons.point_touches(pos)) + 1:
                    buttons.click(b)
            if e.button == pgc.BUTTON_RIGHT:
                grid.evolve()
        if e.type == pgc.KEYDOWN:
            if e.key == pgc.K_SPACE:
                grid.enable_auto_evolve()
            if e.key == pgc.K_c:
                grid.set_grid()
            if e.key == pgc.K_r:
                grid.set_random_grid()

    WINDOW.fill(c.BLACK)

    grid.draw()
    buttons.draw()

    pg.display.set_caption(f'FPS: {clock.get_fps()}')
    pg.display.update()
    clock.tick(FPS)

pg.quit()
