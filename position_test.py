import unittest
from position import *


class PositionTest(unittest.TestCase):
    def test_that_get_neighbors_returns_set_of_neighbors_for_0_0(self):
        self.assertEqual({Position(-1, -1), Position(0, -1), Position(1, -1),
                          Position(-1, 0), Position(1, 0),
                          Position(-1, 1), Position(0, 1), Position(1, 1)}, Position(0, 0).get_neighbors())

    def test_that_get_neighbors_returns_set_of_neighbors_for_100_100(self):
        self.assertEqual({Position(99, 99), Position(100, 99), Position(101, 99),
                          Position(99, 100), Position(101, 100),
                          Position(99, 101), Position(100, 101), Position(101, 101)},
                         Position(100, 100).get_neighbors())


if __name__ == '__main__':
    unittest.main()
