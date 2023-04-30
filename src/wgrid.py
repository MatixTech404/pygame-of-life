import pygame as pg
import pygame.locals as pgc  # pygame constants

from grid import Grid
import colors as c


def _handle_keypress(percent, e):
    if e.key == pgc.K_0:
        if percent <= 10:
            percent = 10 * percent
    if e.key == pgc.K_1:
        if percent < 10:
            percent = 10 * percent + 1
    if e.key == pgc.K_2:
        if percent < 10:
            percent = 10 * percent + 2
    if e.key == pgc.K_3:
        if percent < 10:
            percent = 10 * percent + 3
    if e.key == pgc.K_4:
        if percent < 10:
            percent = 10 * percent + 4
    if e.key == pgc.K_5:
        if percent < 10:
            percent = 10 * percent + 5
    if e.key == pgc.K_6:
        if percent < 10:
            percent = 10 * percent + 6
    if e.key == pgc.K_7:
        if percent < 10:
            percent = 10 * percent + 7
    if e.key == pgc.K_8:
        if percent < 10:
            percent = 10 * percent + 8
    if e.key == pgc.K_9:
        if percent < 10:
            percent = 10 * percent + 9
    return percent


class WGrid:
    def __init__(self, window, grid, left_top, rect_size, grid_size=(50, 50), margin=5):
        if grid is None:
            grid = Grid(*grid_size)
        self.window = window
        self.grid = grid
        self.rect = pg.Rect(left_top, rect_size)

        # for auto evolving
        self._auto_evolve = False
        self._count = 0
        self.max_count = 6

        a = self.rect.width / grid.width - 2 * margin
        b = self.rect.height / grid.height - 2 * margin
        self.cells = [
            [pg.Rect((i*a + (2*i + 1) * margin, j*b + (2*j + 1) * margin), (a, b))
                for i in range(grid.width)] for j in range(grid.height)
        ]

    def set_grid(self):
        self.grid.set_grid()

    def set_random_grid(self):
        ask = True
        percent = 0

        prompt = pg.Surface((520, 220))
        font = pg.font.SysFont('Seoge UI', 60)
        txt_ask = font.render('How much percent to fill?', True, c.WHITE)
        txt_ask_rect = txt_ask.get_rect(center=(260, 70))
        while ask:
            for e in pg.event.get():
                if e.type == pgc.QUIT:
                    return True
                if e.type == pgc.KEYDOWN:
                    percent = _handle_keypress(percent, e)

                    if e.key == pgc.K_BACKSPACE:
                        percent //= 10
                    if e.key == pgc.K_RETURN:
                        ask = False
                    if e.key == pgc.K_ESCAPE:
                        return False

            txt_pcnt = font.render(str(percent), True, c.WHITE)
            txt_pcnt_rect = txt_pcnt.get_rect(right=510, centery=160)

            prompt.fill(c.BLACK)
            pg.draw.rect(prompt, c.RED, pg.Rect((0, 0), (520, 220)), 5)

            prompt.blit(txt_ask, txt_ask_rect)
            prompt.blit(txt_pcnt, txt_pcnt_rect)

            self.window.blit(prompt, (90, 190))
            pg.display.update()

        self.grid.set_random_grid(percent)
        return False

    def auto_evolve(self):
        if not self._auto_evolve:
            self._count = 0
            return
        if self._count == self.max_count:
            self.grid.evolve()
            self._count = 0
            return
        self._count += 1

    def click(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self):
        self.auto_evolve()

        pg.draw.rect(self.window, c.DARK_GREY, self.rect)
        for ri, ci in zip(self.cells, self.grid.get_grid()):
            for rj, cj in zip(ri, ci):
                pg.draw.rect(self.window, c.RED if cj else c.BLACK, rj)

    def evolve(self):
        if not self._auto_evolve:
            self.grid.evolve()

    def enable_auto_evolve(self, enable=None):
        if enable is None:
            enable = not self._auto_evolve
        self._auto_evolve = enable

    def toggle_cell(self, xpos, ypos):
        for y, ri in enumerate(self.cells):
            for x, rj in enumerate(ri):
                if rj.collidepoint(xpos, ypos):
                    self.grid.toggle_cell(x, y)
                    break
