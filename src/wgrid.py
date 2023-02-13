import pygame as pg

from grid import Grid
from colors import *


class WGrid:
    def __init__(self, window, grid, left_top, rect_size, grid_size=(50, 50), margin=5):
        if grid is None:
            grid = Grid(*grid_size)
        self.window = window
        self.grid = grid
        self.rect = pg.Rect(left_top, rect_size)

        a = self.rect.width / grid.width - 2 * margin
        b = self.rect.height / grid.height - 2 * margin
        self.cells = [
            [pg.Rect((i*a + (2*i + 1) * margin, j*b + (2*j + 1) * margin), (a, b))
                for i in range(grid.width)] for j in range(grid.height)
        ]

    def set_grid(self, new_grid=None):
        self.grid.set_grid(new_grid)

    def set_random_grid(self):
        self.grid.set_random_grid()

    def draw(self):
        pg.draw.rect(self.window, DARK_GREY, self.rect)
        for ri, ci in zip(self.cells, self.grid.get_grid()):
            for rj, cj in zip(ri, ci):
                pg.draw.rect(self.window, RED if cj else BLACK, rj)

    def evolve(self):
        self.grid.evolve()

    def toggle_cell(self, xpos, ypos):
        for y, ri in enumerate(self.cells):
            for x, rj in enumerate(ri):
                if rj.collidepoint(xpos, ypos):
                    self.grid.toggle_cell(x, y)
                    break
