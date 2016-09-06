#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from enum import Enum
from position import Pos


class CellState(Enum):
    DEAD, ALIVE = range(2)


class Gol:
    def __init__(self):
        self.universe = dict()

    def get_state(self, pos):
        assert isinstance(pos, Pos)
        return self.universe[pos] if pos in self.universe else CellState.DEAD

    def make_alive(self, pos):
        self.universe[pos] = CellState.ALIVE

    def make_dead(self, pos):
        if pos in self.universe:
            _ = self.universe.pop(pos)

    def get_cells_to_step(self):
        cells_to_step = set()
        for pos in self.universe.keys():
            cells_to_step.add(pos)
            cells_to_step = cells_to_step.union(pos.get_neighbors())
        return cells_to_step

    def step(self):
        next_universe = dict()
        for pos in self.get_cells_to_step():
            next_cell_state = self.next_cell_state(self.get_state(pos), self.num_alive_neighbors(pos))
            if next_cell_state == CellState.ALIVE:
                next_universe[pos] = next_cell_state
        self.universe = next_universe

    def get_universe(self):
        return self.universe

    def num_alive_neighbors(self, pos):
        assert isinstance(pos, Pos)
        alive_neighbor_count = 0
        for neighbor in pos.get_neighbors():
            if self.get_state(neighbor) == CellState.ALIVE:
                alive_neighbor_count += 1
        return alive_neighbor_count

    @staticmethod
    def next_cell_state(current_cell_state, num_alive_neighbors):
        if Gol.is_birth(num_alive_neighbors):
            return CellState.ALIVE
        if Gol.is_starvation(num_alive_neighbors) or Gol.is_overcrowding(num_alive_neighbors):
            return CellState.DEAD
        return current_cell_state

    @staticmethod
    def is_starvation(number_of_alive_neighbors):
        return number_of_alive_neighbors < 2

    @staticmethod
    def is_overcrowding(number_of_alive_neighbors):
        return number_of_alive_neighbors > 3

    @staticmethod
    def is_birth(number_of_alive_neighbors):
        return number_of_alive_neighbors == 3
