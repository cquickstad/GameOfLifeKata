#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from position import Pos
from gol import Gol, CellState


class GolTest(unittest.TestCase):
    def setUp(self):
        self.game = Gol()

    def test_that_empty_cell_is_dead(self):
        self.assertEqual(CellState.DEAD, self.game.get_state(Pos(0, 0)))

    def test_that_cell_can_be_made_alive(self):
        self.game.set_state(Pos(0, 0), CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, self.game.get_state(Pos(0, 0)))

    def test_that_two_cells_can_be_made_alive(self):
        self.game.set_state(Pos(0, 0), CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, self.game.get_state(Pos(0, 0)))
        self.assertEqual(CellState.DEAD, self.game.get_state(Pos(3, 1)))

        self.game.set_state(Pos(3, 1), CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, self.game.get_state(Pos(0, 0)))
        self.assertEqual(CellState.ALIVE, self.game.get_state(Pos(3, 1)))

    def test_that_cell_can_be_made_dead_after_being_alive(self):
        self.game.set_state(Pos(0, 0), CellState.ALIVE)
        self.game.set_state(Pos(0, 0), CellState.DEAD)
        self.assertEqual(CellState.DEAD, self.game.get_state(Pos(0, 0)))

    def test_that_one_alive_cell_dies_of_starvation(self):
        self.game.set_state(Pos(5, 6), CellState.ALIVE)
        self.game.step()
        self.assertEqual(dict(), self.game.get_universe())

    def test_next_cell_state(self):
        self.assertEqual(CellState.DEAD, Gol.next_cell_state(CellState.DEAD, 1))
        self.assertEqual(CellState.ALIVE, Gol.next_cell_state(CellState.ALIVE, 2))
        self.assertEqual(CellState.DEAD, Gol.next_cell_state(CellState.ALIVE, 1))
        self.assertEqual(CellState.ALIVE, Gol.next_cell_state(CellState.DEAD, 3))
        self.assertEqual(CellState.DEAD, Gol.next_cell_state(CellState.ALIVE, 4))

    def test_count_alive_neighbors(self):
        self.assertEqual(0, self.game.num_alive_neighbors(Pos(5, 5)))

        self.game.set_state(Pos(1, 1), CellState.ALIVE)

        self.game.set_state(Pos(4, 4), CellState.ALIVE)
        self.game.set_state(Pos(5, 4), CellState.ALIVE)
        self.game.set_state(Pos(6, 4), CellState.ALIVE)

        self.game.set_state(Pos(4, 5), CellState.ALIVE)
        self.game.set_state(Pos(6, 5), CellState.ALIVE)

        self.game.set_state(Pos(4, 6), CellState.ALIVE)
        self.game.set_state(Pos(5, 6), CellState.ALIVE)
        self.game.set_state(Pos(6, 6), CellState.ALIVE)

        self.assertEqual(8, self.game.num_alive_neighbors(Pos(5, 5)))

    def test_blinker(self):
        self.game.set_state(Pos(5, 5), CellState.ALIVE)
        self.game.set_state(Pos(5, 4), CellState.ALIVE)
        self.game.set_state(Pos(5, 6), CellState.ALIVE)
        self.game.step()
        self.assertEqual({Pos(4, 5): CellState.ALIVE,
                          Pos(5, 5): CellState.ALIVE,
                          Pos(6, 5): CellState.ALIVE},
                         self.game.get_universe())

    def test_that_a_dead_cell_three_alive_neighbors_is_born_in_next_generation(self):
        self.game.set_state(Pos(0, 0), CellState.ALIVE)
        self.game.set_state(Pos(2, 2), CellState.ALIVE)
        self.game.set_state(Pos(2, 0), CellState.ALIVE)
        self.game.step()
        self.assertEqual({Pos(1, 1): CellState.ALIVE}, self.game.get_universe())


if __name__ == '__main__':
    unittest.main()
