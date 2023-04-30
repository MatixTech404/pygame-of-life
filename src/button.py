import pygame as pg
import colors as c


class Button:
    def __init__(self, window, left_top, rect_size, action, symbol):
        self.window = window
        self.rect = pg.Rect(left_top, rect_size)
        self.action = action
        self.symbol = symbol

    def draw(self):
        pg.draw.rect(self.window, c.GREEN, self.rect)
        symbol_rect = self.symbol.get_rect()
        symbol_rect.center = self.rect.center
        self.window.blit(self.symbol, symbol_rect)

    def point_touches(self, point):
        return self.rect.collidepoint(point)

    def click(self):
        return self.action()
