from button import Button


class ButtonGroup:
    def __init__(self, window, startpoint, position_change, button_size, actions):
        self.button_list = []
        for i, action in enumerate(actions):
            left_top = (startpoint[0]+i*position_change[0], startpoint[1]+i*position_change[1])
            self.button_list.append(Button(window, left_top, button_size, action))

        self.n_of_buttons = len(self.button_list)

    def point_touches(self, point):
        for i, button in enumerate(self.button_list):
            if button.point_touches(point):
                return i
        return -1

    def click(self, button_number):
        if button_number >= self.n_of_buttons:
            raise IndexError('button_number is too high')
        self.button_list[button_number].click()

    def draw(self):
        for i in self.button_list:
            i.draw()
