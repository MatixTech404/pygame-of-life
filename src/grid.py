import random


class Grid:
    def __init__(self, width=50, height=50):
        # zasady dla komórek
        self.newlife = (3,)
        self.life = (3, 2)

        # wielkość siatki
        self.width = width
        self.height = height

        # siatka sama w sobie
        self.grid = [[0] * width for _ in range(height)]

    def get_grid(self):
        # zwróć siatkę
        return self.grid[:]

    def set_grid(self, new_grid):
        # sprawdź poprawność wielkości nowej siatki
        if not (len(new_grid) == self.height or len(new_grid[0]) == self.width):
            raise ValueError('size of the new grid is incorrect')

        # zmień wartości siatki
        self.grid = new_grid
        return self

    def set_random_grid(self):
        new_grid = [[0] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                new_grid[i][j] = random.randint(0, 1)

        self.set_grid(new_grid)
        return self

    def get_cell(self, x, y):
        # zwróć wartość konkretnej komórki
        return self.grid[y][x]

    def set_cell(self, x, y, val):
        # sprawdź, czy wartość jest poprawna
        if val not in (0, 1):
            raise ValueError('val can only be 0 or 1')
        self.grid[y][x] = val
    
    def sum_nearby_cells(self, i, j):
        # zmienne dla łatwiejszych odwołań
        g = self.grid
        w = self.width
        h = self.height

        # zwróć sumę pobliskich komórek
        return sum([g[i-1][j-1], g[i-1][j], g[i-1][(j+1) % w],
                    g[i][j-1], g[i][(j+1) % w],
                    g[(i+1) % h][j-1], g[(i+1) % h][j], g[(i+1) % h][(j+1) % w]])

    def compute_new_cell_state(self, cur_cell_state, sum_of_nearby_cells):
        # ustal nowy stan komórki
        new_state = 0
        if cur_cell_state == 0:
            if sum_of_nearby_cells in self.newlife:
                new_state = 1
        else:
            if sum_of_nearby_cells in self.life:
                new_state = 1
        return new_state
    
    def evolve(self):
        # ewoluuj siatkę
        cur_grid = self.grid
        new_grid = [[0] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                cur_cell_state = cur_grid[i][j]
                sum_of_nearby_cells = self.sum_nearby_cells(i, j)
                new_grid[i][j] = self.compute_new_cell_state(cur_cell_state, sum_of_nearby_cells)

        self.grid = new_grid
