from position import *
from gol import *


class GolGfx:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.orchid = (218, 112, 214)
        self.skyblue = (135, 206, 235)
        self.window_resolution = (1280, 720)
        self.cell_width = 10
        self.cell_height = 10
        self.display = pygame.display.set_mode(self.window_resolution)

    def clear(self):
        self.display.fill(self.skyblue)

    def cell_pos_to_px(self, pos):
        x = pos.x * self.cell_width
        y = pos.y * self.cell_height
        return x, y

    def add_cell_at_pos(self, pos):
        cell_color = self.orchid
        x, y = self.cell_pos_to_px(pos)
        width, height = self.cell_width, self.cell_height
        thickness = 0
        rect = (x, y, width, height)
        pygame.draw.rect(self.display, cell_color, rect, thickness)

    def plot_universe(self, universe):
        self.clear()
        for pos in universe:
            self.add_cell_at_pos(pos)
        pygame.display.update()


def add_x_y_list_to_base_pos(game, base_pos, x_y_list):
    for x, y in x_y_list:
        game.make_alive(Position(base_pos.x + x, base_pos.y + y))


def add_blinker_to_game(game, base_pos):
    add_x_y_list_to_base_pos(game, base_pos, [(0, 0), (1, 0), (0, 1), (3, 2), (2, 3), (3, 3)])


def add_glider_to_game(game, base_pos):
    add_x_y_list_to_base_pos(game, base_pos, [(2, 0), (2, 1), (2, 2), (1, 2), (0, 1)])


def add_gosper_glider_gun_to_game(game, base_pos):
    x_y_list = [(0, 4), (0, 5), (1, 4), (1, 5), (10, 4), (10, 5), (10, 6), (11, 3), (11, 7), (12, 2), (12, 8), (13, 2),
                (13, 8), (14, 5), (15, 3), (15, 7), (16, 4), (16, 5), (16, 6), (17, 5), (20, 2), (20, 3), (20, 4),
                (21, 2), (21, 3), (21, 4), (22, 1), (22, 5), (24, 0), (24, 1), (24, 5), (24, 6), (34, 2), (34, 3),
                (35, 2), (35, 3)]
    add_x_y_list_to_base_pos(game, base_pos, x_y_list)


if __name__ == '__main__':
    num_generations = 300
    generation_seconds = 0.125 / 4

    game = Gol()
    add_blinker_to_game(game, Position(40, 40))
    add_glider_to_game(game, Position(5, 5))
    add_gosper_glider_gun_to_game(game, Position(20, 0))

    gfx = GolGfx()
    gfx.plot_universe(game.get_universe())

    for _ in range(num_generations):
        sleep(generation_seconds)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.step()
        gfx.plot_universe(game.get_universe())
