import pygame as pg
import colors as c


class Button:
    def __init__(self, window, left_top, rect_size, action):
        self.window = window
        self.rect = pg.Rect(left_top, rect_size)
        self.action = action

    def draw(self):
        pg.draw.rect(self.window, c.GREEN, self.rect)

    def point_touches(self, point):
        return self.rect.collidepoint(point)

    def click(self):
        self.action()
