#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from position import *


class PositionTest(unittest.TestCase):
    def test_that_get_neighbors_returns_set_of_neighbors_for_0_0(self):
        self.assertEqual({Pos(-1, -1), Pos(0, -1), Pos(1, -1),
                          Pos(-1, 0), Pos(1, 0),
                          Pos(-1, 1), Pos(0, 1), Pos(1, 1)}, Pos(0, 0).get_neighbors())

    def test_that_get_neighbors_returns_set_of_neighbors_for_100_100(self):
        self.assertEqual({Pos(99, 99), Pos(100, 99), Pos(101, 99),
                          Pos(99, 100), Pos(101, 100),
                          Pos(99, 101), Pos(100, 101), Pos(101, 101)},
                         Pos(100, 100).get_neighbors())


if __name__ == '__main__':
    unittest.main()
