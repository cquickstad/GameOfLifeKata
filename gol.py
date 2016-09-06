#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from enum import Enum
from position import Position
import pygame
import sys
from time import sleep


class CellState(Enum):
    DEAD, ALIVE = range(2)


class Gol:
    def __init__(self):
        self.universe = dict()

    def get_state(self, pos):
        assert isinstance(pos, Position)
        return self.universe[pos] if pos in self.universe else CellState.DEAD

    def set_state(self, pos, state):
        assert isinstance(pos, Position)
        assert isinstance(state, CellState)
        if state == CellState.DEAD:
            if pos in self.universe:
                _ = self.universe.pop(pos)
        else:
            self.universe[pos] = state

    def make_alive(self, pos):
        self.set_state(pos, CellState.ALIVE)

    def get_cells_to_step(self):
        cells_to_step = set()
        for pos in self.universe.keys():
            cells_to_step.add(pos)
            cells_to_step = cells_to_step.union(pos.get_neighbors())
        return cells_to_step

    def step(self):
        next_universe = dict()
        for pos in self.get_cells_to_step():
            next_cell_state = self.next_cell_state(self.get_state(pos), self.count_alive_neighbors(pos))
            if next_cell_state == CellState.ALIVE:
                next_universe[pos] = next_cell_state
        self.universe = next_universe

    def get_universe(self):
        return self.universe

    def count_alive_neighbors(self, pos):
        assert isinstance(pos, Position)
        num_alive_neighbors = 0
        for neighbor in pos.get_neighbors():
            if self.get_state(neighbor) == CellState.ALIVE:
                num_alive_neighbors += 1
        return num_alive_neighbors

    @staticmethod
    def next_cell_state(current_cell_state, number_of_alive_neighbors):
        if Gol.birth_condition(number_of_alive_neighbors):
            return CellState.ALIVE
        if Gol.starvation_condition(number_of_alive_neighbors) or Gol.overcrowding_condition(number_of_alive_neighbors):
            return CellState.DEAD
        return current_cell_state

    @staticmethod
    def starvation_condition(number_of_alive_neighbors):
        return number_of_alive_neighbors < 2

    @staticmethod
    def overcrowding_condition(number_of_alive_neighbors):
        return number_of_alive_neighbors > 3

    @staticmethod
    def birth_condition(number_of_alive_neighbors):
        return number_of_alive_neighbors == 3
